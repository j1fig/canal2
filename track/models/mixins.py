from sqlalchemy import Column, Datetime, func


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())
