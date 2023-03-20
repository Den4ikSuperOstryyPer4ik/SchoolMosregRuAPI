from .model import Type
from typing import Optional

from .Works import Work
from .Subjects import Subject
from .Users import User
import datetime

class LESSON(Type):
    id: int
    id_str: Optional[str] = None
    title: Optional[str] = None
    date: Optional[datetime.datetime] = None
    number: int | str |  Optional[None] = None
    subject: Optional[Subject] = None
    group: Optional[int] = None
    status: Optional[str] = None
    resultPlaceId: Optional[int] = None
    works: list[Work] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

class Lesson(Type):
    id: int
    title: Optional[str] = None
    date: Optional[datetime.datetime] = None
    number: Optional[int] = None
    subjectId: int
    status: Optional[str] = None
    resultPlaceId: Optional[int] = None
    building: Optional[str] = None
    place: Optional[str] = None
    floor: Optional[str] = None
    hours: Optional[str] = None
    works: list[int] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

class HomeWorkFile(Type):
    id: int
    id_str: str
    name: Optional[str] = None
    typeGroup: Optional[str] = None
    type: str
    pageUrl: Optional[str] = None
    downloadUrl: str
    user: User
    size: Optional[int] = None
    vote: Optional[int] = None
    uploadedDate: Optional[datetime.datetime] = None
    storageType: Optional[str] = None

class Teacher(Type):
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    shortName: Optional[str] = None
    sex: Optional[str] = None

class HomeWork(Type):
    """[GET] /v2.0/users/me/school/{school}/homeworks\n~~~\n/v2.0/users/me/school/homeworks\n~~~\n/v2.0/persons/{person}/school/{school}/homeworks\n~~~\nДомашние задания\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    works: list[Work] = []
    subjects: list[Subject] = []
    lessons: list[Lesson] = []
    files: list[HomeWorkFile] = []
    teachers: list[Teacher] = []
