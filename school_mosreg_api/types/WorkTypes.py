from .model import Type

class WorkType(Type):
    """[GET] /v2.0/work-types/{school}\n~~~\nПолучение списка всех типов работ школы (Данный класс - 1 тип работы)\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    id: int
    id_str: str
    schoolId: int | None = None
    kindId: int | None = None
    kind: str | None = None
    title: str
    abbr: str | None = None
    weight: int = 0
