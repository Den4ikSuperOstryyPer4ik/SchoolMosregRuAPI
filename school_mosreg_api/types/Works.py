from pydantic import BaseModel

from datetime import datetime

class Work_Task(BaseModel):
    id: int
    id_str: str
    person: int
    person_str: str
    work: int
    work_str: str
    status: str = None
    targetDate: datetime


class Work(BaseModel):
    """[GET/POST/DELETE/PUT]\n~~~\n/v2.0/works\n~~~\n/v2.0/lessons/{lesson}/works\n~~~\n/v2.0/works/{work}\n~~~\n/v2.0/works/many\n~~~\nПолучение списка всех типов работ школы (Данный класс - 1 тип работы)\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    id: int
    id_str: str
    type: str
    workType: int
    markType: str
    markCount: int
    lesson: int
    lesson_str: str
    displayInJournal: bool
    status: str
    eduGroup: int
    eduGroup_str: str
    tasks: list[Work_Task] | list = []
    text: str | bytes
    periodNumber: int
    periodType: str
    subjectId: int
    isImportant: bool
    targetDate: datetime
    sentDate: datetime = None
    createdBy: int
    files: list[int] = []
    oneDriveLinks: list[int] = []


class EditStatusHomeWork(BaseModel):
    """[POST]\n~~~\n/v2.0/works/{work}/persons/{person}/status\n~~~\nИзменить статус выполнения домашней работы учащимся.\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    id: int
    id_str: str
    person: int
    person_str: str
    work: int
    work_str: str
    status: str
    targetDate: datetime
  