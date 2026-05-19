import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("x", [1, 2, 3])
def test_numbers(x: int):
    assert x == 3

@pytest.mark.parametrize("x, y", [(1, 1), (2, 2), (3, 3)])
def test_number_two(x: int, y: int):
    assert x == y

@pytest.fixture(params=["host1", "host2", "host3"])
def host(request) -> SubRequest:
    return request.param

def test_host(host: str):
    print(f"{host}")

@pytest.mark.parametrize("user", ["User1", "User2"])
class TestOperations:
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

users = {
    "number1": "id1",
    "number2": "id2",
    "number3": "id3"
}


@pytest.mark.parametrize(
    "phone_number", users.keys(),
    ids=lambda phone_number: f"{phone_number}, {users[phone_number]}"
)
def test_id(phone_number: str):
    ...