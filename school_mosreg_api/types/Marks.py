from datetime import datetime
from .model import Type

class Mark(Type):
    """Оценка"""
    
    
    id: int
    id_str: str | None = None
    type: str | None = None
    value: str
    textValue: str | None = None
    person: int | None = None
    person_str: str | None = None
    work: int
    work_str: str | None = None
    lesson: int | None = None
    lesson_str: str | None = None
    number: int | None = None
    date: datetime | None = None
    workType: int | None = None
    mood: str | None = None
    use_avg_calc: bool | None
