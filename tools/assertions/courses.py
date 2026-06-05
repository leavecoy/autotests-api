from tools.assertions.base import assert_equal, assert_length
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesResponseSchema, CourseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
import allure
from tools.logger import get_logger

logger = get_logger("COURSES_ASSERTIONS")

@allure.step("Check update course response")
def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    """
    Проверяет, что ответ сервера на обновление курса соответствует запросу.
    :param request: Схема запроса на обновление курса.
    :param response: Схема ответа на обновление курса.
    :return:
    """
    logger.info("Check update course response")
    assert_equal(actual=response.course.title, expected=request.title, name="title")
    assert_equal(actual=response.course.max_score, expected=request.max_score, name="max_score")
    assert_equal(actual=response.course.min_score, expected=request.min_score, name="min_score")
    assert_equal(actual=response.course.description, expected=request.description, name="description")
    assert_equal(actual=response.course.estimated_time, expected=request.estimated_time, name="estimated_time")

@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет, что полученная модель курса соответствует ожидаемой.

    :param actual: Полученная модель курса.
    :param expected: Ожидаемая модель курса.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check course")
    assert_equal(actual=actual.id, expected=expected.id, name="id")
    assert_equal(actual=actual.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.description, expected=expected.description, name="description")
    assert_equal(actual=actual.estimated_time, expected=expected.estimated_time, name="estimated_time")

    assert_file(actual=actual.preview_file, expected=expected.preview_file)
    assert_user(actual=actual.created_by_user, expected=expected.created_by_user)

@allure.step("Check get courses response")
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
    logger.info("Check get courses response")
    assert_length(actual=get_courses_response.courses, expected=create_course_responses, name="courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(actual=get_courses_response.courses[index], expected=create_course_response.course)

@allure.step("Check create course response")
def assert_create_course_response(response: CreateCourseResponseSchema, request: CreateCourseRequestSchema):
    """
    Проверяет, что ответ на создание курса соответствует запросу на создание курса.

    :param response: Модель ответа на запрос на создание курса.
    :param request: Модель запроса на создание курса.
    :raises AssertionError: Если данные курсов не совпадают.
    """
    logger.info("Check create course response")
    assert_equal(response.course.title, request.title, "title")
    assert_equal(response.course.max_score, request.max_score, "max_score")
    assert_equal(response.course.min_score, request.min_score, "min_score")
    assert_equal(response.course.description, request.description, "description")
    assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(response.course.preview_file.id, request.preview_file_id, "preview_file")
    assert_equal(response.course.created_by_user.id, request.created_by_user_id, "name")

