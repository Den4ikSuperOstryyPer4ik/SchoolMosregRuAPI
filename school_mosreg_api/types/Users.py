from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    """[GET/POST]\n~~~\n/v2.0/users/{user}\n~~~\n/v2.0/users/me\n~~~\n/v2.0/users/\n~~~\n/v2.0/users/many\n~~~\nПрофиль пользователя (Данный класс - 1 пользователь)\n~~~"""
    
    id: int
    id_str: str
    personId: int
    personId_str: str
    name: str = None
    email: str = None
    login: str = None
    fullName: str = None
    fullNameInverse: str = None
    firstName: str = None
    middleName: str = None
    lastName: str = None
    shortName: str = None
    locale: str = None
    timezone: str = None
    sex: str = None
    photoSmall: str = None
    photoMedium: str = None
    photoLarge: str = None
    birthday: datetime = None
    roles: list[str] = []
    phone: str = None
