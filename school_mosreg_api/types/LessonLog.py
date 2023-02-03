from datetime import datetime
from pydantic import BaseModel

class LessonLogEntries(BaseModel):
    """Отметка о посещаемости (Данный класс - 1 отметка)\n~~~"""
    
    person: int
    lesson: int
    person_str: str
    lesson_str: str
    comment: str
    status: str
    createdDate: datetime
