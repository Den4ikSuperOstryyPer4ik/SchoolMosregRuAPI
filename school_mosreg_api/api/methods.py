from datetime import date, datetime
from typing import Any, Optional, Union
from .base import BaseAPI
from .. import types

class SchoolMosregRUAPI(BaseAPI):
    """Основной sync класс почти со всеми функциями основного API.\n~~~"""

    def check_person(self, value):
        if value == "me":
            return (self.get_user()).personId
        else:
            return value
        
    def check_user(self, value):
        if value == "me":
            return (self.get_user()).id
        else:
            return value
    
    def get_me_organizations(self) -> Optional[list[int]]:
        """[GET] users/me/organizations
        
        Список идентификаторов организаций текущего пользователя
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Authorities/Authorities_GetOwnOrganizations
        """
        
        return self.get("v2/users/me/organizations", return_json=True)
    
    def get_organization(self, organizationId: Union[int, str]) -> types.Organization:
        """[GET] users/me/organizations/{organizationId}
        
        Данные указанной организации пользователя.
        
        Параметры:
            organizationId: Идентификатор организации (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Authorities/Authorities_GetOrganizationInfo
        """
        
        
        return self.get(f"v2/users/me/organizations/{organizationId}", model=types.Organization)
    
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
        
        return self.post("v2/authorizations", model=types.TokenWithCode, data={
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "refreshToken": refreshToken})
        
    def get_person_avg_marks(self, person: Union[int, str], period) -> Optional[str]:
        """[GET] persons/{person}/reporting-periods/{period}/avg-mark
        
        Оценка персоны за отчетный период
        
        Параметры:
            person: id персоны (``"me"``, для себя)
            period: id отчетного периода
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/AverageMarks/AverageMarks_GetByPersonAndPeriod
        """
        
        return self.get(f"v2/persons/{self.check_person(person)}/reporting-periods/{period}/avg-mark", return_json=True)
    
    def get_person_avg_marks_by_subject(self, person: Union[int, str], period, subject) -> Optional[str]:
        """[GET] persons/{person}/reporting-periods/{period}/subjects/{subject}/avg-mark
        
        Оценка персоны по предмету за отчетный период
        
        Параметры:
            person: id персоны (``"me"``, для себя)
            period: id отчетного периода
            subject: id предмета
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/AverageMarks/AverageMarks_GetByPersonAndPeriodAndSubject
        """
        
        return self.get(f"v2/persons/{self.check_person(person)}/reporting-periods/{period}/subjects/{subject}/avg-mark", return_json=True)
    
    def get_eduGroup_avg_marks_to_date(self, group: Union[int, str], period: Union[int, str], date: Union[datetime, date]) -> Optional[list[dict[str, Any]]]:
        """[GET] edu-groups/{group}/reporting-periods/{period}/avg-marks/{date}
        
        Оценки учебной группы по предмету за отчетный период до определенной даты
        
        Параметры:
            group: id учебной группы (``EduGroup``) (``int`` / ``str``)
            period: id отчетного периода (``int`` / ``str``)
            date: дата (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/AverageMarks/AverageMarks_GetByGroupAndPeriodOnDate
        """
        
        return self.get(f"v2/edu-groups/{group}/reporting-periods/{period}/avg-marks/{self.datetime_to_string(date)}", return_json=True)
    
    def get_eduGroup_avg_marks(self, group: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> Optional[list[dict[str, Any]]]:
        """[GET] edu-groups/{group}/avg-marks/{from}/{to}
        
        Оценки учебной группы за период
        
        Параметры:
            group: id учебной группы (``EduGroup``) (``int`` / ``str``)
            from_: id начало периода (``datetime.datetime`` / ``datetime.date``)
            to: id конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/AverageMarks/AverageMarks_ListByGroupAndDates
        """
        
        return self.get(f"v2/edu-groups/{group}/avg-marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", return_json=True)
    
    def get_user_childrens(self, userID: Union[int, str] = "me") -> Optional[list[types.Children]]:
        """[GET] user/{userID}/children
        
        Получение списка детей по идентификатору родительского пользователя
        
        Параметры:
            userID: 'id' пользователя (``str`` / ``int``) (``"me"``, для себя)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Children/Children_GetChildrenByUserID
        """
        
        return self.get(f"v2/user/{self.check_user(userID)}/children", model=types.Children, is_list=True)
    
    def get_person_childrens(self, personID: Union[int, str] = "me") -> list[types.Children]:
        """[GET] person/{personID}/children
        
        Получение списка детей по идентификатору родительской персоны
        
        Параметры:
            personID: 'id' пользователя (``str`` / ``int``) (``"me"``, для себя)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Children/Children_GetChildrenByPersonID
        """
        
        return self.get(f"v2/person/{self.check_person(personID)}/children", model=types.Children, is_list=True)
     
    def get_me_classmates(self) -> Optional[list[Optional[int]]]:
        """[GET] users/me/classmates
        
        Список id пользователей одноклассников текущего пользователя, если он является учеником,
        либо список активных участников образовательных групп пользователя во всех остальных случаях
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Classmates/Classmates_GetOwnClassmates
        """
        
        return self.get("v2/users/me/classmates", return_json=True)
    
    def get_context(self, userId: Union[int, str] = "me") -> types.Context:
        """[GET] users/{userId}/context | users/me/context
        
        Получение контекстной информации по пользователю
        
        Параметры:
            userId: id пользователя ("me" или оставьте пустым для себя) (int/str)
        
        Права доступа: ``CommonInfo``, ``FriendsAndRelatives``, ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Context
        """
        
        
        return self.get(f"v2/users/{userId}/context", model=types.Context)
    
    def get_user_school_memberships(self, user: Union[int, str] = "me") -> types.SchoolMemberships:
        """[GET] users/{user}/school-memberships
        
        Список участий в школах для произвольного пользователя
        
        Параметры:
            user: id пользователя (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetByUser
        """
        
        return self.get(f"v2/users/{user}/school-memberships", model=types.SchoolMemberships)
    
    def get_user_education(self, user: Union[int, str] = "me") -> types.SchoolMemberships:
        """[GET] users/{user}/education
        
        Список участий в школах для произвольного пользователя
        
        Параметры:
            user: id пользователя (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetByUser_0
        """
        
        return self.get(f"v2/users/{self.check_user(user)}/education", model=types.SchoolMemberships)
    
    def get_person_education(self, person: Union[int, str] = "me") -> list[types.SchoolMemberships]:
        """[GET] persons/{person}/school-memberships
        
        Список участий в школах для произвольного пользователя
        
        Параметры:
            person: id персоны (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetSchoolMembershipsByPerson
        """
        
        return self.get(f"v2/persons/{self.check_person(person)}/school-memberships", model=types.SchoolMemberships)
    
    def get_user_schools(self, user: Union[int, str] = "me") -> list[int] | None:
        """[GET] users/{user}/schools | users/me/schools
        
        Список идентификаторов школ произвольного/текущего пользователя
        
        Параметры:
            user: id пользователя (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetSchoolsByUser
        """
        
        return self.get(f"v2/users/{user}/schools", return_json=True)
    
    def get_user_eduGroups(self, user: Union[int, str] = "me") -> list[int] | None:
        """[GET] users/{user}/edu-groups | users/me/edu-groups
        
        Список идентификаторов классов произвольного/текущего пользователя
        
        Параметры:
            user: id пользователя (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EducationMemberships/EducationMemberships_GetEduGroupsByUser
        """
        
        return self.get(f"v2/users/{user}/edu-groups", return_json=True)
        
    def get_eduGroup(self, eduGroup: Union[int, str]) -> types.EduGroup:
        """[GET] edu-groups/{eduGroup}
        
        Класс или учебная группа
        
        Параметры:
            eduGroup: id класса или образовательной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_Get
        """
        
        return self.get(f"v2/edu-groups/{eduGroup}", model=types.EduGroup)
    
    def get_school_eduGroups(self, school: Union[int, str]) -> list[types.EduGroup]:
        """[GET] schools/{school}/edu-groups
        
        Список классов в школе
        
        Параметры:
            school: id школы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_GetBySchool
        """
        
        return self.get(f"v2/schools/{school}/edu-groups", model=types.EduGroup, is_list=True)
    
    def get_person_eduGroups(self, person: Union[int, str] = "me") -> list[types.EduGroup]:
        """[GET] persons/{person}/edu-groups
        
        Учебные группы персоны
        
        Параметры:
            person: id персоны (``"me"`` или оставьте пустым для себя) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_GetByPerson
        """
        
        return self.get(f"v2/persons/{self.check_person(person)}/edu-groups", model=types.EduGroup, is_list=True)
    
    def get_eduGroup_persons(self, eduGroup: Union[int, str]) -> list[types.Person] | None:
        """[GET] edu-groups/{eduGroup}/persons
        
        Список учеников учебной группы
        
        Параметры:
            eduGroup: id учебной группы (int/str)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_GetGroupPersons
        """
        
        return self.get(f"v2/edu-groups/{eduGroup}/persons", model=types.Person, is_list=True)
    
    def get_parallel_eduGroups(self, groupId: Union[int, str]) -> list[types.EduGroup]:
        """[GET] edu-groups/{groupId}/parallel
        
        Учебные группы персоны
        
        Параметры:
            person: id персоны (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/EduGroups/EduGroups_ListParallelGroups
        """
        
        return self.get(f"v2/edu-groups/{groupId}/parallel", model=types.EduGroup, is_list=True)

    def get_homeworks_by_period(self, school: Union[int, str], startDate: Union[datetime, date], endDate: Union[datetime, date]) -> types.HomeWork:
        """[GET] users/me/school/{school}/homeworks?startDate={startDate}&endDate={endDate}
        
        Получить домашние задания пользователя за период времени
        
        Параметры:
            school: id школы (``int`` / ``str``)
            startDate: дата начало периода (``datetime.datetime`` / ``datetime.date``)
            endDate: дата конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Homeworks/Homeworks_ListUserHomeworksByPeriod
        """
        
        return self.get(f"v2/users/me/school/{school}/homeworks?startDate={self.datetime_to_string(startDate)}&endDate={self.datetime_to_string(endDate)}", model=types.HomeWork)

    def get_homeworks_by_Ids(self, ids: Union[int, str] | list[Union[int, str]]) -> types.HomeWork:
        """[GET] users/me/school/homeworks?homeworkId={ids}
        
        Получить домашние задания по идентификаторам
        
        Параметры:
            ids: work-id домашнего задания (допускается лист) (``int`` / ``str`` / ``list[str / int]``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Homeworks/Homeworks_GetUserHomeworkByIds
        """
        
        return self.get(f"v2/users/me/school/homeworks?homeworkId={ids if (isinstance(ids, int) or isinstance(ids, str)) else '&homeworkId='.join(ids)}", model=types.HomeWork)

    def get_lesson_log_entries(self, lesson: Union[int, str]) -> list[types.LessonLogEntries] | None:
        """[GET] lessons/{lesson}/log-entries
        
        Список отметок о посещаемости на уроке
        
        Параметры:
            lesson: id урока (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/LessonLog/LessonLog_GetByLesson
        """
        
        return self.get(f"v2/lessons/{lesson}/log-entries", model=types.LessonLogEntries, is_list=True)
    
    def get_person_lesson_log_entries(self, lesson: Union[int, str], person: Union[int, str] = "me") -> types.LessonLogEntries:
        """[GET] lesson-log-entries/lesson/{lesson}/person/{person}
        
        Отметка о посещаемости ученика на уроке
        
        Параметры:
            lesson: id урока (int / str)
            person: id персоны ("me" или оставьте пустым для себя) (int/str)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/LessonLog/LessonLog_Get
        """
        
        return self.get(f"v2/lesson-log-entries/lesson/{lesson}/person/{self.check_person(person)}/edu-groups", model=types.LessonLogEntries)
    
    def get_eduGroup_lessons_log_entries(self, eduGroup: Union[int, str], subject: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.LessonLogEntries]:
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
        
        return self.get(f"v2/lesson-log-entries/group/{eduGroup}?subject={subject}&from={self.datetime_to_string(from_)}&to={self.datetime_to_string(to)}", model=types.LessonLogEntries, is_list=True)
    
    def get_person_lessons_log_entries_by_subject(self, personID: Union[int, str], subjectID: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.LessonLogEntries]:
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
        
        return self.get(f"v2/lesson-log-entries/person={self.check_person(personID)}&subject={subjectID}&from={self.datetime_to_string(from_)}&to={self.datetime_to_string(to)}", model=types.LessonLogEntries, is_list=True)
    
    def get_person_lessons_log_entries(self, person: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.LessonLogEntries]:
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
        
        return self.get(f"v2/persons/{self.check_person(person)}/lesson-log-entries&from={self.datetime_to_string(from_)}&to={self.datetime_to_string(to)}", model=types.LessonLogEntries, is_list=True)
    
    def get_lesson(self, lesson: Union[int, str]) -> types.Lesson:
        """[GET] lesssons/{lesson}
        
        Получить урок с заданным id
        
        Параметры:
            lesson: id урока (int / str)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Lessons/Lessons_Get
        """
        return self.get(f"v2/lessons/{lesson}", model=types.Lesson)
    
    def get_eduGroup_lesson_by_period(self, group: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.Lesson]:
        """[GET] edu-groups/{group}/lessons/{from_}/{to}
        
        Уроки группы за период
        
        Параметры:
            group: id класса или учебной группы (``str`` / ``int``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Lessons/Lessons_GetByGroupAndPeriod
        """
        return self.get(f"v2/edu-groups/{group}/lessons/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Lesson, is_list=True)
    
    def get_eduGroup_lesson_by_period_and_subject(self, group: Union[int, str], subject: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.Lesson]:
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
        return self.get(f"v2/edu-groups/{group}/subjects/{subject}/lessons/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Lesson, is_list=True)
    
    def get_work_marks_histogram(self, workID: Union[int, str]) -> types.MarksHistogram:
        """[GET] works/{workID}/marks/histogram
        
        Получение деперсонализированной гистограмы оценок всего класса по идентификатору работы
        
        Параметры:
            workID: id работы на уроке (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/MarkHistograms/MarkHistograms_GetMarksByWork
        """
        return self.get(f"v2/works/{workID}/marks/histogram", model=types.MarksHistogram)
        
    def get_marks_histogram_by_period(self, periodID: Union[int, str], subjectID: Union[int, str], groupID: Union[int, str]) -> types.MarksHistogramByPeriod:
        """[GET] periods/{periodID}/subjects/{subjectID}/groups/{groupID}/marks/histogram
        
        Получение деперсонализированной гистограмы оценок всего класса за отчетный период
        
        Параметры:
            periodID: id отчетного периода (``int`` / ``str``)
            subjectID: id предмета (``int`` / ``str``)
            groupID: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/MarkHistograms/MarkHistograms_GetMarksByPeriod
        """
        
        return self.get(f"v2/periods/{periodID}/subjects/{subjectID}/groups/{groupID}/marks/histogram", model=types.MarksHistogramByPeriod)
    
    def get_mark(self, mark: Union[int, str]) -> types.Mark:
        """[GET] marks/{mark}
        
        Оценка
        
        Параметры:
            mark: id оценки (не work-id!) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_Get
        """
        
        return self.get(f"v2/marks/{mark}", model=types.Mark)

    def get_work_marks(self, work: Union[int, str]) -> list[types.Mark]:
        """[GET] works/{work}/marks
        
        Список оценок за определенную работу на уроке
        
        Параметры:
            work: id работы (не mark-id или lesson-id!) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByWork
        """
        
        return self.get(f"v2/works/{work}/marks", model=types.Mark, is_list=True)

    def get_lesson_marks(self, lesson: Union[int, str]) -> list[types.Mark]:
        """[GET] lessons/{lesson}/marks
        
        Оценки на уроке
        
        Параметры:
            lessson: id урока (не mark-id или work-id!) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByLesson
        """
        
        return self.get(f"v2/lessons/{lesson}/marks", model=types.Mark, is_list=True)
    
    def get_eduGroup_marks(self, group: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.Mark]:
        """[GET] edu-groups/{group}/marks/{from_}/{to}
        
        Оценки учебной группы за период
        
        Параметры:
            group: id учебной группы или класса (``int`` / ``str``)
            from_: начало периода (``datetime.datetime`` / ``datetime.date``)
            to: конец периода (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByGroup
        """
        
        return self.get(f"v2/edu-groups/{group}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_eduGroup_marks_by_subject(self, group: Union[int, str], subject: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.Mark]:
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
        
        return self.get(f"v2/edu-groups/{group}/subjects/{subject}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_person_marks_in_school(self, person: Union[int, str], school: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.Mark]:
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
        
        return self.get(f"v2/persons/{self.check_person(person)}/schools/{school}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_person_marks_in_eduGroup(self, person: Union[int, str], group: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.Mark]:
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
        
        return self.get(f"v2/persons/{self.check_person(person)}/edu-groups/{group}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_person_marks_on_lesson(self, person: Union[int, str], lesson: Union[int, str]) -> list[types.Mark]:
        """[GET] persons/{person}/lessons/{lesson}/marks
        
        Оценки персоны за урок
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            lesson: id урока (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByLessonAndPerson
        """
        
        return self.get(f"v2/persons/{self.check_person(person)}/lessons/{lesson}/marks", model=types.Mark, is_list=True)
    
    def get_person_marks_on_work(self, person: Union[int, str], work: Union[int, str]) -> list[types.Mark]:
        """[GET] persons/{person}/lessons/{lesson}/marks
        
        Оценки персоны за работу
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            work: id работы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByWorkAndPerson
        """
        
        return self.get(f"v2/persons/{self.check_person(person)}/works/{work}/marks", model=types.Mark, is_list=True)
    
    def get_person_marks_by_subject(self, person: Union[int, str], subject: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> list[types.Mark]:
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
        
        return self.get(f"v2/persons/{person}/subjects/{subject}/marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}", model=types.Mark, is_list=True)
    
    def get_person_marks_on_lesson_by_date(self, person: Union[int, str], date: Union[datetime, date]) -> list[types.Mark]:
        """[GET] lessons/{date}/persons/{person}/marks
        
        Оценки персоны по дате урока
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            date: дата урока (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByPersonAndLessonDate
        """
        
        return self.get(f"v2/lessons/{date}/persons/{self.check_person(person)}/marks", model=types.Mark, is_list=True)
    
    def get_person_marks_by_date(self, person: Union[int, str], date: Union[datetime, date]) -> list[types.Mark]:
        """[GET] persons/{person}/marks/{date}
        
        Оценки персоны по дате выставления оценки
        
        Параметры:
            person: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
            date: дата выставления оценки (``datetime.datetime`` / ``datetime.date``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Marks/Marks_GetByPersonAndMarkDate
        """
        
        return self.get(f"v2/persons/{self.check_person(person)}/marks/{date}", model=types.Mark, is_list=True)
    
    def get_marks_values(self) -> dict[str, list[str | None]]:
        """[GET] marks/values
        
        Метод возвращает все поддерживаемые системы (типы) оценок и все возможные оценки в каждой из систем.\n
        Например, для системы "mark5" возвращается массив из следующих оценок:
        "mark5" : ["1-","1","1+","2-","2","2+","3-","3","3+","4-","4","4+","5-","5","5+"]
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/MarkValues/MarkValues_GetAll
        """

        return self.get("v2/marks/values", return_json=True)
    
    def get_marks_values_by_type(self, type: str) -> list[str]:
        """[GET] marks/values/type/{type}
        
        Метод возвращает все возможные оценки в запрашиваемой системе (типе) оценок.\n
        Чтобы узнать, какие типы поддерживаются нужно предварительно делать запрос marks/values без параметров.\n
        Например, для запроса marks/values/type/mark5 ответом
        будет list["1-", "1", "1+", "2-", "2", "2+", "3-", "3", "3+", "4-", "4", "4+", "5-", "5", "5+"].
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/MarkValues/MarkValues_GetByType
        """

        return self.get(f"v2/marks/values/type/{type}", return_json=True)
    
    def get_recent_marks(self, person: Union[int, str], group: Union[int, str], fromDate: Union[datetime, date] = None, subject: Optional[Union[int, str]] = None, limit: int = 10) -> types.RecentMarks:
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
        
        return self.get(f"v2/persons/{self.check_person(person)}/group/{group}/recentmarks", params=params, model=types.RecentMarks)
    
    def get_task(self, task: Union[int, str]) -> types.Task:
        """[GET] tasks/{task}
        
        Домашнее задание
        
        Параметры:
            task: task-id домашнего задания (не work-id!) (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_Get
        """
        
        return self.get(f"v2/tasks/{task}", model=types.Task)

    def get_lesson_tasks(self, lesson: Union[int, str]) -> list[types.Task]:
        """[GET] lessons/{lesson}/tasks
        
        Список Домашних заданий на урок
        
        Параметры:
            lesson: id урока (``str`` / ``int``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_GetByLesson
        """
        
        return self.get(f"v2/lessons/{lesson}/tasks", model=types.Task, is_list=True)

    def get_work_tasks(self, work: Union[int, str], persons: Union[int, str] | list[Union[int, str]]) -> list[types.Task]:
        """[GET] works/{work}/tasks
        
        Список Домашних заданий
        
        Параметры:
            work: id работы (homework) (``str`` / ``int``)
            persons: id (одно или несколько, обернутых в список) персоны (``int`` / ``str`` / ``list[Union[int, str]]``) (``"me"``, для текущего пользователя (можно и в списке указать))
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_GetByWork
        """
        
        return self.get(f"v2/works/{work}/tasks{'?persons={}'.format(self.check_person(persons) if (isinstance(persons, int) or isinstance(persons, str)) else '&persons='.join([self.check_person(i) for i in persons]))}", model=types.Task, is_list=True)

    def get_undone_person_tasks(self, personId: Union[int, str] = "me") -> list[types.Task]:
        """[GET] persons/{personId}/undone
        
        Список невыполненных Домашних заданий
        обучающегося с истекшим сроком выполнения
        
        Параметры:
            personId: id персоны (``int`` / ``str``) (``"me"``, для текущего пользователя)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Tasks/Tasks_ListNotCompletedByPersonId
        """
        
        return self.get(f"v2/persons/{self.check_person(personId)}/undone", model=types.Task, is_list=True)

    def get_person_tasks(self, person: Union[int, str], subject: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date], pageNumber: int = None, pageSize: int = None) -> list[types.Task]:
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
        
        return self.get(f"v2/persons/{self.check_person(person)}/tasks", model=types.Task, is_list=True, params=params)

    def get_eduGroup_subjects(self, eduGroup: Union[int, str]) -> list[types.Subject]:
        """[GET] edu-groups/{eduGroup}/subjects

        Список предметов, преподаваемых в классе в текущем отчетном периоде

        Параметры:
            eduGroup: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Subjects/Subjects_GetByEduGroup
        """
        
        return self.get(f"v2/edu-groups/{eduGroup}/subjects", model=types.Subject, is_list=True)

    def get_school_subjects(self, school: Union[int, str]) -> list[types.Subject]:
        """[GET] schools/{school}/subjects

        Список предметов, преподаваемых в образовательной организации в текущем учебном году
        
        Параметры:
            school: id школы (``int`` / ``str``)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Subjects/Subjects_GetSchoolSubjects
        """
        
        return self.get(f"v2/schools/{school}/subjects", model=types.Subject, is_list=True)

    def get_school_parameters(self, school: Union[int, str]) -> types.SchoolParameters:
        """[GET] schools/{school}/parameters

        Параметры общеобразовательной организации 

        Параметры:
            school: id школы (``int`` / ``str``)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/SchoolsParameters/SchoolsParameters_Get
        """
        
        return self.get(f"v2/schools/{school}/parameters", model=types.SchoolParameters)

    def get_school(self, school: Union[int, str]) -> types.School:
        """[GET] schools/{school}

        Профиль школы

        Параметры:
            school: id школы (``int`` / ``str``)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Schools/Schools_Get
        """
        
        return self.get(f"v2/schools/{school}", model=types.School)

    def get_school_membership(self, school: Union[int, str], schoolMembershipType: str = "Staff") -> list[types.Person]:
        """[GET] schools/{school}/membership

        Список профилей пользователей школы

        Параметры:
            school: id школы (``int`` / ``str``)
            schoolMembershipType: тип запрашиваемых пользователей (``"Staff" / "Admins"``) (``str``). По умолчанию стоит ``"Staff"``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Schools/Schools_GetSchoolMembership
        """
        
        return self.get(f"v2/schools/{school}/membership?schoolMembershipType={schoolMembershipType}", model=types.Person, is_list=True)

    def get_person_schools(self, excludeOrganizations: bool = "") -> list[types.School]:
        """[GET] schools/person-schools

        Список образовательных организаций текущего пользователя

        Параметры:
            excludeOrganizations: - (``bool``)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Schools/Schools_GetPersonSchools
        """
        
        return self.get("v2/schools/person-schools" + ("" if excludeOrganizations == "" else "?excludeOrganizations={}".format('true' if excludeOrganizations else 'false')), model=types.School, is_list=True)

    def get_person_schedules(self, person: Union[int, str], group: Union[int, str], startDate: Union[datetime, date], endDate: Union[datetime, date]) -> types.Schedule:
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
        
        return self.get(f"v2/persons/{self.check_person(person)}/groups/{group}/schedules?startDate={self.datetime_to_string(startDate)}&endDate={self.datetime_to_string(endDate)}", model=types.Schedule)

    def get_eduGroup_reporting_periods(self, eduGroup: Union[int, str]) -> list[types.ReportingPeriod]:
        """[GET] edu-groups/{eduGroup}/reporting-periods
        
        Список отчётных периодов для класса или учебной группы
        
        Параметры:
            eduGroup: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/ReportingPeriods/ReportingPeriods_GetByEduGroup
        """
        
        return self.get(f"v2/edu-groups/{eduGroup}/reporting-periods", model=types.ReportingPeriod, is_list=True)

    def get_eduGroup_reporting_periods_all(self, eduGroup: Union[int, str]) -> types.ReportingPeriodEduGroup:
        """[GET] edu-groups/{eduGroup}/reporting-periods-group
        
        Группа отчётных периодов для класса или учебной группы
        
        Параметры:
            eduGroup: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/ReportingPeriods/ReportingPeriods_GetGroupReportingPeriodsGroup
        """
        
        return self.get(f"v2/edu-groups/{eduGroup}/reporting-periods-group", model=types.ReportingPeriodEduGroup)

    def get_person(self, person: Union[int, str] = "me") -> types.Person:
        """[GET] persons/{person}
        
        Профиль персоны

        Параметры:
            person: id персоны (``"me"``, или пусто для текущего пользователя)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Persons/Persons_Get
        """
        
        return self.get(f"v2/persons/{self.check_person(person)}", model=types.Person)

    def get_eduGroup_students(self, eduGroup: Union[int, str]) -> list[types.Person]:
        """[GET] edu-groups/{eduGroup}/students
        
        Список учеников в классе или учебной группе 
        
        Параметры:
            eduGroup: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Persons/Persons_GetByEduGroup_0
        """
        
        return self.get(f"v2/edu-groups/{eduGroup}/students", model=types.Person, is_list=True)
 
    def search_person(
        self,
        lastName: Optional[str] = None,
        firstName: Optional[str] = None,
        middleName: Optional[str] = None,
        snils: Optional[str] = None,
        birthday: Optional[date] = None,
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

        return self.get("v2/person/search", params=params, model=types.Person, is_list=True)
    
    def get_eduGroup_teachers(self, group: Union[int, str]) -> list[types.EduGroupTeacher]:
        """[GET] edu-groups/{group}/teachers

        Список учителей, которые ведут уроки в данной группе,
        учитываются уроки от недели назад и на 30 дней вперед
        
        Параметры:
            group: id класса или учебной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Teacher/Teacher_GetEduGroupTeachers
        """
        
        return self.get(f'v2/edu-groups/{group}/teachers', model=types.EduGroupTeacher, is_list=True)
    
    def get_school_teachers(self, school: Union[int, str]) -> list[types.SchoolTeacher]:
        """[GET] teacher/{teacher}/students

        Список преподавателей в выбранной образовательной организации
        
        Параметры:
            teacher: person-id учителя (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Teacher/Teacher_GetSchoolTeachers
        """
        
        return self.get(f'v2/schools/{school}/teachers', model=types.SchoolTeacher, is_list=True)
    
    def get_teacher_students(self, teacher: Union[int, str]) -> list[types.TeacherStudent]:
        """[GET] teacher/{teacher}/students

        Список учеников для учителя который ведет уроки у этих учеников(они должны быть в расписании) от недели назад и на 30 дней вперед
        
        Параметры:
            teacher: person-id учителя (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Teacher/Teacher_GetStudentsByTeacher
        """
        
        return self.get(f'v2/teacher/{teacher}/students', model=types.TeacherStudent, is_list=True)
    
    def get_eduGroup_timetable(self, eduGroup: Union[int, str]) -> types.TimeTable:
        """[GET] edu-groups/{eduGroup}/timetables

        Получение расписания учебной группы
        
        Параметры:
            eduGroup: id класса или учбеной группы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Timetables/Timetables_GetByEduGroup
        """
        
        return self.get(f'v2/edu-groups/{eduGroup}/timetables', model=types.TimeTable)
    
    def get_school_timetable(self, school: Union[int, str]) -> types.TimeTable:
        """[GET] schools/{school}/timetables

        Получение расписания школы
        
        Параметры:
            school: id школы (``int`` / ``str``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Timetables/Timetables_GetBySchool
        """
        
        return self.get(f'v2/schools/{school}/timetables', model=types.TimeTable)
    
    def get_user_feed(self, date: Union[datetime, date], childPersonId: Optional[Union[int, str]] = None, limit: Optional[Union[int, str]] = None) -> types.UserFeed:
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
        
        return self.get(f"v2/users/me/childrenrelatives", model=types.UserRelatives, is_list=True)
    
    def get_my_childrens(self) -> list[int | None] | None:
        """[GET] users/me/children
        
        Список id пользователей детей текущего пользователя
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/UserRelatives/UserRelatives_GetOwnChildren
        """
        
        return self.get(f"v2/users/me/children", return_json=True)
    
    def get_user_relatives(self, user: Union[int, str] = "me") -> types.UserRelatives:
        """[GET] users/{user}/relatives | users/me/relatives
        
        Получение всех родственных связей произвольного/текущего пользователя.
        
        Параметры:
            user: id пользователя (``int`` / ``str``) (``"me"``, для текущего пользователя)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/UserRelatives/UserRelatives_GetRelatives
        """
        
        return self.get(f"v2/users/{user}/relatives", model=types.UserRelatives)
    
    def get_user(self, user: Union[int, str] = "me") -> types.User:
        """[GET] users/{user} | users/me
        
        Профиль текущего пользователя (или по ID)
        
        Параметры:
            user: id пользователя (``int`` / ``str``) (``"me"``, для текущего пользователя)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Users/Users_Get
        """
        
        return self.get(f"v2/users/{user}", model=types.User)
    
    def get_user_roles(self, user: Union[int, str] = "me") -> list[int | None] | None:
        """[GET] users/{user}/roles | users/me/roles
        
        Профиль текущего пользователя (или по ID)
        
        Параметры:
            user: id пользователя (``int`` / ``str``) (``"me"``, для текущего пользователя)
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Users/Users_Get
        """
        
        return self.get(f"v2/users/{user}/roles", return_json=True)
    
    def get_weighted_average_marks(self, group: Union[int, str], from_: Union[datetime, date], to: Union[datetime, date]) -> types.WeightedAverageMarks:
        """[GET] edu-groups/{group}/wa-marks/{from_}/{to}

        Получить взвешенные оценки за период.
        
        Параметры:
            group: id класса или учебной группы (``int`` / ``str``) (``EduGroup``)
            from_: начало периода (``datetime.datetime``)
            to: конец периода (``datetime.datetime``)
        
        Права доступа: ``EducationalInfo``

        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/WeightedAverageMarks/WeightedAverageMarks_GetGroupAverageMarks
        """
        
        return self.get(f'v2/edu-groups/{group}/wa-marks/{self.datetime_to_string(from_)}/{self.datetime_to_string(to)}', model=types.WeightedAverageMarks)
    
    def get_lesson_works(self, lesson: Union[int, str]) -> types.Work:
        """[GET] lessons/{lesson}/works

        Список работ на уроке
        
        Параметры:
            lesson: id урока (``str`` / ``int``)
        
        Права доступа: ``EducationalInfo``

        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Works/Works_GetByLesson_0
        """
        
        return self.get(f'v2/lessons/{lesson}/works', model=types.Work, is_list=True)
    
    def get_work(self, work: Union[int, str]) -> types.Work:
        """[GET] works/{work}

        Работа на уроке по ID
        
        Параметры:
            work: id работы (``str`` / ``int``)
        
        Права доступа: ``EducationalInfo``

        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Works/Works_Get
        """
        
        return self.get(f'v2/works/{work}', model=types.Work)
    
    def edit_homework_status(self, work: Union[int, str], person: Union[int, str] = "me", change: dict[str, str] = {"action": "StartWorking"}):
        """[POST] works/{work}/persons/{person}/status

        Изменить статус выполнения домашней работы учащимся.
        
        Параметры:
            work: id урока (``int`` / ``str``)
            person: id персоны (``int`` / ``str``) (``"me"``, для себя)
            change: статус (``dict[str, str]``) : Пример -> ``{"action": "StartWorking"}``
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/Works/Works_ChangeStatus
        """
        
        return self.post(f'v2/works/{work}/persons/{self.check_person(person)}/status', return_json=True, data=change)
    
    def get_school_work_types(self, school: Union[int, str]) -> list[types.WorkType]:
        """[GET] work-types/{school}

        Получение списка всех типов работ школы
        
        Параметры:
            school: id школы (``str`` / ``int``)
        
        Права доступа: ``EducationalInfo``
        
        Docs: https://api.school.mosreg.ru/partners/swagger/ui/index#!/WorkTypes/WorkTypes_Get
        """
        
        return self.get(f'v2/work-types/{school}', model=types.WorkType, is_list=True)
