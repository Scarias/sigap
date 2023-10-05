from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class User(BaseModel):
    username: str
    domain: str
    password: str


@router.get('/menu')
async def get_menu_options():
    return {'result': 'done'}
