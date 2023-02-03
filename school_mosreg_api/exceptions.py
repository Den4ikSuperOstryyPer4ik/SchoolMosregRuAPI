class APIError(Exception):
    """Обработка всех типов ошибок"""
    NAME = "APIError"

    def __init__(self, url: str, status_code: int, description: str = None) -> None:
        error_text = f"API-Error | {status_code}:{self.NAME}:\nURL: {url}"
        
        if description:
            error_text += f"\n{description}"
        
        super().__init__(error_text)
        
        self.url = url
        self.status_code = status_code
        self.description = description


class HTMLError(APIError):
    """HTML отраженная ошибка."""
    NAME = "HTMLError"


class InvalidRequest(APIError):
    """Неверный запрос"""
    NAME = "InvalidRequest"


class ParameterInvalid(APIError):
    """Неверное значение одного из параметров"""
    NAME = "ParameterInvalid"


class ApiResourceUnavailable(APIError):
    """Ресурс не существует"""
    NAME = "ApiResourceUnavailable"


class ApiMethodNotSupported(APIError):
    """Метод не поддерживается для этого ресурса"""
    NAME = "ApiMethodNotSupported"


class ApiRequestLimit(APIError):
    """Превышен лимит запросов для данного токена"""
    NAME = "ApiRequestLimit"


class ApiServerError(APIError):
    """Ошибка на сервере"""
    NAME = "ApiServerError"


class ApiHttpsRequired(APIError):
    """Ресурс доступен только через https"""
    NAME = "ApiHttpsRequired"


class AuthorizationInvalidToken(APIError):
    """Неверный или неактивный токен"""
    NAME = "AuthorizationInvalidToken"


class AuthorizationTokenRequired(APIError):
    """Для доступа к ресурсу нужна авторизация"""
    NAME = "AuthorizationTokenRequired"


class AuthorizationOutOfScope(APIError):
    """Токен содержит недостаточно прав доступа """
    NAME = "AuthorizationOutOfScope"


class AuthorizationNotOwner(APIError):
    """Текущий пользователь не является владельцем ресурса"""
    NAME = "AuthorizationNotOwner"


class AuthorizationOwnerForbidden(APIError):
    """Данный запрос запрещён владельцем ресурса"""
    NAME = "AuthorizationOwnerForbidden"


class AuthorizationSystemForbidden(APIError):
    """Данный запрос запрещён правилами доступа системы"""
    NAME = "AuthorizationSystemForbidden"

all_error_types_str = [
    'HTMLError',
    'InvalidRequest',
    'ParameterInvalid',
    'ApiResourceUnavailable',
    'ApiMethodNotSupported',
    'ApiRequestLimit',
    'ApiServerError',
    'ApiHttpsRequired',
    'AuthorizationInvalidToken',
    'AuthorizationTokenRequired',
    'AuthorizationOutOfScope',
    'AuthorizationNotOwner',
    'AuthorizationOwnerForbidden',
    'AuthorizationSystemForbidden',
]

all_error_types_str_ = [
    'HTMLError',
    'invalidRequest',
    'parameterInvalid',
    'apiResourceUnavailable',
    'apiMethodNotSupported',
    'apiRequestLimit',
    'apiServerError',
    'apiHttpsRequired',
    'authorizationInvalidToken',
    'authorizationTokenRequired',
    'authorizationOutOfScope',
    'authorizationNotOwner',
    'authorizationOwnerForbidden',
    'authorizationSystemForbidden',
    'invalidToken',
    'tokenRequired',
    'outOfScope',
    'notOwner',
    'ownerForbidden',
    'systemForbidden',
    'resourceUnavailable',
    'methodNotSupported',
    'requestLimit',
    'serverError',
    'httpsRequired',
]

all_error_types_str__dict = {
    'HTMLError': "HTMLError",
    'invalidRequest': "InvalidRequest",
    'parameterInvalid': "ParameterInvalid",
    'apiResourceUnavailable': "ApiResourceUnavailable",
    'apiMethodNotSupported': "ApiMethodNotSupported",
    'apiRequestLimit': "ApiRequestLimit",
    'apiServerError': "ApiServerError",
    'apiHttpsRequired': "ApiHttpsRequired",
    'authorizationInvalidToken': "AuthorizationInvalidToken",
    'authorizationTokenRequired': "AuthorizationTokenRequired",
    'authorizationOutOfScope': "AuthorizationOutOfScope",
    'authorizationNotOwner': "AuthorizationNotOwner",
    'authorizationOwnerForbidden': "AuthorizationOwnerForbidden",
    'authorizationSystemForbidden': "AuthorizationSystemForbidden",
    'invalidToken': "AuthorizationInvalidToken",
    'tokenRequired': "AuthorizationTokenRequired",
    'outOfScope': "AuthorizationOutOfScope",
    'notOwner': "AuthorizationNotOwner",
    'ownerForbidden': "AuthorizationOwnerForbidden",
    'systemForbidden': "AuthorizationSystemForbidden",
    'resourceUnavailable': "ApiResourceUnavailable",
    'methodNotSupported': "ApiMethodNotSupported",
    'requestLimit': "ApiRequestLimit",
    'serverError': "ApiServerError",
    'httpsRequired': "ApiHttpsRequired",
}

all_error_types = {
    "HTMLError": HTMLError,
    "InvalidRequest": InvalidRequest,
    "ParameterInvalid": ParameterInvalid,
    "ApiResourceUnavailable": ApiResourceUnavailable,
    "ApiMethodNotSupported": ApiMethodNotSupported,
    "ApiRequestLimit": ApiRequestLimit,
    "ApiServerError": ApiServerError,
    "ApiHttpsRequired": ApiHttpsRequired,
    "AuthorizationInvalidToken": AuthorizationInvalidToken,
    "AuthorizationTokenRequired": AuthorizationTokenRequired,
    "AuthorizationOutOfScope": AuthorizationOutOfScope,
    "AuthorizationNotOwner": AuthorizationNotOwner,
    "AuthorizationOwnerForbidden": AuthorizationOwnerForbidden,
    "AuthorizationSystemForbidden": AuthorizationSystemForbidden,
}


def raise_error(url: str, status_code: int, error_type: str, description: str = None):
    raise all_error_types[all_error_types_str__dict[error_type]](url, status_code, description)