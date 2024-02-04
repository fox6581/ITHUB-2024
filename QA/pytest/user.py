import unittest
import requests

class PetstoreAPITest(unittest.TestCase):

    def test_create_user(self):
        url = "https://petstore.swagger.io/v2/user"
        headers = {"Content-Type": "application/json"}

        data = {
            "id": 22,
            "username": "test13",
            "firstName": "test223",
            "lastName": "test32323",
            "email": "111@mail.ru",
            "password": "12345",
            "phone": "8989787776",
            "userStatus": 0
        }

        response = requests.post(url, json=data, headers=headers)

        # Проверка успешности запроса (можете настроить на основе ожидаемого кода ответа)
        self.assertEqual(response.status_code, 200)

        # Проверка, что создание пользователя выполнено успешно (ваша логика проверки)
        self.assertEqual(response.json().get("code"), 200)

if __name__ == "__main__":
    unittest.main()