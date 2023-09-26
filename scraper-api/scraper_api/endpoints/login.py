from scraper_api import app

from scraper_api.scraper import login_user

@app.get('/login')
async def login(user: str, domain: str, password: str):
    result = await login_user(user, domain, password)
    return { 'message': 'login exitoso' if result else 'login fallido' }