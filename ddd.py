import time
import unittest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class BasePage2:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, value=locator_value).click()

    def enter_text(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, value=locator_value).send_keys(text)

class LoginPage(BasePage2):
    def __init__(self, driver):
        BasePage2.__init__(self, driver)

    def test_registration(self):
        self.click_element(By.XPATH, "//*[@id='ember1005']/div/ul[1]/li[3]/a/span")
        self.click_element(By.XPATH, "//*[@id='ember964']/div/div[1]/div[2]/div/div[3]/div[1]/span")
        self.enter_text(By.XPATH, "//*[@id='ember1875']", "Netanel")
        self.enter_text(By.XPATH, "//*[@id='ember1882']", "bznatik@gmail.com")
        self.enter_text(By.XPATH, "//*[@id='valPass']", "Sisma123")
        self.enter_text(By.XPATH, "//*[@id='ember1896']", "Sisma123")
        element_txt = self.driver.find_element(By.XPATH, "//*[@id='ember1005']/div/ul[1]/li[3]/a/span").get_attribute(
            'value')
        print(element_txt)
        time.sleep(5)

class AutoBuyMe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("C:\\Users\\natan\\Documents\\ChromeDriver\\chromedriver.exe"))
        self.driver.get('https://buyme.co.il/')
        self.driver.implicitly_wait(10)
        self.registration = LoginPage(self.driver)

    def test_1_registration(self):
        self.registration.test_registration()

