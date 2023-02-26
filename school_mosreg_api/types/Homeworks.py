from .model import Type


from .Works import Work
from .Subjects import Subject
from .Users import User
import datetime

class LESSON(Type):
    id: int
    id_str: str | None = None
    title: str | None = None
    date: datetime.datetime | None = None
    number: int | str |  None | None = None
    subject: Subject | None = None
    group: int | None = None
    status: str | None = None
    resultPlaceId: int | None = None
    works: list[Work] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

class Lesson(Type):
    id: int
    title: str | None = None
    date: datetime.datetime | None = None
    number: int | None = None
    subjectId: int
    status: str | None = None
    resultPlaceId: int | None = None
    building: str | None = None
    place: str | None = None
    floor: str | None = None
    hours: str | None = None
    works: list[int] = []
    teachers: list[int] = []
    teachers_str: list[str] = []

class HomeWorkFile(Type):
    id: int
    id_str: str
    name: str | None = None
    typeGroup: str | None = None
    type: str
    pageUrl: str | None = None
    downloadUrl: str
    user: User
    size: int | None = None
    vote: int | None = None
    uploadedDate: datetime.datetime | None = None
    storageType: str | None = None

class Teacher(Type):
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str | None = None
    lastName: str | None = None
    middleName: str | None = None
    shortName: str | None = None
    sex: str | None = None

class HomeWork(Type):
    """[GET] /v2.0/users/me/school/{school}/homeworks\n~~~\n/v2.0/users/me/school/homeworks\n~~~\n/v2.0/persons/{person}/school/{school}/homeworks\n~~~\nДомашние задания\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    works: list[Work] = []
    subjects: list[Subject] = []
    lessons: list[Lesson] = []
    files: list[HomeWorkFile] = []
    teachers: list[Teacher] = []
