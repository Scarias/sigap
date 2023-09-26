# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotVisibleException

from scraper_api.scraper import driver

async def login_user(user, domain, password):
    driver.get('https://siga.usm.cl/')

    # Fill fields

    user_field = driver.find_element(By.NAME, 'login')
    domain_field = Select(driver.find_element(By.NAME, 'server'))
    password_field = driver.find_element(By.NAME, 'passwd')

    user_field.send_keys(user)
    domain_field.select_by_value(domain)
    password_field.send_keys(password)

    print(user, domain, password)

    # Click button

    login_button = driver.find_element(By.XPATH, '//*[@id="val_login"]/table/tbody/tr/td[3]/table/tbody/tr[2]/td[3]/a')
    login_button.click()

    print(login_button)

    try:
        driver.find_element()
        return True
    except ElementNotVisibleException:
        return False
