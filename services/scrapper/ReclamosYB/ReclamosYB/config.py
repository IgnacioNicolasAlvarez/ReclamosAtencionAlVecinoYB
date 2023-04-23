import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_ID = os.getenv("PROJECT_ID")


settings = Settings()
