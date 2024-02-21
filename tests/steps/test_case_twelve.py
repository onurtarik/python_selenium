import time

import pytest

from tests.pages.cart_page import CartPage
from tests.pages.home_page import HomePage
from tests.pages.product_page import ProductPage


class TestAddProductInCart:

    @pytest.mark.all
    def test_add_product_in_cart(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        assert home_page.expected_url == home_page.current_url
        home_page.click_products_button()
        product_page = ProductPage(driver)
        product1_details = product_page.get_detail_product(1)
        product2_details = product_page.get_detail_product(2)
        product_page.hover_over_and_click_product(1)
        time.sleep(3)
        product_page.click_continue_shopping()
        time.sleep(3)
        product_page.hover_over_and_click_product(2)
        product_page.click_view_cart()
        cart_page = CartPage(driver)
        cart1_details = cart_page.get_detail_product(1)
        cart2_details = cart_page.get_detail_product(2)
        assert cart1_details == product1_details
        assert cart2_details == product2_details

