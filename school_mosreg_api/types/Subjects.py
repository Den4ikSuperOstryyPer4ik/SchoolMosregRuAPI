from pydantic import BaseModel

class Subject(BaseModel):
    """[GET] /v2.0/edu-groups/{eduGroup}/subjects\n~~~\n/v2.0/schools/{school}/subjects\n~~~\nСписок предметов, преподаваемых в классе в текущем отчётном периоде или преподаваемых в образовательной организации в текущем учебном году\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    id: int
    id_str: str = None
    name: str
    knowledgeArea: str = None
    fgosSubjectId: int = None
