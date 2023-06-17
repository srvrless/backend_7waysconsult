from ast import Dict
import os
from typing import Any
from dotenv import load_dotenv
from pydantic import BaseSettings, PostgresDsn, validator


load_dotenv()


class Settings(BaseSettings):
    API: str = "/api"

    DATABASE_URI: PostgresDsn | None = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls,
        value: str | None,
    ) -> str:
        if isinstance(value, str):
            return value
        DB_HOST = os.environ.get("DB_HOST")
        DB_PORT = os.environ.get("DB_PORT")
        DB_USER = os.environ.get("DB_USER")
        DB_NAME = os.environ.get("DB_NAME")
        DB_PASSWORD = os.environ.get("DB_PASS")
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            path=f"/{DB_NAME}",
        )

    class Config(object):
        case_sensitive = True


settings = Settings()
