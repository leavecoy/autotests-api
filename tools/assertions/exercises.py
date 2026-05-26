from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from tools.assertions.base import assert_equal

def assert_create_exercise_response(response: CreateExerciseResponseSchema, request: CreateExerciseRequestSchema):
    """
    Проверяет, что ответ сервера соответствует запросу на создание упражнения.
    :param response: Модель ответа сервера на запрос на создание упражнения.
    :param request: Модель запроса на создание упражнения
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")
