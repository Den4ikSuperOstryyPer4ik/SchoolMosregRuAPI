from .model import Type


class UserRelatives_person(Type):
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str
    lastName: str
    middleName: str
    shortName: str
    sex: str


class UserRelatives(Type):
    """[GET]\n~~~\n/v2.0/users/{user}/relatives\n~~~\n/v2.0/users/me/relatives\n~~~\n/v2.0/users/me/childrenrelatives\n~~~\nПолучение всех родственных связей (детей) произвольного пользователя.\n~~~"""
    
    type: str = None
    person: UserRelatives_person
    relatives: "list[UserRelatives]" = None
