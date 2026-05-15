from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true

def assert_login_response(response: LoginResponseSchema):
    """
    Проверяет, корректность ответа при успешной авторизации.

    :param request: Исходный запрос на авторизацию.
    :param response: Объект ответа с токенами авторизации.
    :raises AssertionError: Если хотя бы одно условие не выполнено.
    """
    assert_equal(response.token.token_type, expected="bearer", name="token_type")
    assert_is_true(response.token.access_token, name="access_token")
    assert_is_true(response.token.refresh_token, name="refresh_token")
