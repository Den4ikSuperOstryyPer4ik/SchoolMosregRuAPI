from datetime import datetime
from .model import Type
from typing import Optional

class LessonLogEntries(Type):
    """Отметка о посещаемости (Данный класс - 1 отметка)\n~~~"""
    
    person: Optional[int] = None
    lesson: Optional[int] = None
    person_str: Optional[str] = None
    lesson_str: Optional[str] = None
    comment: Optional[str] = None
    status: Optional[str] = None
    createdDate: Optional[datetime] = None
