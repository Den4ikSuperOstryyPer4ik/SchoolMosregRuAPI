from datetime import datetime
from .model import Type

from .Subjects import Subject
from .Works import Work


class Lesson(Type):
    """Урок"""
    
    id: int
    id_str: str | None = None
    title: str | None = None
    date: datetime | None = None
    number: int | None = None
    subject: Subject
    group: int
    status: str | None = None
    resultPlaceId: int | None = None
    works: list[Work] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

