from typing import Optional

from .EduGroups import EduGroup
from .model import Type


class Context_Children(Type):
    personId: int
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    shortName: Optional[str] = None
    schoolIds: list[Optional[int]] = []
    groupIds: list[Optional[int]] = []


class Context_school(Type):
    id: int
    name: str
    type: str
    groupIds: list[int]
 

class Context(Type):
    """[GET] /v2.0/users/me/context | /v2.0/users/{userID}/context\n~~~\nПолучение контекстной информации по пользователю\n~~~\nПрава доступа: CommonInfo, FriendsAndRelatives, EducationalInfo\n~~~\n"""
    
    userId: Optional[int] = None
    avatarUrl: Optional[str] = None
    roles: list[Optional[str]] = []
    children: list[Optional[Context_Children]] = []
    schools: list[Optional[Context_school]] = []
    eduGroups: list[Optional[EduGroup]] = []
    splitId: Optional[str] = None
    personId: Optional[int] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    shortName: Optional[str] = None
    schoolIds: list[Optional[int]] = []
    groupIds: list[Optional[int]] = []