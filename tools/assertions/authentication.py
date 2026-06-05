from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true
import allure
from tools.logger import get_logger

logger = get_logger("AUTHENTICATION_ASSERTIONS")

@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет, корректность ответа при успешной авторизации.

    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если хотя бы одно условие не выполнено.
    """
    logger.info("Check login response")
    assert_equal(response.token.token_type, expected="bearer", name="token_type")
    assert_is_true(response.token.access_token, name="access_token")
    assert_is_true(response.token.refresh_token, name="refresh_token")
