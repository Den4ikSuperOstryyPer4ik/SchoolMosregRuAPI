from io import BufferedIOBase, BufferedRandom, BufferedReader
from typing import Optional, Union

from .base import AsyncBaseAPI
from .. import types


class AsyncSchoolMosregMobileAPI(AsyncBaseAPI):
    """Основной Async класс с функциями mobile API.\n~~~"""
    
    def __init__(self, token: Optional[str] = None) -> None:
        self.token = token
        self.UserAgentDict = {
            "User-Agent": self.get_random_UserAgent()
        }
    
    BASIC_SCOPE = "CommonInfo,EducationalInfo,Schools,Relatives,EduGroups,Lessons,marks,EduWorks,Avatar"
    BASIC_CLIENT_ID = "594df05c-fea3-4e66-9949-60ae72a2150d"
    BASIC_CLIENT_SECRET = "2436e132-8103-417b-ab63-5e89dcf6fba9"
    
    @staticmethod
    def auth_data(login: str, password: str, clientId: str = BASIC_CLIENT_ID, clientSecret: str = BASIC_CLIENT_SECRET, scope: str = BASIC_SCOPE):
        return types.AuthData(username=login, password=password, clientId=clientId, clientSecret=clientSecret, scope=scope)
    
    def login_data(self, login: str, old_password: str, new_password: str, email: str, phone: Optional[str] = None, token: Optional[str] = None, clientId: str = BASIC_CLIENT_ID, clientSecret: str = BASIC_CLIENT_SECRET, scope: str = BASIC_SCOPE):
        return types.LoginData(
            agreeTerms=True,
            email=email,
            username=login,
            newPassword=new_password,
            newPasswordRepeat=new_password,
            password=old_password,
            passwordRepeat=old_password,
            phone=phone,
            clientId=clientId,
            clientSecret=clientSecret,
            scope=scope,
            token=(self.token if not token else token) or "",
        )
    
    @staticmethod
    def _method(method):
        return "mobile/v6.0/" + method
    
    METHODS = {
        "person-activation": _method("persons/{personId}/activation"),
        "addZone": _method("tracker/users/{userId}/children/{childPersonId}/zones"),
        "authorizationEsiaInfo": _method("authorizations/esia/"),
        "changePassword": _method("persons/{personId}/password"),
        "deleteAttachment": _method("persons/{personId}/groups/{groupId}/lessons/{lessonId}/files/{fileId}/delete"),
        "deleteZone": _method("tracker/users/{userId}/children/{childPersonId}/zones/{zoneId}/delete"),
        "getAdsCommentsList": _method("thread/{event_key}"),
        "getAdsList": _method("persons/{personId}/schools/{schoolId}/notifications"),
        "getAvailableEsiaRegions": _method("authorizations/esia/regions"),
        "getChatCloseContacts": _method("chat/closecontacts"),
        "getChatContacts": _method("chat/contactlist"),
        "getChatContext": _method("chat/context"),
        "getChatCredentials": _method("chat/credentials"),
        "getChats": _method("chat/contacts/enrich"),
        "getCommentCommentsList": _method("thread/{event_key}/comment/{parentCommentId}"),
        "getEsiaTaskStaus": "task/status",
        "getFinalGrades": _method("persons/{personId}/groups/{groupId}/finalMarks"),
        "getPersonMarks": _method("persons/{personId}/groups/{groupId}/periods/{periodId}/periodMarks"),
        "getPushSettings": _method("users/{userId}/pushNotifications/settings"),
        "getRating": _method("persons/{personId}/groups/{groupId}/rating"),
        "getSubjectDetails": _method("persons/{personId}/groups/{groupId}/subjects/{subjectId}/periods/{periodId}/subjectDetails"),
        "getLessonDetails": _method("persons/{personId}/groups/{groupId}/lessons/{lessonId}/lessonDetails"),
        "getMarksDetails": _method("persons/{personId}/groups/{groupId}/marks/{markId}/markDetails"),
        "getSubscriptionInfo": _method("users/{userId}/subscription/info"),
        "getUserAvatar": _method("users/{userId}/avatar"),
        "getUserContext": _method("users/{userId}/context"),
        "getUserDayBook": _method("persons/{personId}/schools/{schoolId}/groups/{groupId}/diary"),
        "getUserFeed": _method("persons/{personId}/groups/{groupId}/important"),
        "login": _method("authorizations/bycredentials"),
        "uploadAttachment": _method("persons/{personId}/groups/{groupId}/lessons/{lessonId}/file"),
        "uploadAvatar": _method("users/{userId}/avatars"),
        "auth": _method("authorizations/byCredentials")
    }
    
    def method(self, name: str, *args, **kwargs):
        return self.METHODS.get(name, "").format(*args, **kwargs)
    
    async def activate_person(self, personId: Union[int, str], loginData: types.LoginData) -> types.LoginResponse:
        """Activate [POST]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `loginData` (``types.LoginData``)
        
        :return: `types.LoginResponse`
        """
        return await self.post(self.method("person-activation", personId=personId), json=loginData.dict(), model=types.LoginResponse, required_token=False) 
    
    async def add_zone(self, userId: Union[int, str], childPersonId: Union[int, str], zone: types.Zone) -> types.CreateZoneResponse:
        """Add Zone [POST]
        ~~~
        
        :param: `userId` (``int``)
        :param: `childPersonId` (``int``)
        :param: `zone` (``types.Zone``)
        
        :return: ``types.CreateZoneResponse``
        """
        return await self.post(self.method("addZone", userId=userId, childPersonId=childPersonId), json=zone.dict(), model=types.CreateZoneResponse) 
    
    async def authorization_esiaInfo(self, esiaCredentials: dict[str, Union[int, str]]) -> types.AuthorizationEsiaInfo:
        """AuthorizationEsiaInfo [POST]
        ~~~
        
        :param: `esiaCredentials` (``dict[str, int/str]``) example:
        
        `{`
            `"taskId": "str",`
            `"userId": int,`
            `"regionId": int,`
            `"clientId": "str",`
            `"clientSecret": "str",`
            `"scope": "str"`
        `}`
        
        :return: `types.AuthorizationEsiaInfo`
        """
        return await self.post(self.method("authorizationEsiaInfo"), json=esiaCredentials, model=types.AuthorizationEsiaInfo, required_token=False) 

    async def change_password(self, personId: Union[int, str], loginData: types.LoginData) -> types.LoginResponse:
        """Change Password [POST]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `loginData` (``types.LoginData``)
        
        :return: `types.LoginResponse`
        """
        return await self.post(self.method("changePassword", personId=personId), json=loginData.dict(), model=types.LoginResponse, required_token=False) 
    
    async def delete_attachment(self, personId: Union[int, str], groupId: Union[int, str], lessonId: Union[int, str], fileId: str) -> types.TypeMobile:
        """DeleteAttachment [POST]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        :param: `lessonId` (``int`` | ``str``)
        :param: `fileId` (``str``)
        
        :return: `types.TypeMobile`
        """
        return await self.post(self.method("deleteAttachment", personId=personId, groupId=groupId, lessonId=lessonId, fileId=fileId), model=types.TypeMobile) 
    
    async def delete_zone(self, userId: Union[int, str], childPersonId: Union[int, str], zoneId: Union[int, str]) -> types.TypeMobile:
        """Delete Person Zone [POST]
        ~~~
        
        :param: `userId` (``int`` | ``str``)
        :param: `childPersonId` (``int`` | ``str``)
        :param: `zoneId` (``int`` | ``str``)
        
        :return: `types.TypeMobile`
        """
        return await self.post(self.method("deleteZone", userId=userId, childPersonId=childPersonId, zoneId=zoneId), model=types.TypeMobile) 

    async def get_ads_comments_list(self, event_key: str, fromCommentId: Optional[str] = None, limit: Optional[int] = None) -> types.PostCommentsResponse:
        """GetAdsCommentsList [GET]
        ~~~
        
        :param: `event_key` (``str``)
        :param: `fromCommentId` (``str``, ``*optional*``)
        :param: `limit` (``int``, ``*optional*``)
        
        :return: `types.PostCommentResponse`
        """
        return await self.get(self.method("getAdsCommentsList", event_key=event_key), model=types.PostCommentsResponse, params={ 
            **({} if not fromCommentId else {"fromCommentId": fromCommentId}),
            **({} if not limit else {"limit": str(limit)})
        })

    async def get_school_notifications(self, personId: Union[int, str], schoolId: Union[int, str]) -> types.PostsResponse:
        """GetAdsList (Get School Notifications) [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `schoolId` (``int`` | ``str``)
        
        :return: `types.PostsResponse`
        """
        return await self.get(self.method("getAdsList", personId=personId, schoolId=schoolId), model=types.PostsResponse) 

    get_ads_list = get_school_notifications
    
    async def get_esiaRegions(self) -> types.EsiaRegions:
        """Get Available EsiaRegions [GET]
        ~~~
        
        :return: `types.EsiaRegions`
        """
        return await self.get(self.method("getAvailableEsiaRegions"), model=types.EsiaRegions, required_token=False) 

    async def get_chat_close_contacts(self) -> types.ContactsResponse:
        """GetChatCloseContacts [GET]
        ~~~
        
        :return: ``types.ContactsResponse``
        """
        return await self.get(self.method("getChatCloseContacts"), model=types.ContactsResponse) 
    
    async def get_contact_list(self, fromJid: Optional[str] = None) -> types.ContactsResponse:
        """GetChatContacts [GET]
        ~~~
        
        :param: `fromJid` (``str``, ``*optional*``)
        
        :return: ``types.ContactsResponse``
        """
        return await self.get(self.method("getChatContacts"), model=types.ContactsResponse, params={} if not fromJid else {"fromJid": fromJid}) 
    
    async def get_chat_context(self) -> types.ChatContextResponse:
        """GetChatContext [GET]
        ~~~
        
        :return: `types.ChatContextResponse`
        """
        return await self.get(self.method("getChatContext"), model=types.ChatContextResponse) 
    
    async def get_chat_credentials(self) -> types.ChatCredsResponse:
        """GetChatCredentials [POST]
        ~~~
        
        :return: `types.ChatCredsResponse`
        """
        return await self.post(self.method("getChatCredentials"), model=types.ChatCredsResponse) 
    
    async def get_chats(self, jidsWrapper: types.JidsWrapper) -> types.ChatsResponse:
        """GetChats [POST]
        ~~~
        
        :param: `jidsWrapper` (``types.JidsWrapper``)
        
        :return: `types.ChatsResponse`
        """
        return await self.post(self.method("getChats"), json=jidsWrapper.dict(), model=types.ChatsResponse) 

    async def get_comment_comments_list(self, event_key: str, parentCommentId: int, fromCommentId: Optional[str] = None, limit: Optional[int] = None) -> types.PostCommentsResponse:
        """GetCommentCommentsList [GET]
        ~~~
        
        :param: `event_key` (``str``)
        :param: `parentCommentId` (``int``)
        :param: `fromCommentId` (``str``, ``*optional*``)
        :param: `limit` (``int``, ``*optional*``)
        
        :return: `types.PostCommentResponse`
        """
        return await self.get(self.method("getCommentCommentsList", event_key=event_key, parentCommentId=parentCommentId), model=types.PostCommentsResponse, params={ 
            **({} if not fromCommentId else {"fromCommentId": fromCommentId}),
            **({} if not limit else {"limit": str(limit)})
        })
    
    async def get_task_status(self, taskId: str) -> types.TaskStatus:
        """GetTaskStatus [GET]
        ~~~
        
        :param: `taskId` (``str``)
        
        :return: `types.TaskStatus`
        """
        return await self.get(self.method("getEsiaTaskStaus"), params={"taskId": taskId}, model=types.TaskStatus, required_token=False) 
    
    async def get_final_marks(self, personId: Union[int, str], groupId: Union[int, str]) -> types.FinalMarksResponse:
        """GetFinalGrades(Marks) [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        
        :return: `types.FinalMarksResponse`
        """
        return await self.get(self.method("getFinalGrades", personId=personId, groupId=groupId), model=types.FinalMarksResponse) 
    
    async def get_person_period_marks(self, personId: Union[int, str], groupId: Union[int, str], periodId: Union[int, str]) -> types.MarksResponse:
        """Get Person Period Marks [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        :param: `periodId` (``int`` | ``str``)
        
        :return: `types.MarksResponse`
        """
        return await self.get(self.method("getPersonMarks", periodId=periodId, personId=personId, groupId=groupId), model=types.MarksResponse) 
    
    async def get_user_push_settings(self, userId: Union[int, str]) -> types.PushSettingsResponse:
        """Get User PushNotifications Settings [GET]
        ~~~
        
        :param: `userId` (``int`` | ``str``)
        
        :return: `types.PushSettingsResponse`
        """
        return await self.get(self.method("getPushSettings", userId=userId), model=types.PushSettingsResponse) 
    
    async def get_group_rating(self, personId: Union[int, str], groupId: Union[int, str]) -> types.RatingResponse:
        """Get EduGroup Rating [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        
        :return: `types.RatingResponse`
        """
        return await self.get(self.method("getRating", personId=personId, groupId=groupId), model=types.RatingResponse) 
    
    async def get_subject_details(self, personId: Union[int, str], groupId: Union[int, str], subjectId: Union[int, str], periodId: Union[int, str]) -> types.SubjectDetailsResponse:
        """Get person group subject details [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        :param: `subjectId` (``int`` | ``str``)
        :param: `periodId` (``int`` | ``str``)
        
        :return: `types.SubjectDetailsResponse`"""
        return await self.get(self.method("getSubjectDetailds", personId=personId, groupId=groupId, subjectId=subjectId, periodId=periodId), model=types.SubjectDetailsResponse) 

    async def get_lesson_details(self, personId: Union[int, str], groupId: Union[int, str], lessonId: Union[int, str]) -> types.LessonDetailsResponse:
        """Get person group lesson details [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        :param: `lessonId` (``int`` | ``str``)
        
        :return: `types.LessonDetailsResponse`"""
        return await self.get(self.method("getLessonDetailds", personId=personId, groupId=groupId, lessonId=lessonId), model=types.LessonDetailsResponse) 
    
    async def get_mark_details(self, personId: Union[int, str], groupId: Union[int, str], markId: Union[int, str]) -> types.MarkDetailsResponse:
        """Get person group mark details [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        :param: `markId` (``int`` | ``str``)
        
        :return: `types.MarkDetailsResponse`"""
        return await self.get(self.method("getMarksDetailds", personId=personId, groupId=groupId, markId=markId), model=types.MarkDetailsResponse) 

    async def get_user_subscription_info(self, userId: Union[int, str]) -> types.SubscriptionInfoResponse:
        """Get User Subscription Info [GET]
        ~~~
        
        :param: `userId` (``int`` | ``str``)
        
        :return: `types.SubscriptionInfoResponse`
        """
        return await self.get(self.method("getSubscriptionInfo", userId=userId), model=types.SubscriptionInfoResponse) 
    
    async def get_user_avatar(self, userId: Union[int, str]) -> types.UserAvatarResponse:
        """Get User Avatar [GET]
        ~~~
        
        :param: `userId` (``int`` | ``str``)
        
        :return: `types.UserAvatarResponse`
        """
        return await self.get(self.method("getUserAvatar", userId=userId), model=types.UserAvatarResponse) 
    
    async def get_user_context(self, userId: Union[int, str]) -> types.UserContextResponse:
        """Get User Context Info [GET]
        ~~~
        
        :param: `userId` (``int`` | ``str``)
        
        :return: `types.UserContextResponse`
        """
        return await self.get(self.method("getUserContext", userId=userId), model=types.UserContextResponse) 
    
    async def get_user_day_book(self, personId: Union[int, str], schoolId: Union[int, str], groupId: Union[int, str], id: Optional[str] = None, loadType: Optional[str] = None) -> types.DayBookResponse:
        """Get User Day Book [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `schoolId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        :param: `id` (``str``, ``*optional*``)
        :param: `loadType` (``str``, ``*optional*``)
        
        :return: `types.DayBookResponse`
        """
        return await self.get(self.method("getUserDayBook", personId=personId, schoolId=schoolId, groupId=groupId), model=types.DayBookResponse, params={ 
            **({} if not id else {"id": id}),
            **({} if not loadType else {"loadType": str(loadType)})
        })
    
    async def get_user_feed(self, personId: Union[int, str], groupId: Union[int, str]) -> types.UserFeedResponse:
        """Get User Feed [GET]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        
        :return: `types.UserFeedResponse`
        """
        return await self.get(self.method("getUserFeed", personId=personId, groupId=groupId), model=types.UserFeedResponse) 
        
    async def login(self, login_data: types.LoginData) -> types.LoginResponse:
        """Login [POST]
        ~~~
        
        :param: `loginData` (``types.LoginData``)
        
        :return: `types.LoginResponse`
        """
        return await self.post(self.method("login"), json=login_data.dict(), model=types.LoginResponse, required_token=False) 
    
    async def upload_lesson_file(self, personId: Union[int, str], groupId: Union[int, str], lessonId: Union[int, str], file_name: str, fileObj: Union[BufferedReader, BufferedRandom, BufferedIOBase]) -> types.UploadResponse:
        """Upload Lesson File (Attachment) [POST]
        ~~~
        
        :param: `personId` (``int`` | ``str``)
        :param: `groupId` (``int`` | ``str``)
        :param: `lessonId` (``int`` | ``str``)
        :param: `file_name` (``str``)
        :param: `fileObj` (``BufferedReader`` | ``BufferedRandom`` | ``BufferedIOBase``), example: ``fileObj=open("path-to-file.ext", "rb")``
        
        :return: `types.UploadResponse`"""
        return await self.post(self.method("uploadAttachment", personId=personId, groupId=groupId, lessonId=lessonId), model=types.UploadResponse, files={file_name: fileObj}) 
    
    upload_attachment = upload_lesson_file
   
    async def upload_user_avatar(self, userId: Union[int, str], fileObj: Union[BufferedReader, BufferedRandom, BufferedIOBase]) -> types.UploadResponse:
        """Upload User Avatar [POST]
        ~~~
        
        :param: `userId` (``int`` | ``str``)
        :param: `file_name` (``str``)
        :param: `fileObj` (``BufferedReader`` | ``BufferedRandom`` | ``BufferedIOBase``), example: ``fileObj=open("path-to-file.ext", "rb")``
        
        :return: `types.UploadResponse`"""
        return await self.post(self.method("uploadAvatar", userId=userId), model=types.UploadResponse, files={"avatar": fileObj}) 
    
    async def auth(self, auth_data: types.AuthData) -> types.AuthResult:
        """Auth [POST]
        ~~~
        
        :param: `auth_data` (``types.AuthData``)
        
        :return: ``types.AuthResult``
        """
        return await self.post(self.method('auth'), json=auth_data.dict(), model=types.AuthResult, required_token=False) 

