from .model import Type

class Person(Type):
    """Персона."""
    
    id: int | None = None
    id_str: str | None = None
    userId: int | None = None
    userId_str: str | None = None
    firstName: str | None = None
    lastName: str | None = None
    middleName: str | None = None
    shortName: str | None = None
    sex: str | None = None
