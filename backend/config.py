import os


class Config:
    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost/ok"
    )


config = Config()
