import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class CustomMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class Group(Base, CustomMixin):
    __tablename__ = "group"

    name: Mapped[str] = mapped_column(String(35), nullable=False)
    description: Mapped[str] = mapped_column(String(128), nullable=False)


class User(Base, CustomMixin):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(35), nullable=False)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(256), nullable=False)


class Activity(Base, CustomMixin):
    __tablename__ = "activity"

    name: Mapped[str] = mapped_column(String(35), nullable=False)
    description: Mapped[str] = mapped_column(String(128), nullable=False)
    date_time: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)


class Channel(Base, CustomMixin):
    __tablename__ = "channel"

    name: Mapped[str] = mapped_column(String(35), nullable=False)
    summary: Mapped[str] = mapped_column(String(128), nullable=False)


class Message(Base, CustomMixin):
    __tablename__ = "message"

    message: Mapped[str] = mapped_column(String(500), nullable=False)
