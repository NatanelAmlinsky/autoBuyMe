import unittest
from unittest import TestCase
from selenium.webdriver.chrome.options import Options
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from registration_test import Registration
from home_screen_test import HomeScreen
from pick_business_test import PickBusiness
from sender_receiver_info_screen_test import InfoScreen
from extras_test import Extras
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AutoBuyMe(TestCase):

    def setUp(self):
        self.chrome_option = Options()
        self.chrome_option.add_argument("--start-maximized")  # using Options class for "start maximized" the browser
        self.chrome_option.add_argument("--disable-popup-blocking")  # disable pop-up blocking
        json_file = open('configuration.json', 'r')  # open the json file
        data = json.load(json_file)  # loading the json content to the variable "data"
        browser = data['browserType']
        url = data['url']
        if browser == 'chrome' and url == "https://buyme.co.il/":
            self.driver = webdriver.Chrome(service=Service("C:\\Users\\natan\\Documents\\ChromeDriver\\chromedriver.exe"), options=self.chrome_option)
            self.driver.get('https://buyme.co.il/')
            json_file.close()
        elif browser == 'firefox' and url == "https://buyme.co.il/":
            self.driver = webdriver.Firefox(service=Service("C:\\Program Files\\GeckoDriver\\geckodriver.exe"))
            self.driver.get('https://buyme.co.il/')
            json_file.close()  # reading the json content and define the driver and url for the program

        self.driver.implicitly_wait(10)

        self.registration_test = Registration(self.driver)
        self.home_screen_test = HomeScreen(self.driver)
        self.pick_business_test = PickBusiness(self.driver)
        self.test_sender_receiver_info_screen = InfoScreen(self.driver)
        self.extras = Extras(self.driver)

    def test_1_registration(self):  # run registration test
        self.registration_test.test_registration()

    def test_2_home_screen(self):   # run home screen test
        self.home_screen_test.test_pick_info()

    def test_3_pick_business(self): # run pick business test
        self.pick_business_test.test_pick_business()

    def test_4_sender_receiver_info_screen(self): # run sender receiver information screen test
        self.test_sender_receiver_info_screen.test_info_screen()

    def test_5_extras(self):    # run extras module test
        self.extras.test_home_screen_error()
        self.extras.test_screenshot_buttom_of_page()

    def tearDown(self): # quiting from the web driver
        self.driver.quit()

