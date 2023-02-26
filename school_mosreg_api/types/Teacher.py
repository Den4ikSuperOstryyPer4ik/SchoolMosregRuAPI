from datetime import datetime
from .model import Type

class _Student(Type):
    """[GET] /v2.0/teacher/{teacher}/students\n~~~\nСписок учеников для учителя который ведет уроки у этих учеников(они должны быть в расписании) от недели назад и на 30 дней вперед (Данный класс - 1 ученик)\n~~~"""
    
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str | None = None
    lastName: str | None = None
    middleName: str | None = None
    shortName: str | None = None
    sex: str | None = None


class TeacherStudent(Type):
    id: int
    id_str: str
    students: list[_Student]


class SchoolTeacher(Type):
    """[GET] /v2.0/schools/{school}/teachers\n~~~\nСписок преподавателей в выбранной образовательной организации (Данный класс - 1 учитель)\n~~~"""
    
    Id: int
    IdStr: str
    UserId: int
    UserIdStr: str
    FirstName: str
    LastName: str
    MiddleName: str
    ShortName: str
    Sex: str
    DateBirth: datetime
    Email: str
    Subjects: str
    HouseMaster: bool
    Education: str
    ScientificDegree: str
    StartDate: datetime
    PedagogicalActivityDate: datetime
    ManagingEmployee: bool
    NameManagingPosition: str
    TeachingStaff: bool
    NameTeacherPosition: str
    TrainingAndSupportStaff: bool
    ServicePersonnel: bool
    MedicalWorker: bool
    NameMedicalPosition: str
    ExternalPartTime: bool


class EduGroupTeacher(Type):
    """[GET] /v2.0/edu-groups/{group}/teachers\n~~~\nСписок учителей, которые ведут уроки в данной группе, учитываются уроки от недели назад и на 30 дней вперед (Данный класс - 1 учитель)\n~~~"""
    
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str | None = None
    lastName: str | None = None
    middleName: str | None = None
    shortName: str | None = None
    sex: str | None = None

