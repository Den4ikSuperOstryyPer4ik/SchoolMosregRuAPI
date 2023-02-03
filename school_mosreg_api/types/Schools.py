from pydantic import BaseModel


class School(BaseModel):
    """[GET] /v2.0/schools/{school}\n~~~\nПрофиль школы\n~~~"""
    
    fullName: str = None
    avatarSmall: str = None
    city: str = None
    municipality: str = None
    regionid: int = None
    markType: str = None
    timeZone: int = None
    uses_avg: bool = None
    uses_weighted_avg: bool = None
    id: int = None
    id_str: str = None
    name: str
    educationType: str
    tsoCityId: int = None
    tsoRegionTreePath: str = None

class PersonSchool(BaseModel):
    """[GET] /v2.0/schools/person-schools\n~~~\nСписок образовательных организаций пользователя\n~~~"""
    
    id: int
    id_str: str
    name: str
    educationType: str
    tsoCityId: int
    tsoRegionTreePath: str

class SchoolsCities(BaseModel):
    """[GET] /v2.0/schools/cities\n~~~\nСписок населенных пунктов, образовательные организации которых включены в Систему\n~~~"""
    
    id: int
    id_str: str
    name: str
    regionId: int
    regionId_str: str