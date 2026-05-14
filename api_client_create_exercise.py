from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.courses.courses_client import get_courses_client

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()

create_user_response = public_users_client.create_user(create_user_request)
print("Create user data:", create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(user=authentication_user)
courses_client = get_courses_client(user=authentication_user)
exercises_client = get_exercises_client(user=authentication_user)

create_file_request = CreateFileRequestSchema(upload_file="./test_data/files/image.png")

create_file_response=files_client.create_file(create_file_request)
print("Create file data:", create_file_response)

course = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)

create_course_response = courses_client.create_course(request=course)
print("Create course data:", create_course_response)

exercise = CreateExerciseRequestSchema(course_id=create_course_response.course.id)

create_exercise_response = exercises_client.create_exercise(request=exercise)
print("Create exercise data:", create_exercise_response)