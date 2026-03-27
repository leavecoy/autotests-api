from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
import jsonschema
from tools.fakers import get_random_email
from tools.assertions.schema import validate_json_chema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
      email=get_random_email(),
      password="test",
      last_name="string",
      first_name="string",
      middle_name="string"
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()


validate_json_chema(instance=create_user_response.json(), schema=create_user_response_schema)
