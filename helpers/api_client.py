import requests
from config import Config

class ApiClient:
    def __init__(self):
        self.base_url = Config.BASE_URL

    def create_user(self, payload):
        return requests.post(f"{self.base_url}/auth/register", json=payload)

    def login_user(self, payload):
        return requests.post(f"{self.base_url}/auth/login", json=payload)

    def delete_user(self, token):
        headers = {"Authorization": token}
        return requests.delete(f"{self.base_url}/auth/user", headers=headers)

    def create_order(self, payload, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.post(f"{self.base_url}/orders", json=payload, headers=headers)