from typing import Annotated

from fastapi import APIRouter, Form, HTTPException

from ..scraper import functions as fun, errors as err


router = APIRouter()


@router.post('/login')
async def log_in(username: Annotated[str, Form()], domain: Annotated[str, Form()], password: Annotated[str, Form()]):
    try:
        fun.login(username, domain, password)
    except err.InvalidCredentialsException as e:
        raise HTTPException(status_code=500, detail=e.args[0])
    except err.InvalidDomainException as e:
        raise HTTPException(status_code=404, detail=e.args[0])
    return {'message': 'success'}
