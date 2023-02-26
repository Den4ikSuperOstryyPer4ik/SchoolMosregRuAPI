from .model import Type

class Person(Type):
    """Персона."""
    
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str | None = None
    lastName: str | None = None
    middleName: str | None = None
    shortName: str | None = None
    sex: str
