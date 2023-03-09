from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    card_title = (By.XPATH, "//div[@class='card h-100']")
    cart = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    check_out = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def get_card_title(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    def get_cart(self):
        return self.driver.find_element(*CheckoutPage.cart)

    def get_check_out(self):
        self.driver.find_element(*CheckoutPage.check_out).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
