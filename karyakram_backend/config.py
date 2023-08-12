from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    # DB
    db_hostname: str
    db_port: str
    db_password: str
    db_name: str
    db_username: str

    class Config:
        env_file = ".env"


settings = Settings()
