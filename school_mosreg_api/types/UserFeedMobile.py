from .model import Type, TypeMobile
from typing import Union, Optional, Any, List
from pydantic import Field


class Hours(Type):
    start_hour: str = Field(None, alias='startHour')
    start_minute: str = Field(None, alias='startMinute')
    end_hour: str = Field(None, alias='endHour')
    end_minute: str = Field(None, alias='endMinute')
    
    @property
    def start_time_str(self) -> Optional[str]:
        if self.start_hour and self.start_minute:
            return f"{self.start_hour}:{self.start_minute}"
        elif self.start_hour:
            return self.start_hour
        elif self.start_minute:
            return self.start_minute
        else:
            return None
    
    
    @property
    def end_time_str(self) -> Optional[str]:
        if self.end_hour and self.end_minute:
            return f"{self.end_hour}:{self.end_minute}"
        elif self.end_hour:
            return self.end_hour
        elif self.end_minute:
            return self.end_minute
        else:
            return None
    


class Subject(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class TomorrowLesson(Type):
    id: int
    number: int
    place: str
    start_time: int = Field(None, alias='startTime')
    end_time: int = Field(None, alias='endTime')
    hours: Hours
    subject: Subject
    
    @property
    def start_time_str(self) -> Optional[str]:
        if self.hours.start_hour and self.hours.start_minute:
            return f"{self.hours.start_hour}:{self.hours.start_minute}"
        elif self.hours.start_hour:
            return self.hours.start_hour
        elif self.hours.start_minute:
            return self.hours.start_minute
        else:
            return None
    
    
    @property
    def end_time_str(self) -> Optional[str]:
        if self.hours.end_hour and self.hours.end_minute:
            return f"{self.hours.end_hour}:{self.hours.end_minute}"
        elif self.hours.end_hour:
            return self.hours.end_hour
        elif self.hours.end_minute:
            return self.hours.end_minute
        else:
            return None


class Schedule(Type):
    today_lessons: List[TomorrowLesson] = Field(None, alias='todayLessons')
    tomorrow_lessons: List[TomorrowLesson] = Field(None, alias='tomorrowLessons')
    next_lesson_date: Any = Field(None, alias='nextLessonDate')


class Category(Type):
    mood: str
    percent: float
    student_count: int = Field(None, alias='studentCount')
    mark_number: int = Field(None, alias='markNumber')
    value: str


class Subject1(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class Lesson(Type):
    id: int
    date: int
    theme: str


class Mark(Type):
    id: int
    value: str
    mood: str


class RecentMark(Type):
    categories: List[Category]
    date: int
    subject: Subject1
    mark_type: str = Field(None, alias='markType')
    criteria_mark_type: str = Field(None, alias='criteriaMarkType')
    mark_type_text: str = Field(None, alias='markTypeText')
    short_mark_type_text: str = Field(None, alias='shortMarkTypeText')
    lesson: Lesson
    is_new: bool = Field(None, alias='isNew')
    is_final: bool = Field(None, alias='isFinal')
    is_important: bool = Field(None, alias='isImportant')
    marks: List[Mark]
    indicator: Any


class HomeworksProgress(Type):
    total_lessons_with_homeworks_count: int = Field(
        None, alias='totalLessonsWithHomeworksCount'
    )
    completed_lessons_with_homeworks_count: int = Field(
        None, alias='completedLessonsWithHomeworksCount'
    )
    lesson_with_homeworks_ids: List[int] = Field(None, alias='lessonWithHomeworksIds')


class Context(Type):
    charge_level: int = Field(None, alias='chargeLevel')
    is_geolocation_enabled: bool = Field(None, alias='isGeolocationEnabled')
    is_background_refresh_enabled: bool = Field(None, alias='isBackgroundRefreshEnabled')


class Zone(Type):
    id: int
    name: str
    zone_type: str = Field(None, alias='zoneType')
    radius: int
    latitude: float
    longitude: float


class ChildLocationInfo(Type):
    code: int
    person_id: int = Field(None, alias='personId')
    last_location: Any = Field(None, alias='lastLocation')
    context: Context
    zones: List[Zone]


class Subject2(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class Mark1(Type):
    id: int
    value: str
    mood: str


class SubjectMark(Type):
    marks: List[Mark1]


class AverageMarks(Type):
    average_mark_trend: str = Field(None, alias='averageMarkTrend')
    average_mark_mood: str = Field(None, alias='averageMarkMood')
    averagemark_by_important_work_trend: str = Field(
        None, alias='averagemarkByImportantWorkTrend'
    )
    weighted_average_mark_trend: str = Field(None, alias='weightedAverageMarkTrend')
    indicator: Any
    average_mark: str = Field(None, alias='averageMark')
    average_mark_by_important_work: Optional[str] = Field(
        None, alias='averageMarkByImportantWork'
    )
    weighted_average_mark: str = Field(None, alias='weightedAverageMark')


class Item(Type):
    date: int
    subject: Subject2
    subject_marks: List[SubjectMark] = Field(None, alias='subjectMarks')
    average_marks: AverageMarks = Field(None, alias='averageMarks')
    messenger_entry_point: Any = Field(None, alias='messengerEntryPoint')


class Subject3(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class AverageMarks1(Type):
    average_mark: str = Field(None, alias='averageMark')
    average_mark_by_important_work: str = Field(None, alias='averageMarkByImportantWork')
    weighted_average_mark: str = Field(None, alias='weightedAverageMark')


class Work(Type):
    date: int
    work_type_name: str = Field(None, alias='workTypeName')
    subject: Subject3
    knowledge_area: str = Field(None, alias='knowledgeArea')
    lesson_id: int = Field(None, alias='lessonId')
    lesson_number: int = Field(None, alias='lessonNumber')
    average_marks: AverageMarks1 = Field(None, alias='averageMarks')
    summative_marks: Any = Field(None, alias='summativeMarks')
    messenger_entry_point: Any = Field(None, alias='messengerEntryPoint')


class Content(Type):
    date: Optional[int] = None
    items: Optional[List[Item]] = None
    works: Optional[List[Work]] = None


class FeedItem(Type):
    type: str
    time_stamp: int = Field(None, alias='timeStamp')
    content: Content


class RankingPosition(Type):
    trend_description: str = Field(None, alias='trendDescription')
    place_trend: str = Field(None, alias='placeTrend')
    place: int


class RankingPlace(Type):
    image_url: str = Field(None, alias='imageUrl')
    is_context_user: bool = Field(None, alias='isContextUser')


class Rating(Type):
    ranking_position: RankingPosition = Field(None, alias='rankingPosition')
    ranking_places: List[RankingPlace] = Field(None, alias='rankingPlaces')


class UserFeedResponse(Type):
    schedule: Optional[Schedule] = None
    recent_marks: Optional[List[RecentMark]] = Field(None, alias='recentMarks')
    homeworks_progress: Optional[HomeworksProgress] = Field(
        None, alias='homeworksProgress'
    )
    child_location_info: Optional[ChildLocationInfo] = Field(
        None, alias='childLocationInfo'
    )
    feed: Optional[List[FeedItem]] = None
    rating: Optional[Rating] = None