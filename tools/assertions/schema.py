from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
import allure
from tools.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")

@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema)
    :param instance: валидируемый JSON
    :param schema: модель, по которой валидируется JSON
    :raises: jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    :return: None
    """
    logger.info("Validate JSON schema")
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )