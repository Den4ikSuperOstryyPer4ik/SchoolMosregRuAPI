from .model import Type

from datetime import datetime

class User(Type):
    """[GET/POST]\n~~~\n/v2.0/users/{user}\n~~~\n/v2.0/users/me\n~~~\n/v2.0/users/\n~~~\n/v2.0/users/many\n~~~\nПрофиль пользователя (Данный класс - 1 пользователь)\n~~~"""
    
    id: int
    id_str: str
    personId: int
    personId_str: str
    name: str | None = None
    email: str | None = None
    login: str | None = None
    fullName: str | None = None
    fullNameInverse: str | None = None
    firstName: str | None = None
    middleName: str | None = None
    lastName: str | None = None
    shortName: str | None = None
    locale: str | None = None
    timezone: str | None = None
    sex: str | None = None
    photoSmall: str | None = None
    photoMedium: str | None = None
    photoLarge: str | None = None
    birthday: datetime | None = None
    roles: list[str] = []
    phone: str | None = None
