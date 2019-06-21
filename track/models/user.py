from sqlalchemy import Column, Integer, String

from .base import Base
from .mixins import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
