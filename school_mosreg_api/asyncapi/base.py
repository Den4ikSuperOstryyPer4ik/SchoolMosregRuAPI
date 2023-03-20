from datetime import date as DATE, datetime
from typing import Optional, TypeVar, Union
import aiohttp
from fake_useragent.fake import UserAgent

from ..types.model import Type
from ..exceptions import raise_error, all_error_types_str, all_error_types_str_, APIError, all_error_types_str__dict

_Type = TypeVar("_Type")


class AsyncBaseAPI:
    """
    Basic class for async use schools.school.mosreg.ru API
    ``(api.school.mosreg.ru)``
    """
    
    API = "https://api.school.mosreg.ru/"
    
    def __init__(self, login: Optional[str] = None, password: Optional[str] = None, token: Optional[str] = None) -> None:
        self.login = login
        self.password = password
        self.token = token
        
        self.UserAgentDict = {
            "User-Agent": self.get_random_UserAgent()
        }
        
        if not self.token:
            if not self.login:
                raise ValueError("Token and login is None. Please add to arguments ``login=LOGIN, password=PASSWORD`` or ``token=TOKEN``")
            elif not self.password:
                raise ValueError("Token and password is None. Please add to arguments ``login=LOGIN, password=PASSWORD`` or ``token=TOKEN``")
            else:
                self.token = None
    
    @staticmethod
    def get_random_UserAgent():
        return UserAgent().random
    
    @staticmethod
    def datetime_to_string(time: Optional[Union[datetime, DATE]] = None) -> str:
        """Сконвертировать datetime.datetime объект в строку(``str``) для использования в URL (METHOD)\n~~~"""
        if not time:
            time = datetime.now()
        return f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}" if isinstance(time, datetime) else f"{time.year}-{time.month}-{time.day}"
    
    @staticmethod
    def date_to_string(date: Optional[Union[datetime, DATE]] = None) -> str:
        """Сконвертировать datetime.date объект в строку(``str``) для использования в URL (METHOD)\n~~~"""
        if not date:
            date = DATE.today()
        return f"{date.year}-{date.month}-{date.day}"

    @classmethod
    def get_headers(cls, token: str):
        if not token:
            raise ValueError("Token is required!\nCode: API.token = await API.get_token()")
        return {
            "Access-token": token,
            **cls.get_random_UserAgent()
        }
    
    @property
    def headers(self):
        if not self.token:
            raise ValueError("Token is required!\nCode: API.token = await API.get_token()")
        return {
            "Access-token": self.token,
            **self.UserAgentDict
        }
    
    @property
    def DEFAULT_GET_TOKEN_PARAMS(self):
        return {
            "ReturnUrl": (
                "https://login.school.mosreg.ru/oauth2?"
                "response_type=token&client_id=bafe713c96a342b194d040392cadf82b"
                "&scope=EducationalInfo,CommonInfo,FriendsAndRelatives,SocialInfo,ContactInfo"
            ),
            "login": self.login, "password": self.password
        }
    
    async def get_token(self, params: Optional[dict] = None):
        """
        Get Token with login&password
        
        :param:params - dict -> {"ReturnUrl": "...", "login": "...", "password": "..."}
        """
        if not params:
            params = self.DEFAULT_GET_TOKEN_PARAMS
            
        URL = "https://login.school.mosreg.ru/login/"
        async with aiohttp.ClientSession() as session:
            async with session.post(URL, headers=self.UserAgentDict, params=params, allow_redirects=True) as resp:
                if resp.real_url.query.get("result") != "success":
                    resp = await session.post(params["ReturnUrl"])
                    
                    if resp.real_url.query.get("result") != "success":
                        raise APIError(params["ReturnUrl"], resp.status, "Что-то не так...")

                if resp.status != 200:
                    raise APIError(URL, resp.status,
                        "Сайт лежит или ведутся технические работы, использование API временно невозможно."
                    )
                
                return resp.real_url.fragment.replace("access_token=", "").replace("&state=", "")
    
    @staticmethod
    def ParseListModels(model: _Type, text: str) -> list[_Type]:
        class ListModels(Type):
            listik: list[model] 
        
        return ListModels.parse_raw('{"listik": '+ text.replace("'", '"') + '}').listik
    
    @staticmethod
    async def _check_response(response: aiohttp.ClientResponse):
        if response.content_type == "text/html":
            error_html = await response.text()
            if "502" in error_html:
                raise_error(url=str(response.url), status_code=response.status, error_type="HTMLError", description=error_html)
            
            error_text = " ".join(
                word
                for word in error_html.split('<div class="error__description">')[-1]
                .split("<p>")[1]
                .strip()[:-4]
                .split()
            )
            raise_error(url=str(response.url), status_code=response.status, error_type="HTMLError", description=error_text)
        
        json_response = await response.json()

        if isinstance(json_response, dict):
            if json_response.get("type") in all_error_types_str or json_response.get("type") in all_error_types_str_ or json_response.get("type") in all_error_types_str__dict.keys():
                raise_error(url=str(response.url), status_code=response.status, error_type=json_response.get("type", "unknownError"), description=json_response.get("description", None))
    
    async def get(
        self,
        method: str,
        headers: Optional[dict] = None,
        model: Optional[Type] = None,
        is_list: bool = False,
        return_json: bool = False,
        return_raw_text: bool = False,
        required_token: bool = True,
        **kwargs
    ):
        if not headers:
            headers = self.headers if required_token else self.UserAgentDict

        async with aiohttp.ClientSession() as session:
            async with session.get(
                (self.API + method) if not method.startswith(self.API) else method,
                headers=headers, **kwargs
            ) as response:
                await self._check_response(response)
                RAW_TEXT = await response.text()
                
                return (
                    await response.json()
                    if return_json
                    else RAW_TEXT
                    if return_raw_text
                    else self.ParseListModels(model, RAW_TEXT)
                    if is_list
                    else model.parse_raw(RAW_TEXT)
                    if model
                    else RAW_TEXT
                )
    
    async def post(
        self,
        method: str,
        headers: Optional[dict] = None,
        json = None,
        data = None,
        model: Optional[Type] = None,
        is_list: bool = False,
        return_json: bool = False,
        return_raw_text: bool = False,
        required_token: bool = True,
        **kwargs
    ):
        if not headers:
            headers = self.headers if required_token else self.UserAgentDict

        async with aiohttp.ClientSession() as session:
            async with session.post(
                (self.API + method) if not method.startswith(self.API) else method,
                headers=headers, json=json, data=data, **kwargs
            ) as response:
                await self._check_response(response)
                RAW_TEXT = await response.text()
                
                return (
                    await response.json()
                    if return_json
                    else RAW_TEXT
                    if return_raw_text
                    else self.ParseListModels(model, RAW_TEXT)
                    if is_list
                    else model.parse_raw(RAW_TEXT)
                    if model
                    else RAW_TEXT
                )

    async def put(
        self,
        method: str,
        headers: Optional[dict] = None,
        json = None,
        data = None, 
        model: Optional[Type] = None,
        is_list: bool = False,
        return_json: bool = False,
        return_raw_text: bool = False,
        required_token: bool = True,
        **kwargs
    ):
        if not headers:
            headers = self.headers if required_token else self.UserAgentDict

        async with aiohttp.ClientSession() as session:
            async with session.put(
                (self.API + method) if not method.startswith(self.API) else method, headers=headers, json=json, data=data, **kwargs
            ) as response:
                await self._check_response(response)
                RAW_TEXT = await response.text()
                
                return (
                    await response.json()
                    if return_json
                    else RAW_TEXT
                    if return_raw_text
                    else self.ParseListModels(model, RAW_TEXT)
                    if is_list
                    else model.parse_raw(RAW_TEXT)
                    if model
                    else RAW_TEXT
                )
    
    async def delete(
        self,
        method: str,
        headers: Optional[dict] = None,
        json = None,
        data = None,
        model: Optional[Type] = None,
        is_list: bool = False,
        return_json: bool = False,
        return_raw_text: bool = False, 
        required_token: bool = True,
        **kwargs
    ):
        if not headers:
            headers = self.headers if required_token else self.UserAgentDict

        async with aiohttp.ClientSession() as session:
            async with session.delete(
                (self.API + method) if not method.startswith(self.API) else method, headers=headers, json=json, data=data, **kwargs
            ) as response:
                await self._check_response(response)
                RAW_TEXT = await response.text()
                
                return (
                    await response.json()
                    if return_json
                    else RAW_TEXT
                    if return_raw_text
                    else self.ParseListModels(model, RAW_TEXT)
                    if is_list
                    else model.parse_raw(RAW_TEXT)
                    if model
                    else RAW_TEXT
                )

