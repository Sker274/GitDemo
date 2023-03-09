from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radio = (By.ID, "inlineRadio1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")
    date = (By.CSS_SELECTOR, "input[name='bday']")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckoutPage(self.driver)
        return check_out_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_radio(self):
        return self.driver.find_element(*HomePage.radio)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_alert(self):
        return self.driver.find_element(*HomePage.alert)

    def get_date(self):
        return self.driver.find_element(*HomePage.date)