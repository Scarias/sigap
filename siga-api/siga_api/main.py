from fastapi import FastAPI

from .routers import menu, auth


# App creation with security
app = FastAPI()

# Add routers
app.include_router(auth.router)
app.include_router(menu.router)
