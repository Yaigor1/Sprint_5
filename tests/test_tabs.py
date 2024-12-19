import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.mark.usefixtures("driver")
class TestTabs:

    def test_constructor_sauce(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.sauces_tab).click()
        assert self.is_tab_active(driver, Locators.sauces_tab_div)

    def test_constructor_buns(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.sauces_tab).click()
        driver.find_element(*Locators.buns_tab).click()
        assert self.is_tab_active(driver, Locators.buns_tab_div)

    def test_constructor_filling(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.filling_tab).click()
        assert self.is_tab_active(driver, Locators.filling_tab_div)
