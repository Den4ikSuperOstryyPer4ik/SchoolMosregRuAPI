from .model import Type, TypeMobile
from typing import Union, Optional, Any, List
from pydantic import Field


class Setting(Type):
    push_type: str = Field(None, alias='pushType')
    name: str
    is_enabled: bool = Field(None, alias='isEnabled')


class PushSettingsResponse(TypeMobile):
    settings: Optional[List[Setting]] = None


class Avatar(Type):
    user_id: Optional[int] = Field(None, alias='userId')
    url: Optional[str] = None


class UserAvatarResponse(TypeMobile):
    avatar: Optional[Avatar] = None


class Info(Type):
    sex: str
    user_id: int = Field(None, alias='userId')
    person_id: int = Field(None, alias='personId')
    first_name: str = Field(None, alias='firstName')
    middle_name: str = Field(None, alias='middleName')
    last_name: str = Field(None, alias='lastName')
    avatar_url: str = Field(None, alias='avatarUrl')
    current_culture_code: str = Field(None, alias='currentCultureCode')


class School(Type):
    id: int
    name: str
    type: str
    avatar_url: Any = Field(None, alias='avatarUrl')
    radius: Any
    latitude: Any
    longitude: Any


class Group(Type):
    id: int
    name: str


class Period(Type):
    id: int
    number: int
    type: str
    date_start: int = Field(None, alias='dateStart')
    date_finish: int = Field(None, alias='dateFinish')
    study_year: int = Field(None, alias='studyYear')
    is_current: bool = Field(None, alias='isCurrent')


class ReportingPeriodGroup(Type):
    id: int
    type: str
    periods: List[Period]


class ContextPerson(Type):
    sex: str
    user_id: int = Field(None, alias='userId')
    person_id: int = Field(None, alias='personId')
    first_name: str = Field(None, alias='firstName')
    middle_name: str = Field(None, alias='middleName')
    last_name: str = Field(None, alias='lastName')
    avatar_url: str = Field(None, alias='avatarUrl')
    school: School
    group: Group
    reporting_period_group: ReportingPeriodGroup = Field(
        None, alias='reportingPeriodGroup'
    )


class Experiments(Type):
    notes: bool
    without_support_button: bool = Field(None, alias='withoutSupportButton')
    mobile_chat_experiment: bool = Field(None, alias='mobileChatExperiment')
    kid_tracker_value_test: bool = Field(None, alias='kidTrackerValueTest')
    full_data_local_validation_experiment: bool = Field(
        None, alias='fullDataLocalValidationExperiment'
    )
    ratings_turn_off_experiment: bool = Field(None, alias='ratingsTurnOffExperiment')
    week_view_lesson_list_experiment: bool = Field(
        None, alias='weekViewLessonListExperiment'
    )
    blocker_lessons_list_experiment: bool = Field(
        None, alias='blockerLessonsListExperiment'
    )
    blocker_mark_experiment: bool = Field(None, alias='blockerMarkExperiment')
    homework_push_mobile_experiment: bool = Field(
        None, alias='homeworkPushMobileExperiment'
    )
    messenger_mongoose_mobile_teacher_experiment: bool = Field(
        None, alias='messengerMongooseMobileTeacherExperiment'
    )
    community_invitation_experiment: bool = Field(
        None, alias='communityInvitationExperiment'
    )


class UserContextResponse(TypeMobile):
    info: Optional[Info] = None
    context_persons: Optional[List[ContextPerson]] = Field(None, alias='contextPersons')
    experiments: Optional[Experiments] = None
    firebase_experiments: Optional[List] = Field(None, alias='firebaseExperiments')
    onboarding: Optional[Any] = None
    full_screen_banner: Optional[Any] = Field(None, alias='fullScreenBanner')


class UploadResponse(TypeMobile):
    taskId: Optional[str] = None


class AuthData(Type):
    username: str
    password: str
    clientId: str
    clientSecret: str
    scope: str

class Credentials(Type):
    accessToken: str
    userId: int


class AuthResult(TypeMobile):
    credentials: Optional[Credentials] = None
    reason: Optional[str] = None


    