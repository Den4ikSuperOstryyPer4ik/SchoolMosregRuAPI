from datetime import datetime
from .model import Type, TypeMobile
from typing import Union, Optional, Any, List
from pydantic import Field


class DayHomeworksProgres(Type):
    total_lessons_with_homeworks_count: int = Field(
        None, alias='totalLessonsWithHomeworksCount'
    )
    completed_lessons_with_homeworks_count: int = Field(
        None, alias='completedLessonsWithHomeworksCount'
    )


class Subject(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class HomeworkItem(Type):
    work_is_attach_required: bool = Field(None, alias='workIsAttachRequired')
    attachments: List
    text: str
    is_completed: bool = Field(None, alias='isCompleted')


class Mark(Type):
    id: int
    value: str
    mood: str


class WorkMark(Type):
    work_id: int = Field(None, alias='workId')
    marks: List[Mark]


class Teacher(Type):
    person_id: int = Field(None, alias='personId')
    first_name: str = Field(None, alias='firstName')
    middle_name: str = Field(None, alias='middleName')
    last_name: str = Field(None, alias='lastName')
    avatar_url: Optional[str] = Field(None, alias='avatarUrl')


class Group(Type):
    id: int
    parent_id: Optional[int] = Field(None, alias='parentId')
    name: str
    parent_name: Optional[str] = Field(None, alias='parentName')


class Lesson(Type):
    id: int
    number: int
    place: str
    start_date_time: str = Field(None, alias='startDateTime')
    end_date_time: str = Field(None, alias='endDateTime')
    is_canceled: bool = Field(None, alias='isCanceled')
    theme: str
    subject: Subject
    important_works: List[str] = Field(None, alias='importantWorks')
    homework: Optional[HomeworkItem]
    has_attachment: bool = Field(None, alias='hasAttachment')
    work_marks: List[WorkMark] = Field(None, alias='workMarks')
    is_empty: Any = Field(None, alias='isEmpty')
    comment: Any
    teacher: Teacher
    group: Group


class Day(Type):
    date: str
    has_important_work: bool = Field(None, alias='hasImportantWork')
    day_homeworks_progress: Optional[DayHomeworksProgres] = Field(
        None, alias='dayHomeworksProgress'
    )
    lessons: List[Lesson]
    messenger_entry_point: Any = Field(None, alias='messengerEntryPoint')


class Week(Type):
    id: str
    homeworks_count: int = Field(None, alias='homeworksCount')
    first_week_day_date: str = Field(None, alias='firstWeekDayDate')
    last_week_day_date: str = Field(None, alias='lastWeekDayDate')
    days: List[Day]


class DayBookResponse(TypeMobile):
    weeks: Optional[List[Week]] = None
