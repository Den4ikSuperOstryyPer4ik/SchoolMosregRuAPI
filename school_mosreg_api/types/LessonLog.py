from datetime import datetime
from .model import Type

class LessonLogEntries(Type):
    """Отметка о посещаемости (Данный класс - 1 отметка)\n~~~"""
    
    person: int | None = None
    lesson: int | None = None
    person_str: str | None = None
    lesson_str: str | None = None
    comment: str | None = None
    status: str | None = None
    createdDate: datetime | None = None
