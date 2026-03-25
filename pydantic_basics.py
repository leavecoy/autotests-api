"""

#
# {
#   "course": {
#     "id": "string",
#     "title": "string",
#     "maxScore": 0,
#     "minScore": 0,
#     "description": "string",
#     "previewFile": {
#       "id": "string",
#       "filename": "string",
#       "directory": "string",
#       "url": "https://example.com/"
#     },
#     "estimatedTime": "string",
#     "createdByUser": {
#       "id": "string",
#       "email": "user@example.com",
#       "lastName": "string",
#       "firstName": "string",
#       "middleName": "string"
#     }
#   }

"""
import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_username(self) -> str:
        return f'{self.first_name} {self.last_name}'

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda :str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id="1",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileSchema( id="id", filename="filename", directory="directory", url="https://example.com/"),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="id", email="user@example.com", lastName="LastName", firstName="FirstName", middleName="MiddleName"
    )
)

print("Course default model:", course_default_model)

course_dict = {
    "id": "1",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "string",
        "filename": "string",
        "directory": "string",
        "url": "https://example.com/"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
  }

course_dict_model = CourseSchema(**course_dict)
print("Course dict model:", course_dict_model)

course_json = """
{
    "id": "1",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "string",
        "filename": "string",
        "directory": "string",
        "url": "https://example.com/"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
  }
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print("Course json model:", course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))

user = UserSchema(
    id = "id", email = "user@example.com", lastName = "LastName", firstName = "FirstName", middleName = "MiddleName"
)

print(user.get_username(), user.username)

try:
    file = FileSchema(
        id = "12",
        filename=";sldkf",
        directory="efsw",
        url="123"
    )
except ValidationError as error:
    print(error)
    print(error.errors())