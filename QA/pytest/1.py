import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Убедитесь, что chromedriver.exe находится в вашем пути или явно укажите путь
        # self.driver = webdriver.Chrome(executable_path="путь_к_вашему_chromedriver.exe")
        self.driver = webdriver.Chrome()
        self.driver.get("https://petstore.swagger.io/v2/user/test13")

    def test_search_in_python_org(self):
        driver = self.driver
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
