from datetime import date, datetime
import aiohttp, asyncio

from pydantic import BaseModel

from ..exceptions import raise_error, all_error_types_str, all_error_types_str_, APIError, all_error_types_str__dict


class AsyncBaseAPI:
    """
    Basic class for async use schools.school.mosreg.ru API
    ``(api.school.mosreg.ru)``
    """
    
    def __init__(self, login: str = None, password: str = None, token: str = None) -> None:
        self.login = login
        self.password = password
        self.token = token
        
        self.API = "https://api.school.mosreg.ru/v2.0/"
        
        self.UserAgentDict = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}
        
        if self.token is None:
            if self.login is None:
                raise ValueError("Token and login is None. Please add to arguments ``login=LOGIN, password=PASSWORD`` or ``token=TOKEN``")
            elif self.password is None:
                raise ValueError("Token and password is None. Please add to arguments ``login=LOGIN, password=PASSWORD`` or ``token=TOKEN``")
            else:
                self.token = asyncio.get_event_loop().run_until_complete(self.get_token())
    
    @staticmethod
    def datetime_to_string(time: datetime | date = datetime.now()) -> str:
        """Сконвертировать datetime.datetime объект в строку(``str``) для использования в URL (METHOD)\n~~~"""
        return f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}" if isinstance(time, datetime) else f"{time.year}-{time.month}-{time.day}"
    
    @staticmethod
    def date_to_string(date: date = date.today()) -> str:
        """Сконвертировать datetime.date объект в строку(``str``) для использования в URL (METHOD)\n~~~"""
        return f"{date.year}-{date.month}-{date.day}"

    @staticmethod
    def get_headers(token: str):
        return {"Access-token": token}
    
    @property
    def headers(self):
        return {"Access-token": self.token}
    
    async def get_token(self, params: dict = None):
        """
        Get Token with login&password
        
        :param:params - dict -> {"ReturnUrl": "...", "login": "...", "password": "..."}
        """
        
        params = params or {
            "ReturnUrl": "https://login.school.mosreg.ru/oauth2?response_type=token&client_id=bafe713c96a342b194d040392cadf82b&scope=EducationalInfo,CommonInfo,FriendsAndRelatives,SocialInfo,ContactInfo",
            "login": self.login, "password": self.password
        }
        URL = "https://login.school.mosreg.ru/login/"
        async with aiohttp.ClientSession() as session:
            async with session.post(URL, headers=self.UserAgentDict, params=params, allow_redirects=True) as resp:
                if resp.real_url.query.get("result") != "success":
                    resp = await session.post(params["ReturnUrl"])
                    
                    if resp.real_url.query.get("result") != "success":
                        raise APIError(params["ReturnUrl"], resp.status, "Что-то не так...")

                if resp.status != 200:
                    raise APIError(URL, resp.status,
                        "Сайт лежит или ведутся технические работы, использование api временно невозможно"
                    )
                
                return resp.real_url.fragment.replace("access_token=", "").replace("&state=", "")
    
    
    def ParseListModels(self, model: BaseModel, text: str) -> list[BaseModel]:
        class ListModels(BaseModel):
            listik: list[model]
        
        return ListModels.parse_raw('{"listik": '+ text.replace("'", '"') + '}').listik
    
    @staticmethod
    async def _check_response(response: aiohttp.ClientResponse):
        if response.content_type == "text/html":
            error_html = await response.text()
            if "502" in error_html:
                raise_error(url=response.url, status_code=response.status, error_type="HTMLError", description=error_html)
            
            error_text = " ".join(
                word
                for word in error_html.split('<div class="error__description">')[-1]
                .split("<p>")[1]
                .strip()[:-4]
                .split()
            )
            raise_error(url=response.url, status_code=response.status, error_type="HTMLError", description=error_text)
        
        json_response = await response.json()

        if isinstance(json_response, dict):
            if json_response.get("type") in all_error_types_str or json_response.get("type") in all_error_types_str_ or json_response.get("type") in all_error_types_str__dict.keys():
                raise_error(url=response.url, status_code=response.status, error_type=json_response.get("type"), description=json_response.get("description", None))
    
    async def get(self, method: str, headers: dict = None, model: BaseModel | None = None, is_list: bool = False, return_json: bool = False, return_raw_text: bool = False, **kwargs):
        async with aiohttp.ClientSession() as session:
            headers = headers or self.headers
            if headers.get("User-Agent", None) is None:
                headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"})
            
            async with session.get(
                self.API + method, headers=headers, **kwargs
            ) as response:
                await self._check_response(response)
                RAW_TEXT = await response.text()
                
                if return_json:
                    return await response.json()
                elif return_raw_text:
                    return RAW_TEXT
                elif is_list:
                    return self.ParseListModels(model, (RAW_TEXT))
                else:
                    return model.parse_raw((RAW_TEXT))
    
    async def post(self, method: str, headers: dict = None, json = None, data = None, model: BaseModel | None = None, is_list: bool = False, return_json: bool = False, return_raw_text: bool = False, **kwargs):
        async with aiohttp.ClientSession() as session:
            headers = headers or self.headers
            if headers.get("User-Agent", None) is None:
                headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"})
            
            async with session.post(
                self.API + method, headers=headers, json=json, data=data, **kwargs
            ) as response:
                await self._check_response(response)
                RAW_TEXT = await response.text()
                
                if return_json:
                    return await response.json()
                elif return_raw_text:
                    return RAW_TEXT
                elif is_list:
                    return self.ParseListModels(model, (RAW_TEXT))
                else:
                    return model.parse_raw((RAW_TEXT))

    async def put(self, method: str, headers: dict = None, json = None, data = None, model: BaseModel | None = None, is_list: bool = False, return_json: bool = False, return_raw_text: bool = False, **kwargs):
        async with aiohttp.ClientSession() as session:
            headers = headers or self.headers
            if headers.get("User-Agent", None) is None:
                headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"})
            
            async with session.put(
                self.API + method, headers=headers, json=json, data=data, **kwargs
            ) as response:
                await self._check_response(response)
                RAW_TEXT = await response.text()
                
                if return_json:
                    return await response.json()
                elif return_raw_text:
                    return RAW_TEXT
                elif is_list:
                    return self.ParseListModels(model, (RAW_TEXT))
                else:
                    return model.parse_raw((RAW_TEXT))
    
    async def delete(self, method: str, headers: dict = None, json = None, data = None, model: BaseModel | None = None, is_list: bool = False, return_json: bool = False, return_raw_text: bool = False, **kwargs):
        async with aiohttp.ClientSession() as session:
            headers = headers or self.headers
            if headers.get("User-Agent", None) is None:
                headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"})
            
            async with session.delete(
                self.API + method, headers=headers, json=json, data=data, **kwargs
            ) as response:
                await self._check_response(response)
                RAW_TEXT = await response.text()
                
                if return_json:
                    return await response.json()
                elif return_raw_text:
                    return RAW_TEXT
                elif is_list:
                    return self.ParseListModels(model, (RAW_TEXT))
                else:
                    return model.parse_raw((RAW_TEXT))
