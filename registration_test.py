import time

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from basePage import BasePage
import allure


class Constants():
    XPATH_LOCATOR = By.XPATH
    LOGIN_BUTTON = "//*[@id='ember1005']/div/ul[1]/li[3]/a/span"
    REGISTRATION_BUTTON = "//*[@id='ember964']/div/div[1]/div[2]/div/div[3]/div[1]/span"
    NAME_TXTBOX_LOCATOR = "//*[@id='ember1875']"


class Registration(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_registration(self):
        self.click_element(Constants.XPATH_LOCATOR, Constants.LOGIN_BUTTON)
        self.click_element(Constants.XPATH_LOCATOR, Constants.REGISTRATION_BUTTON)
        self.enter_text(Constants.XPATH_LOCATOR, Constants.NAME_TXTBOX_LOCATOR , "Netanel")
        self.enter_text(Constants.XPATH_LOCATOR, "//*[@id='ember1882']", "bznatik128@gmail.com")  # finding email text box locator and entering the email text.
        self.enter_text(Constants.XPATH_LOCATOR, "//*[@id='valPass']", "Sisma123")  # finding paswword text box locator and entering the password text.
        self.enter_text(Constants.XPATH_LOCATOR, "//*[@id='ember1896']", "Sisma123")    # finding renter paswword text box locator and entering the password text again.
        name_txt = self.find_element(Constants.XPATH_LOCATOR, Constants.NAME_TXTBOX_LOCATOR).get_attribute('value')
        assert name_txt == 'Netanel'
        self.click_element(By.XPATH, "(//*[name()='circle'][@class='fill'])[1]")    # check vi on the checkbox
        self.click_element(By.XPATH, "(// button[@ id='ember1906'])[1]")    # Enter the final registration button





