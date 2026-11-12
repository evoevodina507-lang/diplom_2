import allure
import requests
from helpers.api_client import ApiClient
from config import Config

api = ApiClient()

@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self, user_data):
        response = api.create_user(user_data)
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, created_user, user_data):
        # created_user - фикстура, которая уже создала юзера
        response = api.create_user(user_data)
        assert response.status_code == 403
        assert response.json().get("message") == "User already exists"

    @allure.title("Создать пользователя без обязательного поля (password)")
    def test_create_user_missing_field(self, user_data):
        del user_data["password"]
        response = api.create_user(user_data)
        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"