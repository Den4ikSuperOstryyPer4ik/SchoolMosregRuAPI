from datetime import date, datetime
import re
import requests

from ..types.model import Type
from ..exceptions import raise_error, all_error_types_str, all_error_types_str_, APIError, all_error_types_str__dict
from typing import Optional, TypeVar

_Type = TypeVar("_Type")

class BaseAPI:
    """
    Basic class for sync use schools.school.mosreg.ru API
    ``(api.school.mosreg.ru)``
    """
    
    def __init__(self, login: Optional[str] = None, password: Optional[str] = None, token: Optional[str] = None) -> None:
        self.login = login
        self.password = password
        self.token = token
        self.session = requests.Session()
        
        self.API = "https://api.school.mosreg.ru/v2.0/"
        
        self.UserAgentDict = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}
        
        if self.token is None:
            if self.login is None:
                raise ValueError("Token and login is None. Please add to arguments ``login=LOGIN, password=PASSWORD`` or ``token=TOKEN``")
            elif self.password is None:
                raise ValueError("Token and password is None. Please add to arguments ``login=LOGIN, password=PASSWORD`` or ``token=TOKEN``")
            else:
                self.token = self.get_token()
    
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
    
    def get_token(self, params: Optional[dict] = None):
        """
        Get Token with login&password
        
        :param:params - dict -> {"ReturnUrl": "...", "login": "...", "password": "..."}
        """
        
        if not params:
            params = self.DEFAULT_GET_TOKEN_PARAMS
        
        URL = "https://login.school.mosreg.ru/login/"
        
        resp = self.session.post(URL, params=params, headers=self.UserAgentDict)
        
        if not (token := re.match(
            r"https://login.school.mosreg.ru/oauth2/Authorization/Result\?response_type=token&client_id=bafe713c-96a3-42b1-94d0-40392cadf82b&scope=EducationalInfo&is_granted=False&result=success#access_token=(.{32})&state=",
            resp.url
        )):
            resp = self.session.get(params["ReturnUrl"], headers=self.UserAgentDict)
            
            if not (token := re.match(
                r"https://login.school.mosreg.ru/oauth2/Authorization/Result\?response_type=token&client_id=bafe713c-96a3-42b1-94d0-40392cadf82b&scope=EducationalInfo&is_granted=False&result=success#access_token=(.{32})&state=",
                resp.url
            )):
                raise APIError(resp.url, resp.status_code, "Что-то не так, попробуйте самостоятельно получить API-Token.")

        if resp.status_code != 200:
            raise APIError(resp.url, resp.status_code,
                "Сайт лежит или ведутся технические работы, использование api временно невозможно"
            )
        
        return token.group(1)
    
    
    def ParseListModels(self, model: _Type, text: str) -> list[_Type]:
        class ListModels(Type):
            listik: list[model] #type: ignore
        
        return ListModels.parse_raw('{"listik": '+ text.replace("'", '"') + '}').listik
    
    @staticmethod
    def _check_response(response: requests.Response):
        if response.headers.get("Content-Type") == "text/html":
            error_html = response.content.decode()
            if "502" in error_html:
                raise_error(url=response.url, status_code=response.status_code, error_type="HTMLError", description=error_html)
            
            error_text = " ".join(
                word
                for word in error_html.split('<div class="error__description">')[-1]
                .split("<p>")[1]
                .strip()[:-4]
                .split()
            )
            raise_error(url=response.url, status_code=response.status_code, error_type="HTMLError", description=error_text)
        
        json_response = response.json()

        if isinstance(json_response, dict):
            if json_response.get("type") in all_error_types_str or json_response.get("type") in all_error_types_str_ or json_response.get("type") in all_error_types_str__dict.keys():
                raise_error(url=response.url, status_code=response.status_code, error_type=json_response.get("type") or "unknownError", description=json_response.get("description", None))
    
    
    def get(self, method: str, headers: Optional[dict] = None, model: Optional[Type] = None, is_list: bool = False, return_json: bool = False, return_raw_text: bool = False, **kwargs):
        headers = headers or self.headers
        if headers.get("User-Agent", None) is None:
            headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"})
        
        response = self.session.get(self.API + method, headers=headers, **kwargs)
        
        self._check_response(response)
        RAW_TEXT = response.text
        
        if return_json:
            return response.json()
        elif return_raw_text:
            return RAW_TEXT
        elif is_list and model:
            return self.ParseListModels(model, (RAW_TEXT))
        else:
            return model.parse_raw((RAW_TEXT)) if model else response.json()
    
    def post(self, method: str, headers: Optional[dict] = None, json = None, data = None, model: Optional[Type] = None, is_list: bool = False, return_json: bool = False, return_raw_text: bool = False, **kwargs):
        headers = headers or self.headers
        if headers.get("User-Agent", None) is None:
            headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"})
        
        response = self.session.post(self.API + method, headers=headers, json=json, data=data, **kwargs)
        
        self._check_response(response)
        RAW_TEXT = response.text
        
        if return_json:
            return response.json()
        elif return_raw_text:
            return RAW_TEXT
        elif is_list and model:
            return self.ParseListModels(model, (RAW_TEXT))
        else:
            return model.parse_raw((RAW_TEXT)) if model else response.json()

    def put(self, method: str, headers: Optional[dict] = None, json = None, data = None, model: Optional[Type] = None, is_list: bool = False, return_json: bool = False, return_raw_text: bool = False, **kwargs):
        headers = headers or self.headers
        if headers.get("User-Agent", None) is None:
            headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"})
        
        response = self.session.put(self.API + method, headers=headers, json=json, data=data, **kwargs)
        
        self._check_response(response)
        RAW_TEXT = response.text
        
        if return_json:
            return response.json()
        elif return_raw_text:
            return RAW_TEXT
        elif is_list and model:
            return self.ParseListModels(model, (RAW_TEXT))
        else:
            return model.parse_raw((RAW_TEXT)) if model else response.json()
    
    def delete(self, method: str, headers: Optional[dict] = None, json = None, data = None, model: Optional[Type] = None, is_list: bool = False, return_json: bool = False, return_raw_text: bool = False, **kwargs):
        headers = headers or self.headers
        if headers.get("User-Agent", None) is None:
            headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"})
        
        response = self.session.delete(self.API + method, headers=headers, json=json, data=data, **kwargs)
        
        self._check_response(response)
        RAW_TEXT = response.text
        
        if return_json:
            return response.json()
        elif return_raw_text:
            return RAW_TEXT
        elif is_list and model:
            return self.ParseListModels(model, (RAW_TEXT))
        else:
            return model.parse_raw((RAW_TEXT)) if model else response.json()
