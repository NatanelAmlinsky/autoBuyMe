from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, value=locator_value).click()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def explicit_wait_click_element(self, locator_type, locator_value):
        # Wait for the element to become clickable
        try:
            self.wait = WebDriverWait(self.driver, 10)
            element = self.wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            # Click the element
            element.click()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_text(self, locator_type, locator_value, text):
        try:
            self.driver.find_element(locator_type, value=locator_value).send_keys(text)
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_element_txt(self,locator_type, locator_value):
        try:
            element_txt = self.driver.find_element(locator_type, value=locator_value)
            return element_txt.text
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_element(self, locator_type, locator_value):  # find element
        try:
            element = self.driver.find_element(locator_type, value=locator_value)
            return element
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_elements(self, locator_type, locator_value): # find elements
        try:
            element = self.driver.find_elements(locator_type, value=locator_value)
            return element
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def get_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, url):
        wait(self.driver, 10).until(EC.url_to_be(url))

    def clear_text(self, locator_type, locator_value):
        try:
            self.driver.find_element(locator_type, value=locator_value).clear()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def scroll_down(self):  # scroll down in the website using java-script executor
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def go_to_last_page(self):  # go back to last website page
        self.driver.back()

    def scroll_down_and_screenshot(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def find_and_return_web_elm_text(self, locator_type, locator_value):  # find element and return text
        try:
            element = self.driver.find_element(locator_type, value=locator_value)
            return element.text

        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
