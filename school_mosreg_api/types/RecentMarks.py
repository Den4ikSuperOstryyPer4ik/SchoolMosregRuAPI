from pydantic import BaseModel
from datetime import datetime

from .LessonLog import LessonLogEntries
from .Lessons import Lesson
from .Subjects import Subject
from .Works import Work
from .Marks import Mark


class criteriabasedmark(BaseModel):
    id: int
    id_str: str = None
    personid: int = None
    section: int = None
    value: int = None
    date: datetime = None


class WORKTYPE(BaseModel):
    id: int
    schoolId: int = None
    abbreviation: str = None
    name: str = None
    isFinal: bool = None
    isImportant: bool = None
    kindId: int = None
    kind: str = None


class RecentMarks(BaseModel):
    """[GET] /v2.0/persons/{person}/group/{group}/recentmarks\n~~~\nПоследние оценки/отметки посещаемости персоны по предмету указанному в параметре subject начиная с даты определенном в параметре fromDate и с ограничением на выводимое количество указанном в параметре limit\n~~~"""
    
    marks: list[Mark] = []
    criteriabasedmarks: list[criteriabasedmark] = []
    works: list[Work] = []
    subjects: list[Subject] = []
    workTypes: list[WORKTYPE] = []
    lessons: list[Lesson] = []
    lessonLogEntries: list[LessonLogEntries] = []