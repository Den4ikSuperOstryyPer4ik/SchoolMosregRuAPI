from .model import Type

from datetime import datetime
from .Works import Work


class ImportantWork(Type):
    work: Work
    subjectName: str
    workTypeName: str


class Mark_(Type):
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


class MarksList(Type):
    marks: list[Mark_]
    

class Mark(Type):
    mark: Mark_


class Lesson(Type):
    id: int
    date: datetime


class MarksCard(Type):
    marks: list[Mark]
    lesson: Lesson
    isImportant: bool
    subjectName: str
    subjectId: int
    workTypeName: str


class Summary(Type):
    importantWorks: list[ImportantWork] = []
    marksCards: list[MarksCard] = []
    dayEmotion: str
    feedMode: str


class NextDayHomeworks(Type):
    work: Work
    subjectName: str
    workTypeName: str


class ImportantWorkType(Type):
    id: int
    name: str


class NextDaySchedule(Type):
    lessonId: int
    lessonStatus: str
    number: int
    subjectName: str
    importantWorkTypes: list[ImportantWorkType]


class TodayHomework(Type):
    work: Work
    subjectName: str
    workTypeName: str


class TodaySchedule(Type):
    lessonId: int
    lessonStatus: str
    number: int
    subjectName: str
    importantWorkTypes: list[ImportantWorkType]


class LessonLogEntry(Type):
    person: int
    lesson: int
    person_str: str
    lesson_str: str
    comment: str
    status: str
    createdDate: datetime


class LogEntries(Type):
    lessonLogEntry: LessonLogEntry
    subjectName: str
    lessonTitle: str


class FeedDay(Type):
    """..."""
    date: datetime
    nextWorkingDayDate: datetime | None = None
    summary: Summary | None = None
    nextDayHomeworks: list[NextDayHomeworks] = []
    nextDaySchedule: list[NextDaySchedule] = []
    todayHomeworks: list[TodayHomework] = []
    todaySchedule: list[TodaySchedule] = []
    logEntries: list[LogEntries] = []



class UserFeed(Type):
    """[GET] /v2.0/users/me/feed\n~~~\nЛента пользователя\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    days: list[FeedDay] | None = None
