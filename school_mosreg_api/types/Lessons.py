from datetime import datetime
from pydantic import BaseModel

from .Subjects import Subject
from .Works import Work


class Lesson(BaseModel):
    """Урок"""
    
    id: int
    id_str: str = None
    title: str = None
    date: datetime = None
    number: int = None
    subject: Subject
    group: int
    status: str = None
    resultPlaceId: int = None
    works: list[Work] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

