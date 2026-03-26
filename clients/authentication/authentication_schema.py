from pydantic import BaseModel, Field, EmailStr

class TokenSchema(BaseModel):
    """
    Описание модели структуры токена.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Описание модели структуры запроса на аутентификацию.
    """
    email: EmailStr
    password: str

class LoginResponseSchema(BaseModel):
    """
    Описание модели структуры ответа на запрос на аутентификацию.
    """
    token: TokenSchema

class RefreshRequestSchema(BaseModel):
    """
    Описание модели структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")