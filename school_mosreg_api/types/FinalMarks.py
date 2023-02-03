from pydantic import BaseModel

from .Marks import Mark
from .Works import Work
from .Subjects import Subject


class FinalMarkWorkType(BaseModel):
    id: int
    schoolId: int
    abbreviation: str
    name: str
    isFinal: bool
    isImportant: bool
    kindId: int
    kind: str
    

class EduGroupFinalMark(BaseModel):
    """[GET] /v2.0/edu-groups/{group}/final-marks\n~~~\nИтоговые Оценки персоны в учебной группе\n~~~"""
    
    marks: list[Mark]
    works: list[Work]
    subjects: list[Subject]
    workTypes: list[FinalMarkWorkType]
        