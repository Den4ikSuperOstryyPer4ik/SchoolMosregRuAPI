import re
from .model import Type, TypeMobile
from typing import Union, Optional


class Contact(Type):
    jid: Optional[str] = None
    name: Optional[str] = None
    shortName: Optional[str] = None
    avatar: Optional[str] = None
    irrelevant: Optional[bool] = None
    classTeacher: Optional[str] = None
    type: Optional[str] = None
    sex: Optional[str] = None
    isCloseContact: Optional[bool] = None


class ContactsResponse(TypeMobile):
    contacts: list[Optional[Contact]] = []


class ChatContextResponse(TypeMobile):
    mongooseWSHost: Optional[str] = None
    mongooseBoshHost: Optional[str] = None
    mongooseTCPHost: Optional[str] = None
    multiUserChatHost: Optional[str] = None


class ChatCredsResponse(TypeMobile):
    jid: Optional[str] = None
    token: Optional[str] = None
    attachmentHosts: list[Optional[str]] = []


class JidsWrapper(Type):
    jids: list[str]


class Chat(Type):
    jid: Optional[str] = None
    name: Optional[str] = None
    shortName: Optional[str] = None
    avatar: Optional[str] = None
    irrelevant: Optional[bool] = None
    type: Optional[str] = None
    classTeacher: Optional[str] = None
    sex: Optional[str] = None


class ChatsResponse(TypeMobile):
    jidList: list[Chat]
    
    