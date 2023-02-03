from .base import AsyncBaseAPI
from school_mosreg_api import types

class AsyncSchoolMosregRUAPI(AsyncBaseAPI):
    async def get_user_schools(self) -> list[types.School]:
        return await self.get("schools/person-schools", model=types.School, is_list=True)

    async def get_me(self) -> types.User:
        return await self.get("users/me", model=types.User)

    async def get_me_classmates(self) -> list[int] | None:
        return await self.get("users/me/classmates", return_json=True)

    async def get_me_context(self) -> types.Context:
        return await self.get(f"users/me/context", model=types.Context)

    async def get_user_context(self, user_id: int) -> types.Context:
        return await self.get(f"users/{user_id}/context", model=types.Context)

    async def get_user_memberships(self, user_id: int) -> types.SchoolMemberships:
        return await self.get(f"users/{user_id}/school-memberships", model=types.SchoolMemberships)
    
    async def get_me_school(self, educationType: str | None = "Regular"):
        schools: list[types.School] = await self.get("schools/person-schools", model=types.School, is_list=True)
        
        for school in schools:
            if school.educationType == educationType:
                return school.id
        
        return None

    async def get_school_work_types(self, school: int = None) -> list[types.WorkType]:
        return await self.get(
            f"work-types/{school or await self.get_me_school()}",
            model=types.WorkType, is_list=True
        )
    
    async def get_lesson_works(self, lesson: int) -> list[types.Work]:
        return await self.get(f'lessons/{lesson}/works', model=types.Work, is_list=True)
    
    async def get_school_subjects(self, school: int = None) -> list[types.Subject]:
        return await self.get(
            f"schools/{school or await self.get_me_school()}/subjects",
            model=types.Subject, is_list=True
        )

    async def get_eduGroup_subjects(self, eduGroup: int | str) -> list[types.Subject]:
        return await self.get(f"edu-groups/{eduGroup}/subjects", model=types.Subject, is_list=True)
    
    async def get_person(self, person: int) -> types.Person:
        return await self.get(f"persons/{person}", model=types.Person)
    
    async def get_me_person_id(self) -> int:
        return await self.get_me().personId
    
    async def get_edu_group(self, type: str = "Group"):
        person_id = await self.get_me_person_id()
        api_result: list[types.EduGroup] = await self.get(f"persons/{person_id}/edu-groups", model=types.EduGroup, is_list=True)
        for group in api_result:
            if group.type == type:
                return group.id
        
        return None
    