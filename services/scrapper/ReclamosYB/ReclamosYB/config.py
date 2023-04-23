import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_ID = os.getenv("PROJECT_ID")
    START_URL = os.getenv("START_URL")
    DEFAULT_URL = os.getenv("DEFAULT_URL")
    ALLOWED_DOMAIN = os.getenv("ALLOWED_DOMAIN")


settings = Settings()
