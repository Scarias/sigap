# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from scraper_api.scraper import driver


async def get_schedule():
    driver.get('https://siga.usm.cl/pag/sistemas.jsp')

    schedule = {
        'lunes': dict.fromkeys([ str(i) for i in range(1,21) ], None),
        'martes': dict.fromkeys([ str(i) for i in range(1,21) ], None),
        'miércoles': dict.fromkeys([ str(i) for i in range(1,21) ], None),
        'jueves': dict.fromkeys([ str(i) for i in range(1,21) ], None),
        'viernes': dict.fromkeys([ str(i) for i in range(1,21) ], None),
        'sábado': dict.fromkeys([ str(i) for i in range(1,21) ], None),
        'domingo': dict.fromkeys([ str(i) for i in range(1,21) ], None),
    }

    if driver.current_url != 'https://siga.usm.cl/pag/sistemas.jsp':
        return
