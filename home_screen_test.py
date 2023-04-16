from selenium.webdriver.common.by import By
from basePage import BasePage
import time


class Constants:
    LOCATOR = By.XPATH


class HomeScreen(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_pick_info(self):
        self.click_element(Constants.LOCATOR, "//span[@title='סכום']")  # Clicking Drop sown list
        self.click_element(Constants.LOCATOR, "//li[@value='6']")    # Choosing from the DDL
        self.click_element(Constants.LOCATOR, "(//span[@title='אזור'])[1]") # Clicking Drop sown list
        self.click_element(Constants.LOCATOR, "//*[@value='13']/span")  # Choosing from the DDL
        self.click_element(Constants.LOCATOR, "(//span[@ title='קטגוריה'])[1]")   # Clicking Drop sown list
        self.click_element(Constants.LOCATOR, "//li[@value = '85']")  # Choosing from the DDL
        self.click_element(Constants.LOCATOR, "//*[@rel = 'nofollow']")   # Clicking search Button

