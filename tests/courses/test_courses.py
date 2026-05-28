import pytest
import allure
from http import HTTPStatus
from clients.courses.courses_client import CoursesClient
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_get_courses_response, assert_create_course_response
from tools.assertions.schema import validate_json_schema
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.parent_suites import AllureParentSuite
from tools.allure.suites import AllureSuite
from tools.allure.sub_suites import AllureSubSuite
from allure_commons.types import Severity
from clients.courses.courses_schema import (UpdateCourseRequestSchema, UpdateCourseResponseSchema,
                                            GetCoursesQuerySchema,
                                            GetCoursesResponseSchema, CreateCourseRequestSchema,
                                            CreateCourseResponseSchema)

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.suite(AllureSuite.COURSES)
class TestCourses:
    @allure.title("Update course")
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureSubSuite.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_update_course(self, function_course: CourseFixture, courses_client: CoursesClient):
        request = UpdateCourseRequestSchema()

        response = courses_client.update_course_api(course_id=function_course.response.course.id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get course")
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureSubSuite.GET_ENTITIES)
    @allure.severity(Severity.BLOCKER)
    def test_get_courses(
            self,
            function_user: UserFixture,
            function_course: CourseFixture,
            courses_client: CoursesClient
    ):

        query = GetCoursesQuerySchema(user_id=function_user.response.user.id) # noqa
        response = courses_client.get_courses_api(query=query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_courses_response(
            get_courses_response=response_data,
            create_course_responses=[function_course.response]
        )

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create course")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureSubSuite.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_course(
            self,
            function_user: UserFixture,
            function_file: FileFixture,
            courses_client: CoursesClient
    ):
        request = CreateCourseRequestSchema(
            preview_file_id=function_file.response.file.id, # noqa
            created_by_user_id=function_user.response.user.id # noqa
        )
        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())
