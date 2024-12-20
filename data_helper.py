import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_random_email():
    random_number = random.randint(100, 999)
    email = f"ilya.stepanov.16.{random_number}@yandex.ru"
    return email


def get_random_password(valid: bool = True):
    if valid:
        password = random.randint(100000, 999999)
        return password
    else:
        password = random.randint(0, 99999)
        return password

def is_tab_active(driver, locator):
    tab_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locator)
    )
    return "tab_tab_type_current__2BEPc" in tab_element.get_attribute("class")

