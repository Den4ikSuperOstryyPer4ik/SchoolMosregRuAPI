from pydantic import BaseModel

class TokenWithCode(BaseModel):
    """[POST] /v2.0/authorizations \n~~~\nОбменять код доступа на токен\n~~~"""
    
    accessToken: str
    expiresIn: int
    expiresIn_str: str
    refreshToken: str
    scope: str
    user: int
    user_str: str