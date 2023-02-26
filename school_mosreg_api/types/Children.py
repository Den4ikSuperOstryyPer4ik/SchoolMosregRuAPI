from .model import Type

class Children(Type):
    """[GET] /v2.0/user/{userID}/children \n~~~\nПолучение списка детей по идентификатору родительского пользователя\n~~~\nПрава доступа: EducationalInfo\n~~~\n"""
    
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str | None = None
    lastName: str | None = None
    middleName: str | None = None
    shortName: str | None = None
    sex: str | None = None