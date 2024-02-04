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
        assert response.status_code == 200, f"POST запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

       

    # GET
    @pytest.mark.order(2)   
    def test_send_get_request(self, setup):
     
        params = {"username": "test12"}
        response = requests.get(f"{self.api_base_url}/user/{params['username']}", params=params)
        assert response.status_code == 200, f"GET запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

       

    # PUT
    @pytest.mark.order(3)   
    def test_send_put_request(self, setup):
     
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
        assert response.status_code == 200, f"PUT запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

      

    # DELETE
    @pytest.mark.order(4)   
    def test_send_delete_request(self, setup):
       
        username_to_delete = "test1223"
        response = requests.delete(f"{self.api_base_url}/user/{username_to_delete}")
        assert response.status_code in [200, 204, 404], f"DELETE запрос вернул статус код: {response.status_code}"
        print("Тест успешно пройден")

       
if __name__ == "__main__":
    pytest.main()
