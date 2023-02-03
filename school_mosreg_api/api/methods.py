from .base import BaseAPI
from school_mosreg_api import types

class SchoolMosregRUAPI(BaseAPI):
    def get_user_schools(self) -> list[types.School]:
        return self.get("schools/person-schools", model=types.School, is_list=True)

    def get_me(self):
        return self.get("users/me", model=types.User)

    def get_me_classmates(self) -> list[int] | None:
        return self.get("users/me/classmates", return_json=True)

    def get_me_context(self) -> types.Context:
        return self.get(f"users/me/context", model=types.Context)

    def get_user_context(self, user_id: int) -> types.Context:
        return self.get(f"users/{user_id}/context", model=types.Context)

    def get_user_memberships(self, user_id: int) -> types.SchoolMemberships:
        return self.get(f"users/{user_id}/school-memberships", model=types.SchoolMemberships)
    
    def get_me_school(self, educationType: str | None = "Regular"):
        schools: list[types.School] = self.get("schools/person-schools", model=types.School, is_list=True)
        
        for school in schools:
            if school.educationType == educationType:
                return school.id
        
        return None
    
    def get_school_work_types(self, school: int = None) -> list[types.WorkType]:
        return self.get(
            f"work-types/{school or self.get_me_school()}",
            model=types.WorkType, is_list=True
        )
    
    def get_lesson_works(self, lesson: int) -> list[types.Work]:
        return self.get(f'lessons/{lesson}/works', model=types.Work, is_list=True)
    
    def get_school_subjects(self, school: int = None) -> list[types.Subject]:
        return self.get(
            f"schools/{school or self.get_me_school()}/subjects",
            model=types.Subject, is_list=True
        )

    def get_eduGroup_subjects(self, user_id: int, eduGroup: int | str) -> list[types.Subject]:
        return self.get(f"edu-groups/{eduGroup}/subjects", model=types.Subject, is_list=True)
    
    def get_person(self, person: int) -> types.Person:
        return self.get(f"persons/{person}", model=types.Person)
    
    def get_me_person_id(self) -> int:
        return self.get_me().personId
    
    def get_edu_group(self, type: str = "Group"):
        person_id = self.get_me_person_id()
        api_result: list[types.EduGroup] = self.get(f"persons/{person_id}/edu-groups", model=types.EduGroup, is_list=True)
        for group in api_result:
            if group.type == type:
                return group.id
        
        return None
    
    
    
    
    
    
    