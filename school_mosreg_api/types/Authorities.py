from pydantic import BaseModel

class Organization(BaseModel):
    """[GET] /v2.0/users/me/organizations/{organizationId}\n~~~\nДанные указанной организации пользователя\n~~~\nПрава доступа: EducationalInfo\n~~~\n"""
    
    OrganizationId: int
    OrganizationType: int
    RegionId: int
    DistrictId: int
    CityId: int