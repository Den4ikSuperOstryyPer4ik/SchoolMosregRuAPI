from .model import Type
from .Subjects import Subject

class EduGroup(Type):
    """[GET]\n~~~\n/v2.0/edu-groups/{eduGroup}\n~~~\n/v2.0/edu-groups\n~~~\n/v2.0/schools/{school}/edu-groups\n~~~\n/v2.0/persons/{person}/edu-groups\n~~~\n/v2.0/persons/{person}/edu-groups/all\n~~~\n/v2.0/persons/{person}/schools/{school}/edu-groups\n~~~\n/v2.0/edu-groups/{groupId}/parallel\n~~~\nКласс или учебная группа\n~~~"""
    
    id: int
    id_str: str
    parentIds: list[int] = []
    parentIds_str: list[str] = []
    type: str
    name: str
    fullName: str | None = None
    parallel: int | None = None
    timetable: int | None = None
    timetable_str: str | None = None
    status: str | None = None
    studyyear: int | None = None
    educationType: str | None = None
    subjects: list[Subject] | None = []
    journaltype: str | None = None
