from pydantic import BaseModel

class WeightedAverageMarks_SubjectMark_Mark(BaseModel):
    person: int
    value: int

class WeightedAverageMarks_SubjectMarks(BaseModel):
    subject: int
    subject_str: str
    marks: list[WeightedAverageMarks_SubjectMark_Mark]

class WeightedAverageMarks(BaseModel):
    """[GET] /v2.0/edu-groups/{group}/wa-marks/{from}/{to}\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    subjectMarks: list[WeightedAverageMarks_SubjectMarks]
