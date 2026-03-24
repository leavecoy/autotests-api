"""

#
# response = {
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
# }
#


"""

from pydantic import BaseModel, Field

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: str

class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class ResponseSchema(BaseModel):
    course: CourseSchema

file = FileSchema(
    id="file_id",
    filename="file_filename",
    directory="file_directory",
    url="file_url"
)

user = UserSchema(
    id="user_id",
    email="user_email",
    lastName="user_last_name",
    firstName="user_first_name",
    middleName="user_middle_name"
)

course = CourseSchema(
    id="course_id",
    title="course_title",
    maxScore=10,
    minScore=1,
    description="course_desc",
    previewFile=file,
    estimatedTime="course_est_time",
    createdByUser=user
)

print(course.model_dump_json())