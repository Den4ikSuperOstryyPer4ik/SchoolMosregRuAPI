from pydantic import BaseModel

class WorkType(BaseModel):
    """[GET] /v2.0/work-types/{school}\n~~~\nПолучение списка всех типов работ школы (Данный класс - 1 тип работы)\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    id: int
    id_str: str
    schoolId: int = None
    kindId: int = None
    kind: str = None
    title: str
    abbr: str = None
    weight: int = 0
