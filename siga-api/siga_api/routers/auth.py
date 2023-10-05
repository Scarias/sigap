from fastapi import APIRouter, HTTPException

from .models import User
from ..scraper import functions as fun, errors as err


router = APIRouter()


@router.post('/login')
async def log_in(user: User):
    try:
        fun.login(user.username, user.domain, user.password)
    except err.InvalidCredentialsException as e:
        raise HTTPException(status_code=500, detail=e.args[0])
    except err.InvalidDomainException as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    return {'message': 'success'}
