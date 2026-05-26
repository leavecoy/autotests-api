from http import HTTPStatus
from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FileFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.schema import validate_json_schema
import pytest
import allure

@pytest.mark.files
@pytest.mark.regression
class TestFiles:
    @allure.title("Create file")
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./test_data/files/image.png")
        response = files_client.create_file_api(request)

        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_file_response(request=request, response=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get file")
    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(file_id=function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_file_response(gef_file_response=response_data, create_file_response=function_file.response)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create file with empty filename")
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(filename="", upload_file="./test_data/files/image.png")

        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(actual=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Create file with empty directory")
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(directory="", upload_file="./test_data/files/image.png")

        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(actual=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get empty file")
    def test_get_empty_file(self, files_client, function_file: FileFixture):
        delete_response = files_client.delete_file_api(file_id=function_file.response.file.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = files_client.get_file_api(file_id=function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(actual=get_response.status_code, expected=HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.title("Create file with incorrect file id")
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        response = files_client.get_file_api("incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(actual=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())