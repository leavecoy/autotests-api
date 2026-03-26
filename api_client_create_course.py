from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
      email=get_random_email(),
      password="test",
      last_name="string",
      first_name="string",
      middle_name="string"
)

create_user_response = public_users_client.create_user(create_user_request)
print("Create user data:", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(user=authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./test_data/files/image.png"
)

create_file_response=files_client.create_file(create_file_request)
print("Create file data:", create_file_response)

course = CreateCourseRequestDict(
    title="Course1",
    maxScore=10,
    minScore=0,
    description="Description1",
    estimatedTime="10",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

create_course_response = courses_client.create_course(request=course)
print("Create course data:", create_course_response)