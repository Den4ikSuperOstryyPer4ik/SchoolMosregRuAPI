from typing import Any, List, Optional

from pydantic import Field
from .model import Type, TypeMobile


class Subject(Type):
    id: int
    name: str
    knowledge_area: Optional[str] = Field(None, alias='knowledgeArea')
    subject_mood: Optional[str] = Field(None, alias='subjectMood')


class AverageMarks(Type):
    average_mark_trend: str = Field(None, alias='averageMarkTrend')
    average_mark_mood: str = Field(None, alias='averageMarkMood')
    averagemark_by_important_work_trend: str = Field(
        None, alias='averagemarkByImportantWorkTrend'
    )
    weighted_average_mark_trend: str = Field(None, alias='weightedAverageMarkTrend')
    indicator: Any
    average_mark: Optional[str] = Field(None, alias='averageMark')
    average_mark_by_important_work: Optional[str] = Field(
        None, alias='averageMarkByImportantWork'
    )
    weighted_average_mark: Optional[str] = Field(None, alias='weightedAverageMark')


class Mark(Type):
    id: int
    value: str
    mood: str


class RecentMark(Type):
    date: int
    marks: List[Mark]
    is_new: bool = Field(None, alias='isNew')


class PeriodMark(Type):
    subject: Subject
    average_marks: AverageMarks = Field(None, alias='averageMarks')
    summative_marks: Any = Field(None, alias='summativeMarks')
    recent_marks: List[RecentMark] = Field(None, alias='recentMarks')
    final_mark: Any = Field(None, alias='finalMark')
    ranking_place: Optional[int] = Field(None, alias='rankingPlace')


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


class MarksResponse(TypeMobile):
    period_number: int = Field(None, alias='periodNumber')
    period_marks: List[PeriodMark] = Field(None, alias='periodMarks')
    rating: Rating
    ask_teacher: Any = Field(None, alias='askTeacher')
