import allure
from helpers.api_client import ApiClient
from config import Config

api = ApiClient()

@allure.feature("Логин пользователя")
class TestLogin:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, user_data):
        # Сначала регистрируем
        api.create_user(user_data)
        # Пытаемся залогиниться
        login_payload = {"email": user_data["email"], "password": user_data["password"]}
        response = api.login_user(login_payload)
        
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()

    @allure.title("Вход с неверным логином и паролем")
    def test_login_wrong_credentials(self):
        payload = {"email": "wrong_email@test.ru", "password": "wrong_pass"}
        response = api.login_user(payload)
        
        assert response.status_code == 401
        assert response.json().get("message") == "email or password are incorrect"