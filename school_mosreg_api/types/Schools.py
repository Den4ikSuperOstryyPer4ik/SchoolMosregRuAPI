from .model import Type


class School(Type):
    """[GET] /v2.0/schools/{school}\n~~~\nПрофиль школы\n~~~"""
    
    fullName: str | None = None
    avatarSmall: str | None = None
    city: str | None = None
    municipality: str | None = None
    regionid: int | None = None
    markType: str | None = None
    timeZone: int | None = None
    uses_avg: bool | None = None
    uses_weighted_avg: bool | None = None
    id: int | None = None
    id_str: str | None = None
    name: str
    educationType: str
    tsoCityId: int | None = None
    tsoRegionTreePath: str | None = None

class PersonSchool(Type):
    """[GET] /v2.0/schools/person-schools\n~~~\nСписок образовательных организаций пользователя\n~~~"""
    
    id: int
    id_str: str
    name: str
    educationType: str
    tsoCityId: int
    tsoRegionTreePath: str

class SchoolsCities(Type):
    """[GET] /v2.0/schools/cities\n~~~\nСписок населенных пунктов, образовательные организации которых включены в Систему\n~~~"""
    
    id: int
    id_str: str
    name: str
    regionId: int
    regionId_str: str