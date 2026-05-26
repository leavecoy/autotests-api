import allure
import pytest
from http import HTTPStatus
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_fount_response, assert_get_exercises_response
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExercisesQuerySchema, \
    GetExercisesResponseSchema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    @allure.title("Create exercise")
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id) # noqa

        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_create_exercise_response(response_data, request)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get exercise")
    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Update exercise")
    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        request = UpdateExerciseRequestSchema()

        response = exercises_client.update_exercise_api(
            exercise_id=function_exercise.response.exercise.id, request=request
        )
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_update_exercise_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Delete exercise")
    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        delete_exercise_response = exercises_client.delete_exercise_api(
            exercise_id=function_exercise.response.exercise.id
        )

        assert_status_code(actual=delete_exercise_response.status_code, expected=HTTPStatus.OK)

        get_exercise_response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        get_exercise_response_data = InternalErrorResponseSchema.model_validate_json(get_exercise_response.text)

        assert_status_code(actual=get_exercise_response.status_code, expected=HTTPStatus.NOT_FOUND)
        assert_exercise_not_fount_response(actual=get_exercise_response_data)

        validate_json_schema(get_exercise_response.json(), get_exercise_response_data.model_json_schema())

    @allure.title("Get exercises")
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture,
            function_exercise: ExerciseFixture
    ):
            query = GetExercisesQuerySchema(course_id=function_course.response.course.id) # noqa

            response = exercises_client.get_exercises_api(query=query)
            response_data = GetExercisesResponseSchema.model_validate_json(response.text)

            assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
            assert_get_exercises_response(
                get_exercises_responses=response_data, create_exercise_responses = [function_exercise.response]
            )

            validate_json_schema(response.json(), response_data.model_json_schema())