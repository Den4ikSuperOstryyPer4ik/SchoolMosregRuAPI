from .model import Type, TypeMobile
from typing import Union, Optional, Any, List
from pydantic import Field


class Subject(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class Hours(Type):
    start_hour: str = Field(None, alias='startHour')
    start_minute: str = Field(None, alias='startMinute')
    end_hour: str = Field(None, alias='endHour')
    end_minute: str = Field(None, alias='endMinute')


class Teacher(Type):
    first_name: str = Field(None, alias='firstName')
    middle_name: str = Field(None, alias='middleName')
    last_name: str = Field(None, alias='lastName')
    avatar_url: Any = Field(None, alias='avatarUrl')
    role: str
    jid: str


class AverageMarks(Type):
    average_mark: str = Field(None, alias='averageMark')
    average_mark_by_important_work: Any = Field(None, alias='averageMarkByImportantWork')
    weighted_average_mark: str = Field(None, alias='weightedAverageMark')


class Mark(Type):
    id: int
    value: str
    mood: str


class LessonDetailsMark(Type):
    is_important: bool = Field(None, alias='isImportant')
    is_final: bool = Field(None, alias='isFinal')
    mark_type: str = Field(None, alias='markType')
    mark_type_text: str = Field(None, alias='markTypeText')
    mark_short_type_text: str = Field(None, alias='markShortTypeText')
    period_type: str = Field(None, alias='periodType')
    period_id: int = Field(None, alias='periodId')
    period_number: int = Field(None, alias='periodNumber')
    marks: List[Mark]


class Homework(Type):
    work_is_attach_required: bool = Field(None, alias='workIsAttachRequired')
    attachments: List
    text: str
    is_completed: bool = Field(None, alias='isCompleted')


class LessonDetailsResponse(TypeMobile):
    status: Optional[str] = None
    subject: Optional[Subject] = None
    start_time: Optional[int] = Field(None, alias='startTime')
    end_time: Optional[int] = Field(None, alias='endTime')
    hours: Optional[Hours] = None
    number: Optional[int] = None
    place: Optional[str] = None
    theme: Optional[str] = None
    teacher: Optional[Teacher] = None
    important_works: Optional[List] = Field(None, alias='importantWorks')
    average_marks: Optional[AverageMarks] = Field(None, alias='averageMarks')
    summative_marks: Optional[Any] = Field(None, alias='summativeMarks')
    forecast_text: Optional[Any] = Field(None, alias='forecastText')
    lesson_details_marks: Optional[List[LessonDetailsMark]] = Field(
        None, alias='lessonDetailsMarks'
    )
    homework: Optional[Homework] = None
    attachments: Optional[List] = None
    comment: Optional[Any] = None
    lesson_description: Optional[str] = Field(None, alias='lessonDescription')
