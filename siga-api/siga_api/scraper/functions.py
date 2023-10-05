from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .errors import *


def login(username: str, domain: str, password: str):
    with webdriver.Firefox() as driver:
        # Navigate
        driver.get('https://siga.usm.cl/pag/home.jsp')

        # Get & fill username
        username_field = driver.find_element(By.NAME, 'login')
        username_field.send_keys(username)

        # Get & fill domain
        domain_field = Select(driver.find_element(By.NAME, 'server'))
        if domain not in domain_field.options:
            raise InvalidDomainException(f'Client domain "{domain}" not exists.')

        domain_field.select_by_value(domain)

        # Get & fill passwrod
        password_field = driver.find_element(By.NAME, 'passwd')
        password_field.send_keys(password)

        # Try login
        login_btn = driver.find_element('//*[@id="val_login"]/table/tbody/tr/td[3]/table/tbody/tr[2]/td[3]/a')
        login_btn.click()

        # Raise exceptions on error
        if driver.current_url == 'https://siga.usm.cl/pag/error_ingreso_login.jsp':
            raise InvalidCredentialsException('Username not exists or password isn\'t valid')
