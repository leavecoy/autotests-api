from tools.assertions.base import assert_equal, assert_length
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesResponseSchema, CourseSchema, CreateCourseResponseSchema
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user

def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ сервера на обновление курса соответствует запросу.
    :param request: Схема запроса на обновление курса.
    :param response: Схема ответа на обновление курса.
    :return:
    """
    assert_equal(actual=response.course.title, expected=request.title, name="title")
    assert_equal(actual=response.course.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.course.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.course.description, expected=request.description, name="description")
    assert_equal(actual=response.course.estimated_time, expected=request.estimated_time, name="estimated_time")

def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что полученная модель курса соответствует ожидаемой.

    :param actual: Полученная курса файла.
    :param expected: Ожидаемая курса файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.description, expected=expected.description, name="description")
    assert_equal(actual=actual.estimated_time, expected=expected.estimated_time, name="estimated_time")

    assert_file(actual=actual.preview_file, expected=expected.preview_file)
    assert_user(actual=actual.created_by_user, expected=expected.created_by_user)

def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка курсов соответствует ответам на их создание.

    :param get_courses_response: Ответ API при запросе списка курсов.
    :param create_course_responses: Список API ответов при создании курсов.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    assert_length(actual=get_courses_response.courses, expected=create_course_responses, name="courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(actual=get_courses_response.courses[index], expected=create_course_response.course)