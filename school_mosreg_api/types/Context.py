from pydantic import BaseModel

from .EduGroups import EduGroup


class Context_Children(BaseModel):
    personId: int
    firstName: str
    lastName: str
    middleName: str
    shortName: str
    schoolIds: list[int]
    groupIds: list[int]


class Context_school(BaseModel):
    id: int
    name: str
    type: str
    groupIds: list[int]
 

class Context(BaseModel):
    """[GET] /v2.0/users/me/context | /v2.0/users/{userID}/context\n~~~\nПолучение контекстной информации по пользователю\n~~~\nПрава доступа: CommonInfo, FriendsAndRelatives, EducationalInfo\n~~~\n"""
    
    userId: int
    avatarUrl: str
    roles: list[str]
    children: list[Context_Children]
    schools: list[Context_school]
    eduGroups: list[EduGroup]
    splitId: str
    personId: int
    firstName: str
    lastName: str
    middleName: str
    shortName: str
    schoolIds: list[int]
    groupIds: list[int]