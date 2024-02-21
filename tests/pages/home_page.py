from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.base_page import BasePage


class HomePage(BasePage):
    __home_page_url = "https://automationexercise.com/"
    __products_button = (By.XPATH, "//a[.=' Products']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__home_page_url)

    @property
    def expected_url(self) -> str:
        return self.__home_page_url

    def click_products_button(self):
        super()._click(self.__products_button)
