import pytest

@pytest.fixture
def users_client():
    print("Aboba")

class TestUserFlow:
    def test_user_can_login(self, users_client):
        ...

    def test_user_can_create_course(self, users_client):
        ...

class TestAccountFlow:
    def test_user_account(self, users_client):
        ...