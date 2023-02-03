from pydantic import BaseModel


class SchoolMemberships_school_school(BaseModel):
    fullName: str
    avatarSmall: str
    city: str
    municipality: str
    regionid: int
    markType: str
    timeZone: int
    uses_avg: bool
    uses_weighted_avg: bool
    id: int
    id_str: str
    name: str
    educationType: str
    tsoCityId: int
    tsoRegionTreePath: str


class SchoolMemberships_school_subject(BaseModel):
    id: int
    id_str: str
    name: str
    knowledgeArea: str
    fgosSubjectId: int


class SchoolMemberships_school_eduGroupMemberships_(BaseModel):
    id: int
    id_str: str
    parentIds: list[int]
    parentIds_str: list[str]
    type: str
    name: str
    fullName: str
    parallel: int
    timetable: int
    timetable_str: str
    status: str
    studyyear: int
    educationType: str
    subjects: list[SchoolMemberships_school_subject]
    journaltype: str
        

class SchoolMemberships_school_eduGroupMemberships(BaseModel):
    eduGroup: SchoolMemberships_school_eduGroupMemberships_


class SchoolMemberships_school(BaseModel):
    school: SchoolMemberships_school_school
    roles: list[str]
    editorRoles: list[str]
    eduGroupMemberships: list[SchoolMemberships_school_eduGroupMemberships]
    roles: list[str]
    subjects: list[SchoolMemberships_school_subject]


class SchoolMemberships(BaseModel):
    """[GET]\n~~~\n/v2.0/users/{user}/school-memberships\n~~~\n/v2.0/users/{user}/education\n~~~\n/v2.0/users/me/school-memberships\n~~~\n/v2.0/persons/{person}/school-memberships\n~~~\nСписок участий в школах для того или иного пользователя\n~~~\nПрава доступа: EducationalInfo\n~~~\n"""
    
    person: int | None = None
    person_str: str | None = None
    schools: list[SchoolMemberships_school]