from http import HTTPStatus

from clients.exercises.exercises_schema import GetExerciseResponseSchema
from fixtures.exercises import exercises_client, ExerciseFixture
from clients.exercises.exercises_client import ExercisesClient
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_exercises(exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
    response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
    response_data = GetExerciseResponseSchema.model_validate_json(response.text)
    print(response_data)


    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

