from datetime import datetime
from pydantic import BaseModel

class ReportingPeriod(BaseModel):
    """[GET] /v2.0/edu-groups/{eduGroup}/reporting-periods\n~~~\nСписок отчётных периодов для класса или учебной группы (Данный класс - 1 отчетный период)\n~~~"""
    
    id: int
    id_str: str
    start: datetime
    finish: datetime
    number: int
    type: str
    name: str
    year: int


class Holidays(BaseModel):
    id: int
    reportingPeriodGroupId: int
    dateStart: datetime
    dateFinish: datetime
    name: str
    description: str


class ReportingPeriodEduGroup(BaseModel):
    """[GET] /v2.0/edu-groups/{eduGroup}/reporting-periods-group\n~~~\nГруппа отчетных периодов для класса или учебной группы (Данный класс - 1 отчетный период)\n~~~"""
    
    id: int
    reportingPeriods: list[ReportingPeriod]
    holidays: list[Holidays]
