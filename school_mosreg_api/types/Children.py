from pydantic import BaseModel


class Children(BaseModel):
    """[GET] /v2.0/user/{userID}/children \n~~~\nПолучение списка детей по идентификатору родительского пользователя\n~~~\nПрава доступа: EducationalInfo\n~~~\n"""
    
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str
    lastName: str
    middleName: str
    shortName: str
    sex: str