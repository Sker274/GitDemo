from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_end2end(self):
        log = self.get_logger()
        # First page (Home Page)
        home_page = HomePage(self.driver)
        # Second page (Products Page)
        check_out_page = home_page.shop_items()
        log.info("Getting all products")
        products = check_out_page.get_card_title()

        for product in products:
            log.info(product.find_element(By.CSS_SELECTOR, ".card-title").text)
            if product.find_element(By.CSS_SELECTOR, ".card-title").text == "Blackberry":
                product.find_element(By.CSS_SELECTOR, "button[class='btn btn-info']").click()

        check_out_page.get_cart().click()
        # Third page (Checkout Page / Confirm Page)
        confirm_page = check_out_page.get_check_out()

        log.info("Entering country as slo")
        confirm_page.get_country().send_keys("slo")
        self.verify_link_presence("Slovakia")
        countries = confirm_page.get_countries()
        print(len(countries))

        for country in countries:
            if country.text == "Slovakia":
                country.click()
                break

        confirm_page.get_conditions().click()
        confirm_page.get_purchase().click()
        alert = confirm_page.get_alert().text
        log.info("Text received from application is: " + alert)
        print(alert)