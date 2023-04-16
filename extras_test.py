import time
from selenium.webdriver.common.by import By
from basePage import BasePage


class Constants:
    LOCATOR_XPATH = By.XPATH


class Extras(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_home_screen_error(self):
        self.click_element(Constants.LOCATOR_XPATH, "//span[@tuafontsizes='14']")
        self.click_element(Constants.LOCATOR_XPATH, "//button[@type='submit']")
        alert = self.find_and_return_web_elm_text(Constants.LOCATOR_XPATH, "//li[@class='parsley-required']")
        assert alert == 'כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה'

    def test_screenshot_buttom_of_page(self):
        self.get_url('https://buyme.co.il/')
        time.sleep(1)
        self.scroll_down_and_screenshot()
