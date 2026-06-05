from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
import allure
from config import settings
from tools.logger import get_logger

logger = get_logger("FILES_ASSERTIONS")

@allure.step("Check create file response")
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
      Проверяет, что ответ на создание файла соответствует запросу.

      :param request: Исходный запрос на создание файла.
      :param response: Ответ API с данными файла.
      :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check create file response")
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"
    assert_equal(str(response.file.url), expected_url, name="url")
    assert_equal(response.file.filename, request.filename, name="filename")
    assert_equal(response.file.directory, request.directory, name="directory")

@allure.step("Check file")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
      Проверяет, что полученная модель файла соответствует ожидаемой.

      :param actual: Полученная модель файла.
      :param expected: Ожидаемая модель файла.
      :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check file")
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.url, expected.url, name="url")
    assert_equal(actual.filename, expected.filename, name="filename")
    assert_equal(actual.directory, expected.directory, name="directory")

@allure.step("Check get file response")
def assert_get_file_response(
        gef_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
      Проверяет, что ответ на получение файла соответствует запросу на создание файла.

      :param gef_file_response: Ответ API на запрос на получение файла.
      :param create_file_response: Ответ API на запрос на создание файла.
      :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Check get file response")
    assert_file(actual=create_file_response.file, expected=gef_file_response.file)

@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty filename response")
    # noinspection PyArgumentList
    expected = ValidationErrorResponseSchema( # noqa
        details=[
            ValidationErrorSchema( # noqa
                type="string_too_short",
                location=["body", "filename"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check create file with empty directory response")
    # noinspection PyArgumentList
    expected = ValidationErrorResponseSchema( # noqa
        details=[
            ValidationErrorSchema( # noqa
                type="string_too_short",
                location=["body", "directory"],
                message="String should have at least 1 character",
                input="",
                context={"min_length": 1}
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Check file nof found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если файл не найден на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
    """
    logger.info("Check file nof found response")
    expected = InternalErrorResponseSchema(details="File not found") # noqa
    assert_internal_error_response(actual, expected)

@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на получение файла с некорректным ID соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Check get file with incorrect file id response")
    # noinspection PyArgumentList
    expected = ValidationErrorResponseSchema( # noqa
        details=[
            ValidationErrorSchema( # noqa
                type="uuid_parsing",
                location=["path", "file_id"],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` "
                        "followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-file-id",
                context={
                    "error":
                        "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found "
                        "`i` at 1"
                }
            )
        ]
    )
    assert_validation_error_response(actual, expected)