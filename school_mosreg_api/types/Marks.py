from datetime import datetime
from .model import Type

class Mark(Type):
    """Оценка"""
    
    
    id: int
    id_str: str
    type: str
    value: str
    textValue: str
    person: int
    person_str: str
    work: int
    work_str: str
    lesson: int
    lesson_str: str
    number: int
    date: datetime
    workType: int
    mood: str
    use_avg_calc: bool
