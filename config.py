import requests

class Config:
    BASE_URL = "https://stellarburgers.education-services.ru/api"
    
    # Данные для тестов
    USER_EMAIL = "test_user_api@yandex.ru"
    USER_PASSWORD = "password123"
    USER_NAME = "TestUser"

    @staticmethod
    def get_valid_ingredients():
        """Динамически получает актуальные ID ингредиентов с сервера"""
        response = requests.get(f"{Config.BASE_URL}/ingredients")
        if response.status_code == 200:
            data = response.json().get("data", [])
            # Берем ID первой булки и первой начинки/соуса
            bun_id = next(item["_id"] for item in data if item["type"] == "bun")
            main_id = next(item["_id"] for item in data if item["type"] != "bun")
            return [bun_id, main_id]
        return []