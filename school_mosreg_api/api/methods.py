from datetime import date, datetime
from typing import Any
from .base import BaseAPI
from .. import types

class SchoolMosregRUAPI(BaseAPI):
    """Основной sync класс почти со всеми функциями API.\n~~~"""
    
    def __init__(self, login: str = None, password: str = None, token: str = None) -> None:
        super().__init__(login, password, token)

        try:
            self.me_context = self.get_context()
            self.me_user = self.get_user()
            self.me_person = self.get_person()
        except:
            self.me_context = None
            self.me_user = None
            self.me_person = None
    
    
    def check_person(self, value):
        if value == "me":
            return (self.me_context).personId if self.me_context else (self.get_user()).personId
        else:
            return value
        
    def check_user(self, value):
        if value == "me":
            return (self.me_user).id if self.me_user else (self.get_user()).id
        else:
            return value
    
    def get_me_organizations(self) -> list[int] | None:
        """[GET] users/me/organizations
        
        Список идентификаторов организаций текущего пользователя
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Authorities/Authorities_GetOwnOrganizations
        """
        
        return self.get("users/me/organizations", return_json=True)
    
    def get_organization(self, organizationId: int | str) -> types.Organization:
        """[GET] users/me/organizations/{organizationId}
        
        Данные указанной организации пользователя.
        
        Параметры:
            organizationId: Идентификатор организации (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Authorities/Authorities_GetOrganizationInfo
        """
        
        
        return self.get(f"users/me/organizations/{organizationId}", model=types.Organization)
    
    def get_token_with_code(self, code: str, client_id: str, client_secret: str, grant_type: str, refreshToken: str) -> types.TokenWithCode:
        """[POST] authorizations
        
        Обменять код доступа на токен
        
        Параметры:
            code: ``str``
            client_id: ``str``
            client_secret: ``str``
            grant_type: ``str``
            refreshToken: ``str``
        
        Параметры запроса [POST] method="authorizations":
            data: Код доступа -> Пример: ``{``
                ``"code": "string",``
                ``"client_id": "00000000-0000-0000-0000-000000000000",``
                ``"client_secret": "00000000-0000-0000-0000-000000000000",``
                ``"grant_type": "NotSet",``
                ``"refreshToken": "string"``
            ``}``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Authorizations/Authorizations_PostTokenRequestCode
        """
        
        return self.post("authorizations", model=types.TokenWithCode, data={
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "refreshToken": refreshToken})
        
    def get_person_avg_marks(self, person: int | str, period) -> str | None:
        """[GET] persons/{person}/reporting-periods/{period}/avg-mark
        
        Оценка персоны за отчетный период
        
        Параметры:
            person: id персоны (``"me"``, для себя)
            period: id отчетного периода
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/AverageMarks/AverageMarks_GetByPersonAndPeriod
        """
        
        return self.get(f"persons/{self.check_person(person)}/reporting-periods/{period}/avg-mark", return_json=True)
    
    def get_person_avg_marks_by_subject(self, person: int | str, period, subject) -> str | None:
        """[GET] persons/{person}/reporting-periods/{period}/subjects/{subject}/avg-mark
        
        Оценка персоны по предмету за отчетный период
        
        Параметры:
            person: id персоны (``"me"``, для себя)
            period: id отчетного периода
            subject: id предмета
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/AverageMarks/AverageMarks_GetByPersonAndPeriodAndSubject
        """
        
        return self.get(f"persons/{self.check_person(person)}/reporting-periods/{period}/subjects/{subject}/avg-mark", return_json=True)
    
    def get_eduGroup_avg_marks_to_date(self, group: int | str, period: int | str, date: datetime | date) -> list[dict[str, Any]] | None:
        """[GET] edu-groups/{group}/reporting-periods/{period}/avg-marks/{date}
        
        Оценки учебной группы по предмету за отчетный период до определенной даты
        
        Параметры:
            group: id учебной группы (``EduGroup``) (``int`` / ``str``)
            period: id отчетного периода (``int`` / ``str``)
            date: дата (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/AverageMarks/AverageMarks_GetByGroupAndPeriodOnDate
        """
        
        return self.get(f"edu-groups/{group}/reporting-periods/{period}/avg-marks/{self.datetime_to_string(date)}", return_json=True)
    
    def get_eduGroup_avg_marks(self, group: int | str, from_: datetime | date, to: datetime | date) -> list[dict[str, Any]] | None:
        """[GET] edu-groups/{group}/avg-marks/{from}/{to}
        
        Оценки учебной группы за период
        
        Параметры:
            group: id учебной группы (``EduGroup``) (``int`` / ``str``)
            from_: id начало периода (``datetime.datetime`` / ``datetime.date``)
            to: id конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/AverageMarks/AverageMarks_ListByGroupAndDates
        """
        
        return self.get(f"edu-groups/{group}/avg-marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", return_json=True)
    
    def get_user_childrens(self, userID: str | int = "me") -> list[types.Children] | None:
        """[GET] user/{userID}/children
        
        Получение списка детей по идентификатору родительского пользователя
        
        Параметры:
            userID: 'id' пользователя (``str`` / ``int``) (``"me"``, для себя)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Children/Children_GetChildrenByUserID
        """
        
        return self.get(f"user/{self.check_user(userID)}/children", model=types.Children, is_list=True)
    
    def get_person_childrens(self, personID: str | int = "me") -> list[types.Children] | None:
        """[GET] person/{personID}/children
        
        Получение списка детей по идентификатору родительской персоны
        
        Параметры:
            personID: 'id' пользователя (``str`` / ``int``) (``"me"``, для себя)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Children/Children_GetChildrenByPersonID
        """
        
        return self.get(f"person/{self.check_person(personID)}/children", model=types.Children, is_list=True)
     
    def get_me_classmates(self) -> list[int] | None:
        """[GET] users/me/classmates
        
        Список id пользователей одноклассников текущего пользователя, если он является учеником,
        либо список активных участников образовательных групп пользователя во всех остальных случаях
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Classmates/Classmates_GetOwnClassmates
        """
        
        return self.get("users/me/classmates", return_json=True)
    
    def get_context(self, userId: str | int = "me") -> types.Context:
        """[GET] users/{userId}/context | users/me/context
        
        Получение контекстной информации по пользователю
        
        Параметры:
            userId: id пользователя ("me" или оставьте пустым для себя) (int/str)
        
        Права доступа: ``CommonInfo``, ``FriendsAndRelatives``, ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Context
        """
        
        self.me_context = self.get(f"users/{userId}/context", model=types.Context)
        return self.me_context
    
    def get_user_school_memberships(self, user: int | str = "me") -> types.SchoolMemberships:
        """[GET] users/{user}/school-memberships
        
        Список участий в школах для произвольного пользователя
        
        Параметры:
            user: id пользователя (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetByUser
        """
        
        return self.get(f"users/{user}/school-memberships", model=types.SchoolMemberships)
    
    def get_user_education(self, user: int | str = "me") -> types.SchoolMemberships:
        """[GET] users/{user}/education
        
        Список участий в школах для произвольного пользователя
        
        Параметры:
            user: id пользователя (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetByUser_0
        """
        
        return self.get(f"users/{self.check_user(user)}/education", model=types.SchoolMemberships)
    
    def get_person_education(self, person: int | str = "me") -> list[types.SchoolMemberships]:
        """[GET] persons/{person}/school-memberships
        
        Список участий в школах для произвольного пользователя
        
        Параметры:
            person: id персоны (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetSchoolMembershipsByPerson
        """
        
        return self.get(f"persons/{self.check_person(person)}/school-memberships", model=types.SchoolMemberships)
    
    def get_user_schools(self, user: str | int = "me") -> list[int] | None:
        """[GET] users/{user}/schools | users/me/schools
        
        Список идентификаторов школ произвольного/текущего пользователя
        
        Параметры:
            user: id пользователя (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetSchoolsByUser
        """
        
        return self.get(f"users/{user}/schools", return_json=True)
    
    def get_user_eduGroups(self, user: str | int = "me") -> list[int] | None:
        """[GET] users/{user}/edu-groups | users/me/edu-groups
        
        Список идентификаторов классов произвольного/текущего пользователя
        
        Параметры:
            user: id пользователя (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetEduGroupsByUser
        """
        
        return self.get(f"users/{user}/edu-groups", return_json=True)
        
    def get_eduGroup(self, eduGroup: int | str) -> types.EduGroup:
        """[GET] edu-groups/{eduGroup}
        
        Класс или учебная группа
        
        Параметры:
            eduGroup: id класса или образовательной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_Get
        """
        
        return self.get(f"edu-groups/{eduGroup}", model=types.EduGroup)
    
    def get_school_eduGroups(self, school: str | int) -> list[types.EduGroup]:
        """[GET] schools/{school}/edu-groups
        
        Список классов в школе
        
        Параметры:
            school: id школы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_GetBySchool
        """
        
        return self.get(f"schools/{school}/edu-groups", model=types.EduGroup, is_list=True)
    
    def get_person_eduGroups(self, person: str | int = "me") -> list[types.EduGroup]:
        """[GET] persons/{person}/edu-groups
        
        Учебные группы персоны
        
        Параметры:
            person: id персоны (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_GetByPerson
        """
        
        return self.get(f"persons/{self.check_person(person)}/edu-groups", model=types.EduGroup, is_list=True)
    
    def get_eduGroup_persons(self, eduGroup: int | str) -> list[types.Person] | None:
        """[GET] edu-groups/{eduGroup}/persons
        
        Список учеников учебной группы
        
        Параметры:
            eduGroup: id учебной группы (int/str)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_GetGroupPersons
        """
        
        return self.get(f"edu-groups/{eduGroup}/persons", model=types.Person, is_list=True)
    
    def get_parallel_eduGroups(self, groupId: int | str) -> list[types.EduGroup]:
        """[GET] edu-groups/{groupId}/parallel
        
        Учебные группы персоны
        
        Параметры:
            person: id персоны (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_ListParallelGroups
        """
        
        return self.get(f"edu-groups/{groupId}/parallel", model=types.EduGroup, is_list=True)

    def get_homeworks_by_period(self, school: str | int, startDate: datetime | date, endDate: datetime | date) -> types.HomeWork:
        """[GET] users/me/school/{school}/homeworks?startDate={startDate}&endDate={endDate}
        
        Получить домашние задания пользователя за период времени
        
        Параметры:
            school: id школы (``int`` / ``str``)
            startDate: дата начало периода (``datetime.datetime`` / ``datetime.date``)
            endDate: дата конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Homeworks/Homeworks_ListUserHomeworksByPeriod
        """
        
        return self.get(f"users/me/school/{school}/homeworks?startDate={self.datetime_to_string(startDate)}&endDate={self.datetime_to_string(endDate)}", model=types.HomeWork)

    def get_homeworks_by_Ids(self, ids: int | str | list[int | str]) -> types.HomeWork:
        """[GET] users/me/school/homeworks?homeworkId={ids}
        
        Получить домашние задания по идентификаторам
        
        Параметры:
            ids: work-id домашнего задания (допускается лист) (``int`` / ``str`` / ``list[str / int]``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Homeworks/Homeworks_GetUserHomeworkByIds
        """
        
        return self.get(f"users/me/school/homeworks?homeworkId={ids if (isinstance(ids, int) or isinstance(ids, str)) else '&homeworkId='.join(ids)}", model=types.HomeWork)

    def get_lesson_log_entries(self, lesson: str | int) -> list[types.LessonLogEntries] | None:
        """[GET] lessons/{lesson}/log-entries
        
        Список отметок о посещаемости на уроке
        
        Параметры:
            lesson: id урока (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/LessonLog/LessonLog_GetByLesson
        """
        
        return self.get(f"lessons/{lesson}/log-entries", model=types.LessonLogEntries, is_list=True)
    
    def get_person_lesson_log_entries(self, lesson: str | int, person: str | int = "me") -> types.LessonLogEntries:
        """[GET] lesson-log-entries/lesson/{lesson}/person/{person}
        
        Отметка о посещаемости ученика на уроке
        
        Параметры:
            lesson: id урока (int / str)
            person: id персоны ("me" или оставьте пустым для себя) (int/str)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/LessonLog/LessonLog_Get
        """
        
        return self.get(f"lesson-log-entries/lesson/{lesson}/person/{self.check_person(person)}/edu-groups", model=types.LessonLogEntries)
    
    def get_eduGroup_lessons_log_entries(self, eduGroup: str | int, subject: str | int, from_: datetime | date, to: datetime | date) -> list[types.LessonLogEntries]:
        """[GET] lesson-log-entries/group/{eduGroup}?subject={subject}&from={from_}&to={to}
        
        Список отметок о посещаемости на уроках
        по заданному предмету в классе за интервал времени
        
        Параметры:
            eduGroup: id учебной группы / класса (``int`` / ``str``)
            subject: id предмета (``int`` / ``str``)
            from_: начало интервала (``datetime.datetime`` / ``datetime.date``)
            to: конец интервала (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/LessonLog/LessonLog_Get
        """
        
        return self.get(f"lesson-log-entries/group/{eduGroup}?subject={subject}&from={self.datetime_to_string(from_)}&to={self.datetime_to_string(to)}", model=types.LessonLogEntries, is_list=True)
    
    def get_person_lessons_log_entries_by_subject(self, personID: str | int, subjectID: str | int, from_: datetime | date, to: datetime | date) -> list[types.LessonLogEntries]:
        """[GET] lesson-log-entries/person={personID}&subject={subjectID}&from={from}&to={to}
        
        Список отметок о посещаемости обучающегося
        по предмету за интервал времени
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            subject: id предмета (``int`` / ``str``)
            from_: начало интервала (``datetime.datetime`` / ``datetime.date``)
            to: конец интервала (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/LessonLog/LessonLog_ListByPersonAndSubjectAndDateRange_0
        """
        
        return self.get(f"lesson-log-entries/person={self.check_person(personID)}&subject={subjectID}&from={self.datetime_to_string(from_)}&to={self.datetime_to_string(to)}", model=types.LessonLogEntries, is_list=True)
    
    def get_person_lessons_log_entries(self, person: str | int, from_: datetime | date, to: datetime | date) -> list[types.LessonLogEntries]:
        """[GET] persons/{person}/lesson-log-entries&from={from}&to={to}
        
        Список отметок о посещаемости обучающегося за интервал времени
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            subject: id предмета (``int`` / ``str``)
            from_: начало интервала (``datetime.datetime`` / ``datetime.date``)
            to: конец интервала (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/LessonLog/LessonLog_GetByPersonAndPeriod
        """
        
        return self.get(f"persons/{self.check_person(person)}/lesson-log-entries&from={self.datetime_to_string(from_)}&to={self.datetime_to_string(to)}", model=types.LessonLogEntries, is_list=True)
    
    def get_lesson(self, lesson: str | int) -> types.Lesson:
        """[GET] lesssons/{lesson}
        
        Получить урок с заданным id
        
        Параметры:
            lesson: id урока (int / str)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Lessons/Lessons_Get
        """
        return self.get(f"lessons/{lesson}", model=types.Lesson)
    
    def get_eduGroup_lesson_by_period(self, group: int | str, from_: datetime | date, to: datetime | date) -> list[types.Lesson]:
        """[GET] edu-groups/{group}/lessons/{from_}/{to}
        
        Уроки группы за период
        
        Параметры:
            group: id класса или учебной группы (``str`` / ``int``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Lessons/Lessons_GetByGroupAndPeriod
        """
        return self.get(f"edu-groups/{group}/lessons/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Lesson, is_list=True)
    
    def get_eduGroup_lesson_by_period_and_subject(self, group: int | str, subject: int | str, from_: datetime | date, to: datetime | date) -> list[types.Lesson]:
        """[GET] edu-groups/{group}/subjects/{subject}/lessons/{from_}/{to}
        
        Уроки группы по предмету за период
        
        Параметры:
            group: id класса или учебной группы (``str`` / ``int``)
            subject: id предмета (``str`` / ``int``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Lessons/Lessons_GetByGroupAndPeriodAndSubject
        """
        return self.get(f"edu-groups/{group}/subjects/{subject}/lessons/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Lesson, is_list=True)
    
    def get_work_marks_histogram(self, workID: int | str) -> types.MarksHistogram:
        """[GET] works/{workID}/marks/histogram
        
        Получение деперсонализированной гистограмы оценок всего класса по идентификатору работы
        
        Параметры:
            workID: id работы на уроке (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/MarkHistograms/MarkHistograms_GetMarksByWork
        """
        return self.get(f"works/{workID}/marks/histogram", model=types.MarksHistogram)
        
    def get_marks_histogram_by_period(self, periodID: int | str, subjectID: int | str, groupID: int | str) -> types.MarksHistogramByPeriod:
        """[GET] periods/{periodID}/subjects/{subjectID}/groups/{groupID}/marks/histogram
        
        Получение деперсонализированной гистограмы оценок всего класса за отчетный период
        
        Параметры:
            periodID: id отчетного периода (``int`` / ``str``)
            subjectID: id предмета (``int`` / ``str``)
            groupID: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/MarkHistograms/MarkHistograms_GetMarksByPeriod
        """
        
        return self.get(f"periods/{periodID}/subjects/{subjectID}/groups/{groupID}/marks/histogram", model=types.MarksHistogramByPeriod)
    
    def get_mark(self, mark: int | str) -> types.Mark:
        """[GET] marks/{mark}
        
        Оценка
        
        Параметры:
            mark: id оценки (не work-id!) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_Get
        """
        
        return self.get(f"marks/{mark}", model=types.Mark)

    def get_work_marks(self, work: int | str) -> list[types.Mark]:
        """[GET] works/{work}/marks
        
        Список оценок за определенную работу на уроке
        
        Параметры:
            work: id работы (не mark-id или lesson-id!) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByWork
        """
        
        return self.get(f"works/{work}/marks", model=types.Mark, is_list=True)

    def get_lesson_marks(self, lesson: int | str) -> list[types.Mark]:
        """[GET] lessons/{lesson}/marks
        
        Оценки на уроке
        
        Параметры:
            lessson: id урока (не mark-id или work-id!) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByLesson
        """
        
        return self.get(f"lessons/{lesson}/marks", model=types.Mark, is_list=True)
    
    def get_eduGroup_marks(self, group: int | str, from_: datetime | date, to: datetime | date) -> list[types.Mark]:
        """[GET] edu-groups/{group}/marks/{from_}/{to}
        
        Оценки учебной группы за период
        
        Параметры:
            group: id учебной группы или класса (``int`` / ``str``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByGroup
        """
        
        return self.get(f"edu-groups/{group}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_eduGroup_marks_by_subject(self, group: int | str, subject: int | str, from_: datetime | date, to: datetime | date) -> list[types.Mark]:
        """[GET] edu-groups/{group}/subjects/{subject}/marks/{from_}/{to}
        
        Оценки учебной группы по предмету за период 
        
        Параметры:
            group: id учебной группы или класса (``int`` / ``str``)
            subject: id предмета (``int`` / ``str``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByGroupAndSubject
        """
        
        return self.get(f"edu-groups/{group}/subjects/{subject}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_person_marks_in_school(self, person: int | str, school: int | str, from_: datetime | date, to: datetime | date) -> list[types.Mark]:
        """[GET] persons/{person}/schools/{school}/marks/{from}/{to}
        
        Оценки персоны в школе за период
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            school: id школы (``int`` / ``str``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetBySchoolAndPersonAndPeriod
        """
        
        return self.get(f"persons/{self.check_person(person)}/schools/{school}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_person_marks_in_eduGroup(self, person: int | str, group: int | str, from_: datetime | date, to: datetime | date) -> list[types.Mark]:
        """[GET] persons/{person}/edu-groups/{group}/marks/{from}/{to}
        
        Оценки персоны в учебной группе за период
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            group: id учебной группы (``int`` / ``str``) (``EduGroup``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByGroupAndPersonAndPeriod
        """
        
        return self.get(f"persons/{self.check_person(person)}/edu-groups/{group}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_person_marks_on_lesson(self, person: int | str, lesson: str | int) -> list[types.Mark]:
        """[GET] persons/{person}/lessons/{lesson}/marks
        
        Оценки персоны за урок
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            lesson: id урока (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByLessonAndPerson
        """
        
        return self.get(f"persons/{self.check_person(person)}/lessons/{lesson}/marks", model=types.Mark, is_list=True)
    
    def get_person_marks_on_work(self, person: int | str, work: str | int) -> list[types.Mark]:
        """[GET] persons/{person}/lessons/{lesson}/marks
        
        Оценки персоны за работу
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            work: id работы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByWorkAndPerson
        """
        
        return self.get(f"persons/{self.check_person(person)}/works/{work}/marks", model=types.Mark, is_list=True)
    
    def get_person_marks_by_subject(self, person: int | str, subject: int | str, from_: datetime | date, to: datetime | date) -> list[types.Mark]:
        """[GET] persons/{person}/subjects/{subject}/marks/{from_}/{to}
        
        Оценки персоны по предмету за период
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            subject: id предмета (``int`` / ``str``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByPersonAndSubject
        """
        
        return self.get(f"persons/{person}/subjects/{subject}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_person_marks_on_lesson_by_date(self, person: int | str, date: datetime | date) -> list[types.Mark]:
        """[GET] lessons/{date}/persons/{person}/marks
        
        Оценки персоны по дате урока
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            date: дата урока (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByPersonAndLessonDate
        """
        
        return self.get(f"lessons/{date}/persons/{self.check_person(person)}/marks", model=types.Mark, is_list=True)
    
    def get_person_marks_by_date(self, person: int | str, date: datetime | date) -> list[types.Mark]:
        """[GET] persons/{person}/marks/{date}
        
        Оценки персоны по дате выставления оценки
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            date: дата выставления оценки (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByPersonAndMarkDate
        """
        
        return self.get(f"persons/{self.check_person(person)}/marks/{date}", model=types.Mark, is_list=True)
    
    def get_marks_values(self) -> dict[str, list[str, None]]:
        """[GET] marks/values
        
        Метод возвращает все поддерживаемые системы (типы) оценок и все возможные оценки в каждой из систем.\n
        Например, для системы "mark5" возвращается массив из следующих оценок:
        "mark5" : ["1-","1","1+","2-","2","2+","3-","3","3+","4-","4","4+","5-","5","5+"]
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/MarkValues/MarkValues_GetAll
        """

        return self.get("marks/values", return_json=True)
    
    def get_marks_values_by_type(self, type: str) -> list[str]:
        """[GET] marks/values/type/{type}
        
        Метод возвращает все возможные оценки в запрашиваемой системе (типе) оценок.\n
        Чтобы узнать, какие типы поддерживаются нужно предварительно делать запрос marks/values без параметров.\n
        Например, для запроса marks/values/type/mark5 ответом
        будет list["1-", "1", "1+", "2-", "2", "2+", "3-", "3", "3+", "4-", "4", "4+", "5-", "5", "5+"].
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/MarkValues/MarkValues_GetByType
        """

        return self.get(f"marks/values/type/{type}", return_json=True)
    
    def get_recent_marks(self, person: str | int, group: int | str, fromDate: datetime | date = None, subject: int | str = None, limit: int = 10) -> types.RecentMarks:
        """[GET] persons/{person}/group/{group}/recentmarks
        
        Последние оценки/отметки посещаемости персоны по предмету,
        указанному в параметре subject, начиная с даты определенном в параметре fromDate,
        и с ограничением на выводимое количество указанном в параметре limit
        
        Параметры:
            ``person``: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            ``group``: id класса или учебной группы (``int`` / ``str``)
            
            ``*OPTIONAL*``:
                ``fromDate``: (``datetime.datetime`` / ``datetime.date``) Дата и время, начиная от которого будут выводится оценки/отметки посещаемости.
                Если не указанно, то результат будет выводится с сегодняшнего дня включительно.
                Параметр применим для постраничного вывода оценок/отметок посещаемости по конкретному предмету
                
                ``subject``: (``int`` / ``str``) id предмета. Если не задан, то результат будет включать в себя оценки/отметки посещаемости по всем предметам,
                но по каждому предмету будет накладываться ограничение указанном в параметре limit
                
                ``limit``: (``int`` = 10) Количество оценок по предмету.
                Если не задан, то будет применено ограничение по умолчанию, равное 10.
                Значение должно быть задано в интервале от 1 до 100.
        
        """
        params = {"limit": str(limit)}
        
        if fromDate:
            params["fromDate"] = self.datetime_to_string(fromDate)
        
        if subject:
            params["subject"] = str(subject)
        
        return self.get(f"persons/{self.check_person(person)}/group/{group}/recentmarks", params=params, model=types.RecentMarks)
    
    def get_task(self, task: str | int) -> types.Task:
        """[GET] tasks/{task}
        
        Домашнее задание
        
        Параметры:
            task: task-id домашнего задания (не work-id!) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_Get
        """
        
        return self.get(f"tasks/{task}", model=types.Task)

    def get_lesson_tasks(self, lesson: str | int) -> list[types.Task]:
        """[GET] lessons/{lesson}/tasks
        
        Список Домашних заданий на урок
        
        Параметры:
            lesson: id урока (``str`` / ``int``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_GetByLesson
        """
        
        return self.get(f"lessons/{lesson}/tasks", model=types.Task, is_list=True)

    def get_work_tasks(self, work: str | int, persons: str | int | list[int | str]) -> list[types.Task]:
        """[GET] works/{work}/tasks
        
        Список Домашних заданий
        
        Параметры:
            work: id работы (homework) (``str`` / ``int``)
            persons: id (одно или несколько, обернутых в список) персоны (``int`` / ``str`` / ``list[str | int]``) (``"me"``, для текущего пользователя (можно и в списке указать))
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_GetByWork
        """
        
        return self.get(f"works/{work}/tasks{'?persons={}'.format(self.check_person(persons) if (isinstance(persons, int) or isinstance(persons, str)) else '&persons='.join([self.check_person(i) for i in persons]))}", model=types.Task, is_list=True)

    def get_undone_person_tasks(self, personId: str | int = "me") -> list[types.Task]:
        """[GET] persons/{personId}/undone
        
        Список невыполненных Домашних заданий
        обучающегося с истекшим сроком выполнения
        
        Параметры:
            personId: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_ListNotCompletedByPersonId
        """
        
        return self.get(f"persons/{self.check_person(personId)}/undone", model=types.Task, is_list=True)

    def get_person_tasks(self, person: str | int, subject: int | str, from_: datetime | date, to: datetime | date, pageNumber: int = None, pageSize: int = None) -> list[types.Task]:
        """[GET] persons{person}/tasks
        
        Список Домашних заданий ученика по предмету
        
        Параметры:
        person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
        subject: id предмета (``int`` / ``str``)
        from_: начало интервала дат (``datetime.datetime``)
        to: конец интервала дат (``datetime.datetime``)
        
        pageNumber: номер страницы (``int``) (``*optional*``)
        pageSize: размер страницы (``int``) (``*optional*``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_GetByPersonAndSubject
        """
        params = {
            "subject": str(subject),
            "from": self.datetime_to_string(from_),
            "to": self.datetime_to_string(to),
        }
        
        if pageNumber:
            params["pageNumber"] = str(pageNumber)
        
        if pageSize:
            params["pageSize"] = str(pageSize)
        
        return self.get(f"persons/{self.check_person(person)}/tasks", model=types.Task, is_list=True, params=params)

    def get_eduGroup_subjects(self, eduGroup: int | str) -> list[types.Subject]:
        """[GET] edu-groups/{eduGroup}/subjects

        Список предметов, преподаваемых в классе в текущем отчетном периоде

        Параметры:
            eduGroup: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Subjects/Subjects_GetByEduGroup
        """
        
        return self.get(f"edu-groups/{eduGroup}/subjects", model=types.Subject, is_list=True)

    def get_school_subjects(self, school: int | str) -> list[types.Subject]:
        """[GET] schools/{school}/subjects

        Список предметов, преподаваемых в образовательной организации в текущем учебном году
        
        Параметры:
            school: id школы (``int`` / ``str``)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Subjects/Subjects_GetSchoolSubjects
        """
        
        return self.get(f"schools/{school}/subjects", model=types.Subject, is_list=True)

    def get_school_parameters(self, school: int | str) -> types.SchoolParameters:
        """[GET] schools/{school}/parameters

        Параметры общеобразовательной организации 

        Параметры:
            school: id школы (``int`` / ``str``)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/SchoolsParameters/SchoolsParameters_Get
        """
        
        return self.get(f"schools/{school}/parameters", model=types.SchoolParameters)

    def get_school(self, school: int | str) -> types.School:
        """[GET] schools/{school}

        Профиль школы

        Параметры:
            school: id школы (``int`` / ``str``)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Schools/Schools_Get
        """
        
        return self.get(f"schools/{school}", model=types.School)

    def get_school_membership(self, school: int | str, schoolMembershipType: str = "Staff") -> list[types.Person]:
        """[GET] schools/{school}/membership

        Список профилей пользователей школы

        Параметры:
            school: id школы (``int`` / ``str``)
            schoolMembershipType: тип запрашиваемых пользователей (``"Staff" / "Admins"``) (``str``). По умолчанию стоит ``"Staff"``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Schools/Schools_GetSchoolMembership
        """
        
        return self.get(f"schools/{school}/membership?schoolMembershipType={schoolMembershipType}", model=types.Person, is_list=True)

    def get_person_schools(self, excludeOrganizations: bool = "") -> list[types.School]:
        """[GET] schools/person-schools

        Список образовательных организаций текущего пользователя

        Параметры:
            excludeOrganizations: - (``bool``)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Schools/Schools_GetPersonSchools
        """
        
        return self.get(
            "schools/person-schools".format(
                f"?excludeOrganizations={'true' if excludeOrganizations is True else 'false' if excludeOrganizations is False else ''}" if (
                    not isinstance(excludeOrganizations, str)
                    and excludeOrganizations in [True, False]) else ""
            ), model=types.School, is_list=True)

    def get_person_schedules(self, person: int | str, group: int | str, startDate: datetime | date, endDate: datetime | date) -> types.Schedule:
        """[GET] persons/{person}/groups/{group}/schedules
        
        Расписание ученика

        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            group: id учебной группы или класса (``int`` / ``str``) (``EduGroupID``)
            startDate: дата начала периода (``datetime.datetime``)
            endDate: дата завершения периода (``datetime.datetime``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Schedules/Schedules_GetByPersonAndPeriod
        """
        
        return self.get(f"persons/{self.check_person(person)}/groups/{group}/schedules?startDate={self.datetime_to_string(startDate)}&endDate={self.datetime_to_string(endDate)}", model=types.Schedule)

    def get_eduGroup_reporting_periods(self, eduGroup: int | str) -> list[types.ReportingPeriod]:
        """[GET] edu-groups/{eduGroup}/reporting-periods
        
        Список отчётных периодов для класса или учебной группы
        
        Параметры:
            eduGroup: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/ReportingPeriods/ReportingPeriods_GetByEduGroup
        """
        
        return self.get(f"edu-groups/{eduGroup}/reporting-periods", model=types.ReportingPeriod, is_list=True)

    def get_eduGroup_reporting_periods_all(self, eduGroup: int | str) -> types.ReportingPeriodEduGroup:
        """[GET] edu-groups/{eduGroup}/reporting-periods-group
        
        Группа отчётных периодов для класса или учебной группы
        
        Параметры:
            eduGroup: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/ReportingPeriods/ReportingPeriods_GetGroupReportingPeriodsGroup
        """
        
        return self.get(f"edu-groups/{eduGroup}/reporting-periods-group", model=types.ReportingPeriodEduGroup)

    def get_person(self, person: int | str = "me") -> types.Person:
        """[GET] persons/{person}
        
        Профиль персоны

        Параметры:
            person: id персоны (``"me"``, или пусто для текущего пользователя)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Persons/Persons_Get
        """
        
        self.me_person = self.get(f"persons/{self.check_person(person)}", model=types.Person)
        return self.me_person

    def get_eduGroup_students(self, eduGroup: int | str) -> list[types.Person]:
        """[GET] edu-groups/{eduGroup}/students
        
        Список учеников в классе или учебной группе 
        
        Параметры:
            eduGroup: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Persons/Persons_GetByEduGroup_0
        """
        
        return self.get(f"edu-groups/{eduGroup}/students", model=types.Person, is_list=True)
 
    def search_person(
        self,
        lastName: str = None,
        firstName: str = None,
        middleName: str = None,
        snils: str = None,
        birthday: date = None,
    ) -> None | list[types.Person]:
        """[GET] person/search
        
        Поиск персоны
        
        Параметры:
            lastName: Фамилия (``str``, ``*optional*``)
            firstName: Имя (``str``, ``*optional*``)
            middleName: Отчество (``str``, ``*optional*``)
            snils: СНИЛС (``str``, ``*optional*``)
            birthday: ДАТА РОЖДЕНИЯ (``datetime.date``, ``*optional*``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Persons/Persons_Search
        """
        params = {}
        
        if lastName:
            params["lastName"] = lastName
        
        if firstName:
            params["firstName"] = firstName
        
        if middleName:
            params["middleName"] = middleName
        
        if snils:
            params["snils"] = snils
        
        if birthday:
            params["birthday"] = self.date_to_string(birthday)

        return self.get("person/search", params=params, model=types.Person, is_list=True)
    
    def get_eduGroup_teachers(self, group: int | str) -> list[types.EduGroupTeacher]:
        """[GET] edu-groups/{group}/teachers

        Список учителей, которые ведут уроки в данной группе,
        учитываются уроки от недели назад и на 30 дней вперед
        
        Параметры:
            group: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Teacher/Teacher_GetEduGroupTeachers
        """
        
        return self.get(f'edu-groups/{group}/teachers', model=types.EduGroupTeacher, is_list=True)
    
    def get_school_teachers(self, school: int | str) -> list[types.SchoolTeacher]:
        """[GET] teacher/{teacher}/students

        Список преподавателей в выбранной образовательной организации
        
        Параметры:
            teacher: person-id учителя (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Teacher/Teacher_GetSchoolTeachers
        """
        
        return self.get(f'schools/{school}/teachers', model=types.SchoolTeacher, is_list=True)
    
    def get_teacher_students(self, teacher: int | str) -> list[types.TeacherStudent]:
        """[GET] teacher/{teacher}/students

        Список учеников для учителя который ведет уроки у этих учеников(они должны быть в расписании) от недели назад и на 30 дней вперед
        
        Параметры:
            teacher: person-id учителя (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Teacher/Teacher_GetStudentsByTeacher
        """
        
        return self.get(f'teacher/{teacher}/students', model=types.TeacherStudent, is_list=True)
    
    def get_eduGroup_timetable(self, eduGroup: int | str) -> types.TimeTable:
        """[GET] edu-groups/{eduGroup}/timetables

        Получение расписания учебной группы
        
        Параметры:
            eduGroup: id класса или учбеной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Timetables/Timetables_GetByEduGroup
        """
        
        return self.get(f'edu-groups/{eduGroup}/timetables', model=types.TimeTable)
    
    def get_school_timetable(self, school: int | str) -> types.TimeTable:
        """[GET] schools/{school}/timetables

        Получение расписания школы
        
        Параметры:
            school: id школы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Timetables/Timetables_GetBySchool
        """
        
        return self.get(f'schools/{school}/timetables', model=types.TimeTable)
    
    def get_user_feed(self, date: datetime | date, childPersonId: int | str = None, limit: int | str = None) -> types.UserFeed:
        """[GET] users/me/feed

        Лента пользователя
        
        Параметры:
            date: Дата начала временного интервала (``datetime.datetime``)
            childPersonId: id персоны ребёнка (``int`` | ``str``) (``optional``)
            limit: Ограничение временного интервала в днях (``int``) (``optional``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/UserFeeds/UserFeeds_GetUserFeed
        """
        params = {"date": self.datetime_to_string(date)}
        
        if childPersonId:
            params["childPersonId"] = childPersonId
        
        if limit:
            params["limit"] = limit
        
        return self.get('users/me/feed', model=types.UserFeed, params=params)
    
    def get_my_children_relatives(self) -> list[types.UserRelatives | None] | None:
        """[GET] users/me/childrenrelatives
        
        Список id всех родственных связей детей произвольного пользователя
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/UserRelatives/UserRelatives_GetOwnChildrenRelatives
        """
        
        return self.get(f"users/me/childrenrelatives", model=types.UserRelatives, is_list=True)
    
    def get_my_childrens(self) -> list[int | None] | None:
        """[GET] users/me/children
        
        Список id пользователей детей текущего пользователя
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/UserRelatives/UserRelatives_GetOwnChildren
        """
        
        return self.get(f"users/me/children", return_json=True)
    
    def get_user_relatives(self, user: str | int = "me") -> types.UserRelatives:
        """[GET] users/{user}/relatives | users/me/relatives
        
        Получение всех родственных связей произвольного/текущего пользователя.
        
        Параметры:
            user: id пользователя (``int`` / ``str``) (``"me"``, для текущего пользователя)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/UserRelatives/UserRelatives_GetRelatives
        """
        
        return self.get(f"users/{user}/relatives", model=types.UserRelatives)
    
    def get_user(self, user: str | int = "me") -> types.User:
        """[GET] users/{user} | users/me
        
        Профиль текущего пользователя (или по ID)
        
        Параметры:
            user: id пользователя (``int`` / ``str``) (``"me"``, для текущего пользователя)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Users/Users_Get
        """
        
        self.me_user = self.get(f"users/{user}", model=types.User)
        return self.me_user
    
    def get_user_roles(self, user: str | int = "me") -> list[int | None] | None:
        """[GET] users/{user}/roles | users/me/roles
        
        Профиль текущего пользователя (или по ID)
        
        Параметры:
            user: id пользователя (``int`` / ``str``) (``"me"``, для текущего пользователя)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Users/Users_Get
        """
        
        return self.get(f"users/{user}/roles", return_json=True)
    
    def get_weighted_average_marks(self, group: int | str, from_: datetime | date, to: datetime | date) -> types.WeightedAverageMarks:
        """[GET] edu-groups/{group}/wa-marks/{from_}/{to}

        Получить взвешенные оценки за период.
        
        Параметры:
            group: id класса или учебной группы (``int`` / ``str``) (``EduGroup``)
            from_: начало периода (``datetime.datetime``)
            to: конец периода (``datetime.datetime``)
        
        Права доступа: ``EducationalInfo``

        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/WeightedAverageMarks/WeightedAverageMarks_GetGroupAverageMarks
        """
        
        return self.get(f'edu-groups/{group}/wa-marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}', model=types.WeightedAverageMarks)
    
    def get_lesson_works(self, lesson: str | int) -> types.Work:
        """[GET] lessons/{lesson}/works

        Список работ на уроке
        
        Параметры:
            lesson: id урока (``str`` / ``int``)
        
        Права доступа: ``EducationalInfo``

        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Works/Works_GetByLesson_0
        """
        
        return self.get(f'lessons/{lesson}/works', model=types.Work, is_list=True)
    
    def get_work(self, work: str | int) -> types.Work:
        """[GET] works/{work}

        Работа на уроке по ID
        
        Параметры:
            work: id работы (``str`` / ``int``)
        
        Права доступа: ``EducationalInfo``

        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Works/Works_Get
        """
        
        return self.get(f'works/{work}', model=types.Work)
    
    def edit_homework_status(self, work: int | str, person: str | int = "me", change: dict[str, str] = {"action": "StartWorking"}):
        """[POST] works/{work}/persons/{person}/status

        Изменить статус выполнения домашней работы учащимся.
        
        Параметры:
            work: id урока (``int`` / ``str``)
            person: id персоны (``int`` / ``str``) (``"me"``, для себя)
            change: статус (``dict[str, str]``) : Пример -> ``{"action": "StartWorking"}``
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Works/Works_ChangeStatus
        """
        
        return self.post(f'works/{work}/persons/{self.check_person(person)}/status', return_json=True, data=change)
    
    def get_school_work_types(self, school: str | int) -> list[types.WorkType]:
        """[GET] work-types/{school}

        Получение списка всех типов работ школы
        
        Параметры:
            school: id школы (``str`` / ``int``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/WorkTypes/WorkTypes_Get
        """
        
        return self.get(f'work-types/{school}', model=types.WorkType, is_list=True)
