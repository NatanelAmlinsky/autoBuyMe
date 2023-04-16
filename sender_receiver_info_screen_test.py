import time

from basePage import BasePage
from selenium.webdriver.common.by import By

LOCATOR = By.XPATH
RECEIVER_NAME = "Natikiel"


class InfoScreen(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self, driver)

    def test_info_screen(self):

        self.get_url("https://buyme.co.il/money/17573384?price=650")
        # self.click_element(By.XPATH, "//div[@class = 'ember-view button button-forSomeone']")
        self.enter_text(LOCATOR, "//input[@maxlength='25']", RECEIVER_NAME)
        self.click_element(LOCATOR,"//div[@class='selected-name']")
        self.click_element(LOCATOR, "(//li[@value='10'])")
        self.clear_text(LOCATOR, "//textarea[@data-parsley-id = '7']")
        self.enter_text(LOCATOR, "//textarea[@data-parsley-id = '7']", "Blessings to you my dear!")
        self.enter_text(LOCATOR, '//input[@type="file"]', "C:\\Users\\natan\Desktop\\python_tests\\pic.png")
        self.click_element(LOCATOR, "//button[@class='ember-view bm-btn no-reverse main xl stretch']")
        # self.click_element(LOCATOR, '//div[@gtm="עכשיו"]')
        self.scroll_down()
        svgs = self.find_elements(By.TAG_NAME, 'svg')
        for svg_sms in svgs:  # using for loop to iterate between element with the same attributes
            if svg_sms.get_attribute('gtm') == 'method-sms':
                time.sleep(0.1)
                svg_sms.click()
                break
        time.sleep(1)
        self.scroll_down()
        self.enter_text(LOCATOR,"//input[@ name = 'sms']", "0533305851")
        self.enter_text(LOCATOR, "//input[@maxlength='25']", RECEIVER_NAME)
        self.enter_text(LOCATOR, "// *[ @ placeholder = 'מספר נייד']", "0533305851")
        self.go_to_last_page()
        self.scroll_down()
        receiver_name = self.find_element(LOCATOR, "//input[@maxlength='25']").get_attribute('value')
        assert receiver_name == RECEIVER_NAME
        time.sleep(8)
