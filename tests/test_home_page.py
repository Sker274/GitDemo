import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        log.info("First name is " + get_data["firstname"])
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys([get_data["email"]])

        homepage.get_password().send_keys("123456")
        homepage.get_checkbox().click()

        # Static dropdown
        self.select_dropdown_option(homepage.get_dropdown(), get_data["gender"])

        homepage.get_radio().click()

        homepage.get_date().send_keys("18")
        homepage.get_date().send_keys("01")
        homepage.get_date().send_keys("1998")

        homepage.get_submit().click()
        message = homepage.get_alert().text
        print(message)
        assert "Success" in message
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_data(self, request):
        return request.param