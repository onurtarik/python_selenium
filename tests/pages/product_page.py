from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.base_page import BasePage


class ProductPage(BasePage):
    __product_items_first = (By.XPATH, "//div[@class='features_items']/div[2]//div[@class='product-overlay']//a[.='Add to cart']")
    __product_items_second = (By.XPATH, "//div[@class='features_items']/div[3]//div[@class='product-overlay']//a[.='Add to cart']")
    __continue_shopping = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
    __view_cart = (By.XPATH, "//u[.='View Cart']")
    __second_product_detail = (By.XPATH, "//div[@class='features_items']/div[3]")
    __first_product_detail = (By.XPATH, "//div[@class='features_items']/div[2]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def hover_over_and_click_product(self, product_number):
        if product_number == 1:
            super()._hover_over(self.__product_items_first)
        elif product_number == 2:
            super()._hover_over(self.__product_items_second)

    def click_continue_shopping(self):
        super()._click(self.__continue_shopping)

    def click_view_cart(self):
        super()._click(self.__view_cart)

    def get_detail_product(self, product_number):
        texts = None
        if product_number == 1:
            texts = self._get_product_detail(self.__first_product_detail)
        elif product_number == 2:
            texts = self._get_product_detail(self.__second_product_detail)

        return texts
