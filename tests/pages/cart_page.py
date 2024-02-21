from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    __second_product_detail = (By.ID, "product-2]")
    __first_product_detail = (By.ID, "product-1")

    def get_detail_product(self, product_number):
        if product_number == 1:
            return   super()._get_product_detail(self.__first_product_detail)
        elif product_number == 2:
            return super()._get_product_detail(self.__second_product_detail)