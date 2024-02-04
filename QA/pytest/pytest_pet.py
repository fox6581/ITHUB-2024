import tracemalloc
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestPetstoreAPI:

    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.api_base_url = "https://petstore.swagger.io/v2"
        yield
        self.driver.close()

    # POST
    @pytest.mark.order(1)   
    def test_send_post_request(self, setup):
        
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
        assert response.status_code == 200, f"POST запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

    # GET
    @pytest.mark.order(2)   
    def test_send_get_request(self, setup):
       
        params = {"petId": "10"}
        response = requests.get(f"{self.api_base_url}/pet/{params['petId']}", params=params)
        assert response.status_code == 200, f"GET запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

        
    # PUT
    @pytest.mark.order(3)   
    def test_send_put_request(self, setup):
       
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
        assert response.status_code == 200, f"PUT запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

       
    # Additional POST test
    @pytest.mark.order(4)   
    def test1_send_post_request(self, setup):
       
        put_data = {
            "id": 10,
            "name": "string1111",
            "status": "sold"
        }
        response = requests.post(f"{self.api_base_url}/pet", json=put_data)
        assert response.status_code == 200, f"POST запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден на обновление")

       
    # Additional GET test
    @pytest.mark.order(5)   
    def test_find_pets_by_status_sold(self, setup):
        params = {"status": "sold"}
        response = requests.get(f"{self.api_base_url}/pet/findByStatus", params=params)
        assert response.status_code == 200, f"GET запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

        try:
            json_data = response.json()
            assert isinstance(json_data, list), "Ответ не содержит список питомцев"
            print("Ответ содержит список питомцев")
        except ValueError:
            pytest.fail("Ответ не является валидным JSON")

    # DELETE
    @pytest.mark.order(6)   
    def test_send_delete_request(self, setup):
       
        petId = "10"
        response = requests.delete(f"{self.api_base_url}/pet/{petId}")
        assert response.status_code in [200, 204, 404], f"DELETE запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

if __name__ == "__main__":
    pytest.main()
