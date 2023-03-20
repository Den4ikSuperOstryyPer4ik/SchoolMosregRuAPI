from .model import Type, TypeMobile
from typing import Union, Optional, Any, List
from pydantic import Field


class RankingPosition(Type):
    trend_description: Optional[str] = Field(None, alias='trendDescription')
    place_trend: Optional[str] = Field(None, alias='placeTrend')
    place: Optional[int]
    description: Optional[str]
    background_image_url: Optional[str] = Field(None, alias='backgroundImageUrl')


class HistoryItem(Type):
    place: Optional[int]
    date: Optional[str]


class History(Type):
    ranking_position: Optional[RankingPosition] = Field(None, alias='rankingPosition')
    history_items: List[Optional[HistoryItem]] = Field(None, alias='historyItems')


class RankingPlace(Type):
    place: Optional[int]
    image_url: Optional[str] = Field(None, alias='imageUrl')
    average_mark: Optional[str] = Field(None, alias='averageMark')
    is_context_user: Optional[bool] = Field(None, alias='isContextUser')
    trend: Optional[str]


class Rating(Type):
    ranking_places: List[Optional[RankingPlace]] = Field(None, alias='rankingPlaces')


class Subject1(Type):
    id: Optional[int]
    name: Optional[str]
    knowledge_area: Optional[str] = Field(None, alias='knowledgeArea')
    subject_mood: Optional[str] = Field(None, alias='subjectMood')


class Subject(Type):
    place: Optional[int]
    subject: Optional[Subject1]
    trend: Optional[str]
    average_mark: Optional[str] = Field(None, alias='averageMark')


class SubjectTop(Type):
    subjects: List[Optional[Subject]]


class RatingDescription(Type):
    body: Optional[str]


class RatingResponse(TypeMobile):
    history: Optional[History] = None
    rating: Optional[Rating] = None
    subject_top: Optional[SubjectTop] = Field(None, alias='subjectTop')
    rating_description: Optional[RatingDescription] = Field(
        None, alias='ratingDescription'
    )
