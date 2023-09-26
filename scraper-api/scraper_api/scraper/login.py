# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from scraper_api.scraper import driver


async def login_user(user, domain, password):
    driver.get('https://siga.usm.cl/')

    # Fill fields

    user_field = driver.find_element(By.NAME, 'login')
    domain_field = Select(driver.find_element(By.NAME, 'server'))
    password_field = driver.find_element(By.NAME, 'passwd')

    if domain not in domain_field.options:
        return False, 'Domain not exists'

    user_field.send_keys(user)
    domain_field.select_by_value(domain)
    password_field.send_keys(password)

    # Click button

    login_button = driver.find_element(By.XPATH, '//*[@id="val_login"]/table/tbody/tr/td[3]/table/tbody/tr[2]/td[3]/a')
    login_button.click()

    try:
        driver.find_element(By.NAME, 'dos')
        return True, 'Success'
    except NoSuchElementException:
        print('Login fail, checking cause')

    try:
        return_button = driver.find_element(By.XPATH, '/html/body/center/a')
        return_button.click()
        return False, 'Incorrect password and/or user/domain'
    except NoSuchElementException:
        return False, 'Unknown error'
