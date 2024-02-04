import tracemalloc
import requests
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PetstoreAPITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.api_base_url = "https://petstore.swagger.io/v2"
# POST
    def test_send_post_request(self):
        tracemalloc.start()  # Включаем tracemalloc
        # Параметры для POST-запроса
        data = {
            "id": 223,
            "username": "test12",
            "firstName": "test223",
            "lastName": "test32323",
            "email": "111@mail.ru",
            "password": "12345",
            "phone": "8989787776",
            "userStatus": 0
        }
        response = requests.post(f"{self.api_base_url}/user", json=data)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200, "POST запрос вернул статус код: {}".format(response.status_code))
        print("Тест успешно пройден")

        # Добавьте другие проверки, в зависимости от ваших требований

        snapshot = tracemalloc.take_snapshot()  # Получаем снимок памяти
        top_stats = snapshot.statistics("lineno")  # Получаем статистику
        print("[ Top 10 ]")
        for stat in top_stats[:10]:
            print(stat)

        tracemalloc.stop()  # Останавливаем tracemalloc
    # GET
    def test_send_get_request(self):
        tracemalloc.start()  # Включаем tracemalloc
        # Параметры для GET-запроса
        params = {"username": "test12"}
        response = requests.get(f"{self.api_base_url}/user/{params['username']}", params=params)


        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200, "GET запрос вернул статус код: {}".format(response.status_code))
        print("Тест успешно пройден")

        # Добавьте другие проверки, в зависимости от ваших требований

        snapshot = tracemalloc.take_snapshot()  # Получаем снимок памяти
        top_stats = snapshot.statistics("lineno")  # Получаем статистику
        print("[ Top 10 ]")
        for stat in top_stats[:10]:
            print(stat)

        tracemalloc.stop()  # Останавливаем tracemalloc
# PUT
    def test_send_put_request(self):
        tracemalloc.start()  # Включаем tracemalloc
        # Параметры для PUT-запроса
        put_data = {
            "id": 223,
            "username": "test1223",
            "firstName": "updated_first_name",
            "lastName": "updated_last_name",
            "email": "updated_email@mail.ru",
            "password": "updated_password",
            "phone": "8989787776",
            "userStatus": 1
        }
        response = requests.put(f"{self.api_base_url}/user/{put_data['id']}", json=put_data)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200, "PUT запрос вернул статус код: {}".format(response.status_code))
        print("Тест успешно пройден")

        # Добавьте другие проверки, в зависимости от ваших требований

        snapshot = tracemalloc.take_snapshot()  # Получаем снимок памяти
        top_stats = snapshot.statistics("lineno")  # Получаем статистику
        print("[ Top 10 ]")
        for stat in top_stats[:10]:
            print(stat)

        tracemalloc.stop()  # Останавливаем tracemalloc
# DELETE
    def test_send_delete_request(self):
        tracemalloc.start()  # Включаем tracemalloc
        # Параметры для DELETE-запроса
        username_to_delete = "test1223"  # Replace with the actual username to delete
        response = requests.delete(f"{self.api_base_url}/user/{username_to_delete}")

        # Проверка статуса ответа
        self.assertIn(response.status_code, [200, 204, 404], "DELETE запрос вернул статус код: {}".format(response.status_code))
        print("Тест успешно пройден")

        # Добавьте другие проверки, в зависимости от ваших требований

        snapshot = tracemalloc.take_snapshot()  # Получаем снимок памяти
        top_stats = snapshot.statistics("lineno")  # Получаем статистику
        print("[ Top 10 ]")
        for stat in top_stats[:10]:
            print(stat)

        tracemalloc.stop()  # Останавливаем tracemalloc


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(PetstoreAPITest('test_send_post_request'))
 
    suite.addTest(PetstoreAPITest('test_send_get_request'))
    suite.addTest(PetstoreAPITest('test_send_put_request'))
    suite.addTest(PetstoreAPITest('test_send_delete_request'))

    
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
