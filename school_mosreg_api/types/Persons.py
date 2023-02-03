from pydantic import BaseModel


class Person(BaseModel):
    """Персона."""
    
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str
    lastName: str
    middleName: str
    shortName: str
    sex: str