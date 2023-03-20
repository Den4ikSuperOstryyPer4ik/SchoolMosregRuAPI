from typing import Optional
from .model import Type
from .Subjects import Subject

class EduGroup(Type):
    """[GET]\n~~~\n/v2.0/edu-groups/{eduGroup}\n~~~\n/v2.0/edu-groups\n~~~\n/v2.0/schools/{school}/edu-groups\n~~~\n/v2.0/persons/{person}/edu-groups\n~~~\n/v2.0/persons/{person}/edu-groups/all\n~~~\n/v2.0/persons/{person}/schools/{school}/edu-groups\n~~~\n/v2.0/edu-groups/{groupId}/parallel\n~~~\nКласс или учебная группа\n~~~"""
    
    id: int
    id_str: str
    parentIds: list[Optional[int]] = []
    parentIds_str: list[Optional[str]] = []
    type: Optional[str] = None
    name: str
    fullName: Optional[str] = None
    parallel: Optional[int] = None
    timetable: Optional[int] = None
    timetable_str: Optional[str] = None
    status: Optional[str] = None
    studyyear: Optional[int] = None
    educationType: Optional[str] = None
    subjects: Optional[list[Optional[Subject]]] = []
    journaltype: Optional[str] = None
