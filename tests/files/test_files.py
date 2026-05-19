from http import HTTPStatus
from clients.files.files_client import FilesClient, get_files_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response
from tools.assertions.schema import validate_json_schema
import pytest

@pytest.mark.files
@pytest.mark.regression
class TestFiles:
    def test_create_files(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./test_data/files/image.png")
        response = files_client.create_file_api(request)

        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_file_response(request=request, response=response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
