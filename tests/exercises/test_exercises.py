from http import HTTPStatus
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response
from tools.assertions.schema import validate_json_schema


class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id) # noqa

        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_create_exercise_response(response_data, request)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())