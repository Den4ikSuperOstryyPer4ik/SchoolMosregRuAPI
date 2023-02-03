from datetime import datetime
from pydantic import BaseModel


class ITEM(BaseModel):
    Id: int
    Start: datetime
    Finish: datetime
    Name: str
    Type: str
    DaysOfWeek: list[str]
    LessonNumber: int


class TimeTable(BaseModel):
    """[GET] /v2.0/schools/{school}/timetables\n~~~\n/v2.0/edu-groups/{eduGroup}/timetables\n~~~\nПолучение расписания школы/учебной группы\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    Name: str
    Start: datetime
    FirstLessonNumber: int
    Items: list[ITEM]