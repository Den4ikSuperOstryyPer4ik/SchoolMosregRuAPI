from .model import Type, TypeMobile

from .Marks import Mark
from .Works import Work
from .Subjects import Subject

from typing import Optional


class FinalMarkWorkType(Type):
    id: int
    schoolId: int
    abbreviation: str
    name: str
    isFinal: bool
    isImportant: bool
    kindId: int
    kind: str
    

class EduGroupFinalMark(Type):
    """[GET] /v2.0/edu-groups/{group}/final-marks\n~~~\nИтоговые Оценки персоны в учебной группе\n~~~"""
    
    marks: list[Mark]
    works: list[Work]
    subjects: list[Subject]
    workTypes: list[FinalMarkWorkType]


class FinalMarkSubject(Type):
    f6966id: Optional[int] = None
    name: Optional[str] = None
    knowledgeArea: Optional[str] = None
    subjectMood: Optional[str] = None


class MarkMobile(Type):
    f6971id: Optional[int] = None
    mood: Optional[str] = None
    value: Optional[str] = None


class PeriodMobile(Type):
    f6972id: Optional[int] = None
    number: Optional[int] = None
    type: Optional[str] = None
    dateStart: Optional[int] = None
    dateFinish: Optional[int] = None
    studyYear: Optional[int] = None
    current: Optional[bool] = None
    

class PeriodMark(Type):
    marks: list[Optional[MarkMobile]]
    period: Optional[PeriodMobile] = None


class PeriodFinalMark(Type):
    workType: Optional[str] = None
    workTypeName: Optional[str] = None
    marks: list[Optional[MarkMobile]]


class FinalMark(Type):
    subject: Optional[FinalMarkSubject] = None
    knowledgeArea: Optional[str] = None
    periodMarks: list[Optional[PeriodMark]] = []
    periodFinalMarks: list[Optional[PeriodFinalMark]] = []


class FinalMarksResponse(TypeMobile):
    finalMarks: list[Optional[FinalMark]]
