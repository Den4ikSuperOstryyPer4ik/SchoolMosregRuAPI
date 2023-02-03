from pydantic import BaseModel
from datetime import datetime
from .Works import Work


class ImportantWork(BaseModel):
    work: Work
    subjectName: str
    workTypeName: str


class Mark_(BaseModel):
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


class MarksList(BaseModel):
    marks: list[Mark_]
    

class Mark(BaseModel):
    mark: Mark_


class Lesson(BaseModel):
    id: int
    date: datetime


class MarksCard(BaseModel):
    marks: list[Mark]
    lesson: Lesson
    isImportant: bool
    subjectName: str
    subjectId: int
    workTypeName: str


class Summary(BaseModel):
    importantWorks: list[ImportantWork] = []
    marksCards: list[MarksCard] = []
    dayEmotion: str
    feedMode: str


class NextDayHomeworks(BaseModel):
    work: Work
    subjectName: str
    workTypeName: str


class ImportantWorkType(BaseModel):
    id: int
    name: str


class NextDaySchedule(BaseModel):
    lessonId: int
    lessonStatus: str
    number: int
    subjectName: str
    importantWorkTypes: list[ImportantWorkType]


class TodayHomework(BaseModel):
    work: Work
    subjectName: str
    workTypeName: str


class TodaySchedule(BaseModel):
    lessonId: int
    lessonStatus: str
    number: int
    subjectName: str
    importantWorkTypes: list[ImportantWorkType]


class LessonLogEntry(BaseModel):
    person: int
    lesson: int
    person_str: str
    lesson_str: str
    comment: str
    status: str
    createdDate: datetime


class LogEntries(BaseModel):
    lessonLogEntry: LessonLogEntry
    subjectName: str
    lessonTitle: str


class FeedDay(BaseModel):
    """..."""
    date: datetime
    nextWorkingDayDate: datetime | None = None
    summary: Summary | None = None
    nextDayHomeworks: list[NextDayHomeworks] = []
    nextDaySchedule: list[NextDaySchedule] = []
    todayHomeworks: list[TodayHomework] = []
    todaySchedule: list[TodaySchedule] = []
    logEntries: list[LogEntries] = []



class UserFeed(BaseModel):
    """[GET] /v2.0/users/me/feed\n~~~\nЛента пользователя\n~~~\nПрава доступа: EducationalInfo\n~~~"""
    
    days: list[FeedDay] | None = None
