from pydantic import BaseModel, EmailStr, Field, UUID4, constr

class UserSchema(BaseModel):
    """
    Описание модели структуры пользователя.
    """
    id: UUID4
    email: EmailStr
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на создание пользователя.
    """
    email: EmailStr
    password: constr(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа сервера на запрос на создание пользователя.
    """
    user: UserSchema
