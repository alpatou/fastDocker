import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    enviroment: str = os.getenv("ENVIROMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
