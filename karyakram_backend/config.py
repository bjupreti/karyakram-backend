from pydantic import BaseSettings
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv() 

class Settings(BaseSettings):
    # DB
    db_hostname: str
    db_port: str
    db_password: str
    db_name: str
    db_username: str

    class Config:
        env_file = '.env'

settings = Settings()
