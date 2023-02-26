from .model import Type
from datetime import datetime

from .LessonLog import LessonLogEntries
from .Lessons import Lesson
from .Subjects import Subject
from .Works import Work
from .Marks import Mark


class criteriabasedmark(Type):
    id: int
    id_str: str | None = None
    personid: int | None = None
    section: int | None = None
    value: int | None = None
    date: datetime | None = None


class WORKTYPE(Type):
    id: int
    schoolId: int | None = None
    abbreviation: str | None = None
    name: str | None = None
    isFinal: bool | None = None
    isImportant: bool | None = None
    kindId: int | None = None
    kind: str | None = None


class RecentMarks(Type):
    """[GET] /v2.0/persons/{person}/group/{group}/recentmarks\n~~~\nПоследние оценки/отметки посещаемости персоны по предмету указанному в параметре subject начиная с даты определенном в параметре fromDate и с ограничением на выводимое количество указанном в параметре limit\n~~~"""
    
    marks: list[Mark] = []
    criteriabasedmarks: list[criteriabasedmark] = []
    works: list[Work] = []
    subjects: list[Subject] = []
    workTypes: list[WORKTYPE] = []
    lessons: list[Lesson] = []
    lessonLogEntries: list[LessonLogEntries] = []