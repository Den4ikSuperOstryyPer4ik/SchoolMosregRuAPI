from typing import Optional
from .model import Type, TypeMobile

class TokenWithCode(Type):
    """[POST] /v2.0/authorizations \n~~~\nОбменять код доступа на токен\n~~~"""
    
    accessToken: str
    expiresIn: int
    expiresIn_str: str
    refreshToken: str
    scope: str
    user: int
    user_str: str


class EsiaRegion(Type):
    regionId: int
    esiaUrl: Optional[str] = None
    name: str
    logoUrl: Optional[str] = None

class EsiaRegions(TypeMobile):
    """[GET] /mobile/v6.0/authorizations/esia/regions\n~~~\nПолучить доступные Esia-Регионы\n~~~"""
    
    regions: list[EsiaRegion]


class Status(Type):
    type: Optional[str] = None
    description: Optional[str] = None


class EsiaInfoLoginResponse(Type):
    accessToken: Optional[str] = None
    userId: Optional[int] = None

class AuthorizationEsiaInfo(TypeMobile):
    status: Optional[Status] = None
    loginResponse: Optional[EsiaInfoLoginResponse] = None
