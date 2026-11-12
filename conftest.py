import pytest
import allure
from helpers.api_client import ApiClient
from config import Config

api = ApiClient()

@pytest.fixture(scope="function")
def user_data():
    """Генерирует уникальные данные для каждого теста, чтобы не было конфликтов"""
    import time
    return {
        "email": f"test_{int(time.time())}@yandex.ru",
        "password": "password123",
        "name": "TestUser"
    }

@pytest.fixture(scope="function")
def created_user(user_data):
    """Создает пользователя перед тестом и удаляет его после"""
    response = api.create_user(user_data)
    token = response.json().get("accessToken")
    yield token
    # Тирдаун: удаляем пользователя
    if token:
        api.delete_user(token)

@pytest.fixture(scope="function")
def auth_token(created_user):
    """Возвращает accessToken авторизованного пользователя"""
    return created_user