from datetime import datetime
from .model import Type, TypeMobile
from typing import Union, Optional, Any, List
from pydantic import Field


class Period(Type):
    id: int
    number: int
    type: str
    date_start: int = Field(None, alias='dateStart')
    date_finish: int = Field(None, alias='dateFinish')
    study_year: int = Field(None, alias='studyYear')
    is_current: bool = Field(None, alias='isCurrent')


class Mark(Type):
    id: int
    value: str
    mood: str


class MarkDetails(Type):
    is_important: bool = Field(None, alias='isImportant')
    is_final: bool = Field(None, alias='isFinal')
    mark_type: str = Field(None, alias='markType')
    mark_type_text: str = Field(None, alias='markTypeText')
    marks: List[Mark]


class Subject(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class AverageMarks(Type):
    average_mark_trend: str = Field(None, alias='averageMarkTrend')
    average_mark_mood: str = Field(None, alias='averageMarkMood')
    averagemark_by_important_work_trend: str = Field(
        None, alias='averagemarkByImportantWorkTrend'
    )
    weighted_average_mark_trend: str = Field(None, alias='weightedAverageMarkTrend')
    indicator: Any
    average_mark: str = Field(None, alias='averageMark')
    average_mark_by_important_work: Any = Field(None, alias='averageMarkByImportantWork')
    weighted_average_mark: str = Field(None, alias='weightedAverageMark')


class Subject1(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class AverageMarks1(Type):
    average_mark: str = Field(None, alias='averageMark')
    weighted_average_mark: str = Field(None, alias='weightedAverageMark')
    average_mark_trend: str = Field(None, alias='averageMarkTrend')
    weighted_average_mark_trend: str = Field(None, alias='weightedAverageMarkTrend')
    average_mark_mood: str = Field(None, alias='averageMarkMood')


class YAxi(Type):
    value: str
    mood: str


class PlotOptions(Type):
    y_axis: List[YAxi] = Field(None, alias='yAxis')


class WeekAverage(Type):
    number: int
    value: Optional[str]
    is_current_week: bool = Field(None, alias='isCurrentWeek')


class ReportingPeriodsReport(Type):
    period_id: int = Field(None, alias='periodId')
    period_number: int = Field(None, alias='periodNumber')
    period_type: str = Field(None, alias='periodType')
    is_current: bool = Field(None, alias='isCurrent')
    week_averages: List[WeekAverage] = Field(None, alias='weekAverages')


class ReportsPlot(Type):
    knowledge_area_group: str = Field(None, alias='knowledgeAreaGroup')
    knowledge_area_group_name: str = Field(None, alias='knowledgeAreaGroupName')
    subject: Subject1
    average_marks: AverageMarks1 = Field(None, alias='averageMarks')
    plot_options: PlotOptions = Field(None, alias='plotOptions')
    reporting_periods_reports: List[ReportingPeriodsReport] = Field(
        None, alias='reportingPeriodsReports'
    )


class StudentPlace(Type):
    place: int
    image_url: Any = Field(None, alias='imageUrl')


class Category(Type):
    mood: str
    percent: float
    student_count: int = Field(None, alias='studentCount')
    mark_number: int = Field(None, alias='markNumber')
    value: str


class Subject2(Type):
    id: int
    name: str
    knowledge_area: str = Field(None, alias='knowledgeArea')
    subject_mood: Any = Field(None, alias='subjectMood')


class AverageMarks2(Type):
    average_mark: Any = Field(None, alias='averageMark')
    average_mark_trend: str = Field(None, alias='averageMarkTrend')
    weighted_average_mark: str = Field(None, alias='weightedAverageMark')
    weighted_average_mark_trend: str = Field(None, alias='weightedAverageMarkTrend')
    average_mark_mood: str = Field(None, alias='averageMarkMood')
    indicator: Any


class YAxi1(Type):
    value: str
    mood: str


class PlotOptions1(Type):
    y_axis: List[YAxi1] = Field(None, alias='yAxis')


class WeekAverage1(Type):
    number: int
    value: Optional[str]
    is_current_week: bool = Field(None, alias='isCurrentWeek')


class ReportingPeriodsReport1(Type):
    period_id: int = Field(None, alias='periodId')
    period_number: int = Field(None, alias='periodNumber')
    period_type: str = Field(None, alias='periodType')
    is_current: bool = Field(None, alias='isCurrent')
    week_averages: List[WeekAverage1] = Field(None, alias='weekAverages')


class GroupReportsPlot(Type):
    knowledge_area_group: str = Field(None, alias='knowledgeAreaGroup')
    knowledge_area_group_name: str = Field(None, alias='knowledgeAreaGroupName')
    subject: Subject2
    average_marks: AverageMarks2 = Field(None, alias='averageMarks')
    plot_options: PlotOptions1 = Field(None, alias='plotOptions')
    reporting_periods_reports: List[ReportingPeriodsReport1] = Field(
        None, alias='reportingPeriodsReports'
    )


class MarkDetailsResponse(TypeMobile):
    date: Optional[datetime] = None
    lesson_id: Optional[int] = Field(None, alias='lessonId')
    period: Optional[Period] = None
    mark_details: Optional[MarkDetails] = Field(None, alias='markDetails')
    subject: Optional[Subject] = None
    average_marks: Optional[AverageMarks] = Field(None, alias='averageMarks')
    reports_plot: Optional[ReportsPlot] = Field(None, alias='reportsPlot')
    summative_marks: Optional[Any] = Field(None, alias='summativeMarks')
    student_place: Optional[StudentPlace] = Field(None, alias='studentPlace')
    categories: Optional[List[Category]] = None
    group_reports_plot: Optional[GroupReportsPlot] = Field(
        None, alias='groupReportsPlot'
    )
    messenger_entry_point: Optional[Any] = Field(None, alias='messengerEntryPoint')
