from basePage import BasePage
from selenium.webdriver.common.by import By


class PickBusiness(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def test_pick_business(self):
        self.get_url("https://buyme.co.il/search?budget=6&category=85&region=13")
        url = self.get_current_url()
        the_website_url = "https://buyme.co.il/search?budget=6&category=85&region=13"
        self.wait_for_url(the_website_url)
        assert url == the_website_url
        self.click_element(By.XPATH, "(//div[@class='bottom'])[10]")
        self.enter_text(By.XPATH, "//*[@placeholder='הכנס סכום']", "650")
        self.click_element(By.XPATH, "(//div[@class='mx-12 money-btn'])[1]")
