from sqlalchemy import Column, DateTime, func


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())
