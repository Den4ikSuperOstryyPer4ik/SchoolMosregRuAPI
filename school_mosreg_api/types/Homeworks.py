from pydantic import BaseModel


from .Works import Work
from .Subjects import Subject
from .Users import User
import datetime

class LESSON(BaseModel):
    id: int
    id_str: str = None
    title: str = None
    date: datetime.datetime = None
    number: int | str |  None = None
    subject: Subject = None
    group: int = None
    status: str = None
    resultPlaceId: int = None
    works: list[Work] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

class Lesson(BaseModel):
    id: int
    title: str = None
    date: datetime.datetime = None
    number: int = None
    subjectId: int
    status: str = None
    resultPlaceId: int = None
    building: str = None
    place: str = None
    floor: str = None
    hours: str = None
    works: list[int] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

class HomeWorkFile(BaseModel):
    id: int
    id_str: str
    name: str = None
    typeGroup: str = None
    type: str
    pageUrl: str = None
    downloadUrl: str
    user: User
    size: int = None
    vote: int = None
    uploadedDate: datetime.datetime = None
    storageType: str = None

class Teacher(BaseModel):
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str = None
    lastName: str = None
    middleName: str = None
    shortName: str = None
    sex: str = None

class HomeWork(BaseModel):
    """[GET] /v2.0/users/me/school/{school}/homeworks\n~~~\n/v2.0/users/me/school/homeworks\n~~~\n/v2.0/persons/{person}/school/{school}/homeworks\n~~~\nДомашние задания\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    works: list[Work] = []
    subjects: list[Subject] = []
    lessons: list[Lesson] = []
    files: list[HomeWorkFile] = []
    teachers: list[Teacher] = []
