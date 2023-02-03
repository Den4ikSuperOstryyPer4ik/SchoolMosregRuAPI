from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
    """[GET] /v2.0/tasks/{task}\n~~~\n/v2.0/tasks\n~~~\n/v2.0/lessons/{lesson}/tasks\n~~~\n/v2.0/works/{work}/tasks\n~~~\n/v2.0/persons/{person}/tasks\n~~~\n/v2.0/tasks/{personId}/undone\n~~~\nДомашнее задание (Данный класс - 1 ДЗ)\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    id: int
    id_str: str
    person: int
    person_str: str
    work: int
    work_str: str
    status: str
    targetDate: datetime
