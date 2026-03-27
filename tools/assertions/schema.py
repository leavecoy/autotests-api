from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema)
    :param instance: валидируемый JSON
    :param schema: модель, по которой валидируется JSON
    :raises: jsonschema.exceptions.ValidationError: Если instance не соответствует schema.
    :return: None
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )