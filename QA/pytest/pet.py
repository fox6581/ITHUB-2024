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
            "id": 10,
            "category": {
                "id": 10,
                "name": "bla"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
            }
        
        response = requests.post(f"{self.api_base_url}/pet", json=data)

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
        params = {"petId": "10"}
        response = requests.get(f"{self.api_base_url}/pet/{params['petId']}", params=params)


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
            "id": 10,
            "category": {
                "id": 10,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
            
        }
        response = requests.put(f"{self.api_base_url}/pet", json=put_data)

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
# PUT
    def test1_send_post_request(self):
        tracemalloc.start()  # Включаем tracemalloc
        # Параметры для PUT-запроса
        put_data = {
            "id": 10,
            
            "name": "string1111",
           
            
            "status": "sold"
        }
        response = requests.post(f"{self.api_base_url}/pet", json=put_data)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200, "POST запрос вернул статус код: {}".format(response.status_code))
        print("Тест успешно пройден на обновление")

        # Добавьте другие проверки, в зависимости от ваших требований

        snapshot = tracemalloc.take_snapshot()  # Получаем снимок памяти
        top_stats = snapshot.statistics("lineno")  # Получаем статистику
        print("[ Top 10 ]")
        for stat in top_stats[:10]:
            print(stat)

    # 
    def test_find_pets_by_status_sold(self):
        # Параметры для GET-запроса
        params = {"status": "sold"}
        response = requests.get(f"{self.api_base_url}/pet/findByStatus", params=params)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200, "GET запрос вернул статус код: {}".format(response.status_code))
        print("Тест успешно пройден")

        # Проверка, что ответ в формате JSON
        try:
            json_data = response.json()
            self.assertIsInstance(json_data, list, "Ответ не содержит список питомцев")
            print("Ответ содержит список питомцев")
        except ValueError:
            self.fail("Ответ не является валидным JSON")

#         tracemalloc.stop()  # Останавливаем tracemalloc
# DELETE
    def test_send_delete_request(self):
        tracemalloc.start()  # Включаем tracemalloc
        # Параметры для DELETE-запроса
        petId  = "10"  # Replace with the actual username to delete
        response = requests.delete(f"{self.api_base_url}/pet/{petId }")

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
    suite.addTest(PetstoreAPITest('test1_send_post_request'))
    suite.addTest(PetstoreAPITest('test_find_pets_by_status_sold'))
    suite.addTest(PetstoreAPITest('test_send_delete_request'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
