from datetime import datetime
from .model import Type

from .Works import Work
from .Subjects import Subject


class ScheduleDayLesson(Type):
    id: int
    title: str
    date: datetime
    number: int
    subjectId: int
    status: str
    resultPlaceId: int
    building: str
    place: str
    floor: str
    hours: str
    works: list[int]
    teachers: list[int]


class ScheduleDayMark(Type):
    id: int
    id_str: str
    type: str
    value: str
    textValue: str
    person: int
    person_str: str
    work: int
    work_str: str
    lesson: int
    lesson_str: str
    number: int
    date: datetime
    workType: int
    mood: str
    use_avg_calc: bool


class ScheduleDayWorkType(Type):
    id: int
    schoolId: int
    abbreviation: str
    name: str
    isFinal: bool
    isImportant: bool
    kindId: int
    kind: str


class ScheduleDayTeacherPerson(Type):
    id: int
    id_str: str
    userId: int
    userId_str: str
    firstName: str
    lastName: str
    middleName: str
    shortName: str
    sex: str


class ScheduleDayTeacher(Type):
    person: ScheduleDayTeacherPerson
    role: str


class ScheduleDayLessonLogEntries(Type):
    person: int
    lesson: int
    person_str: str
    lesson_str: str
    comment: str
    status: str
    createdDate: datetime


class ScheduleDay(Type):
    date: datetime
    lessons: list[ScheduleDayLesson]
    marks: list[ScheduleDayMark]
    works: list[Work]
    homeworks: list[Work]
    subjects: list[Subject]
    workTypes: list[ScheduleDayWorkType]
    lessonLogEntries: list[ScheduleDayLessonLogEntries]
    teachers: list[ScheduleDayTeacher]
    nextDate: datetime


class Schedule(Type):
    """[GET] /v2.0/persons/{person}/groups/{group}/schedules\n~~~\nРасписание ученика\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    days: list[ScheduleDay]