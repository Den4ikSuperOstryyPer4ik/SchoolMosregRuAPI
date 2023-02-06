from .model import Type

class WeightedAverageMarks_SubjectMark_Mark(Type):
    person: int
    value: int

class WeightedAverageMarks_SubjectMarks(Type):
    subject: int
    subject_str: str
    marks: list[WeightedAverageMarks_SubjectMark_Mark]

class WeightedAverageMarks(Type):
    """[GET] /v2.0/edu-groups/{group}/wa-marks/{from}/{to}\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    subjectMarks: list[WeightedAverageMarks_SubjectMarks]
