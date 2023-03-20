from datetime import datetime
from .model import Type

from .Subjects import Subject
from .Works import Work
from typing import Optional

class Lesson(Type):
    """Урок"""
    
    id: int
    id_str: Optional[str] = None
    title: Optional[str] = None
    date: Optional[datetime] = None
    number: Optional[int] = None
    subject: Subject
    group: int
    status: Optional[str] = None
    resultPlaceId: Optional[int] = None
    works: list[Work] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

