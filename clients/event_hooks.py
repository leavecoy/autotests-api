import allure
from httpx import Request, Response
from tools.logger import get_logger
from tools.http.curl import make_curl_from_request

logger = get_logger("HTTP_LOGGER")

def curl_event_hook(request: Request):
    """
    Event hook для автоматического прикрепления cURL команды к Allure отчету.

    :param request: HTTP-запрос, переданный в `httpx` клиент.
    """
    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)

def log_request_event_hook(request: Request):
    """
    Event hook для создания логов с запросами к серверу.

    :param request: Запрос, переданный клиенту.
    """
    logger.info(f"Make {request.method} request to {request.url}")

def log_response_event_hook(response: Response):
    """
    Event hook для создания логов с ответами сервера.

    :param response: Ответ, полученный от сервера.
    """
    logger.info(f"Got response {response.status_code} {response.reason_phrase} from {response.url}")