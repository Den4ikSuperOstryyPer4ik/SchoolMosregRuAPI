from enum import auto
from .model import Type, TypeMobile, AutoNameEnum
from typing import Optional


class CommentUser(Type):
    f6959id: Optional[int] = None
    firstName: Optional[str] = None
    middleName: Optional[str] = None
    lastName: Optional[str] = None
    roles: Optional[list[str]] = []
    avatarUrl: Optional[str] = None
    redirectUrl: Optional[str] = None


class PostComment(Type):
    f6964id: Optional[int] = None
    parentCommentId: Optional[int] = None
    authorID: Optional[int] = None
    author: Optional[CommentUser] = None
    replyUserID: Optional[int] = None
    createdDateTime: Optional[int] = None
    level: Optional[int] = None
    text: Optional[str] = None
    hasPrevious: Optional[bool] = None
    isDeleted: Optional[bool] = None
    comments: list[Optional["PostComment"]] = []
    lastId: Optional[int] = None


class PostCommentsResponse(TypeMobile):
    eventKey: Optional[str] = None
    currentUser: Optional[CommentUser] = None
    hasPrevious: Optional[bool] = None
    comments: Optional[list[PostComment]] = []
    participants: Optional[list[CommentUser]] = []


class NotificationType(AutoNameEnum):
    Notification = auto()
    Post = auto()


class Attachment(Type):
    extension: Optional[str] = None
    fileId: Optional[str] = None
    fileLink: Optional[str] = None
    fileName: Optional[str] = None


class Post(Type):
    f6973id: Optional[int] = None
    type: Optional[NotificationType] = None
    eventKey: Optional[str] = None
    topicEventKey: Optional[str] = None
    eventSign: Optional[str] = None
    eventUrl: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    text: Optional[str] = None
    createdDateTime: Optional[str] = None
    previewUrl: Optional[str] = None
    isReaded: bool
    commentsCount: Optional[int] = None
    authorImageUrl: Optional[str] = None
    authorFirstName: Optional[str] = None
    authorLastName: Optional[str] = None
    authorMiddleName: Optional[str] = None
    files: list[Optional[Attachment]] = []
    content: Optional[str] = None
    details: Optional[str] = None
    invitationId: Optional[int] = None


class PostsResponse(Type):
    unreadCount: Optional[int] = None
    postList: list[Optional[Post]] = []

