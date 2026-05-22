from http import HTTPStatus
from clients.courses.courses_client import CoursesClient
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_get_courses_response
from tools.assertions.schema import validate_json_schema
from clients.courses.courses_schema import (UpdateCourseRequestSchema, UpdateCourseResponseSchema,GetCoursesQuerySchema,
                                            GetCoursesResponseSchema)
import pytest

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:

    def test_update_course(self, function_course: CourseFixture, courses_client: CoursesClient):
        request = UpdateCourseRequestSchema()

        response = courses_client.update_course_api(course_id=function_course.response.course.id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())

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

