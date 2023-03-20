from typing import Optional
from .model import Type, TypeMobile


class LoginData(Type):
    agreeTerms: bool
    clientId: str
    clientSecret: str
    email: str
    newPassword: str
    newPasswordRepeat: str
    password: str
    passwordRepeat: str
    phone: str
    scope: str
    token: str
    username: str


class ActivationData(Type):
    lastName: str
    firstName: str
    middleName: str
    birthday: str
    isPhoneRequired: bool
    sex: str
    termsLink: str
    personId: int
    token: str
    username: str
    password: str


class Credentials(Type):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    scope: Optional[str] = None
    userId: Optional[int] = None


class ValidationRule(Type):
    message: str
    regexs: list[str]


class PasswordLevelRules(Type):
    good: list[Optional[ValidationRule]] = []
    strong: list[Optional[ValidationRule]] = []
    unreliable: list[Optional[ValidationRule]] = []


class ValidationRules(Type):
    emailValidationRules: list[Optional[ValidationRule]] = []
    phoneValidationRules: list[Optional[ValidationRule]] = []
    passwordUnacceptableRules: list[Optional[ValidationRule]] = []
    passwordLevelRules: PasswordLevelRules


class LoginResponse(TypeMobile):
    activationData: Optional[ActivationData] = None
    credentials: Optional[Credentials] = None
    reason: Optional[str] = None
    teacherAppLink: Optional[str] = None
    validationRules: Optional[ValidationRules] = None
