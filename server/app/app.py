from fastapi import FastAPI
from routers.router import api_router
from db import settings

def create_app() -> FastAPI:
    app = FastAPI(
        contact=dict(
            name="Telegram",
            url="https://www.telegram.org/@Holucrap",
            email="maijor18@mail.ru",
        ),)

    app.include_router(api_router, prefix=settings.API)

    return app
