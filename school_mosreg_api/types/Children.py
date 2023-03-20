from .model import Type
from typing import Optional

class Children(Type):
    """[GET] /v2.0/user/{userID}/children \n~~~\nПолучение списка детей по идентификатору родительского пользователя\n~~~\nПрава доступа: EducationalInfo\n~~~\n"""
    
    id: int
    id_str: str
    userId: Optional[int] = None
    userId_str: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    shortName: Optional[str] = None
    sex: Optional[str] = None