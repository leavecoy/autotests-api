from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from tools.assertions.base import assert_equal


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
      Проверяет, что ответ на создание файла соответствует запросу.

      :param request: Исходный запрос на создание файла.
      :param response: Ответ API с данными файла.
      :raises AssertionError: Если хотя бы одно поле не совпадает.
      """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"
    assert_equal(str(response.file.url), expected_url, name="url")
    assert_equal(response.file.filename, request.filename, name="filename")
    assert_equal(response.file.directory, request.directory, name="directory")