from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countries = (By.XPATH, "//div[@class='suggestions']/ul")
    conditions = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CSS_SELECTOR, ".alert")

    def get_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def get_countries(self):
        return self.driver.find_elements(*ConfirmPage.countries)

    def get_conditions(self):
        return self.driver.find_element(*ConfirmPage.conditions)

    def get_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def get_alert(self):
        return self.driver.find_element(*ConfirmPage.alert)