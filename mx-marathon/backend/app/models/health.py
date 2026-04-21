from sqlalchemy import Column, Integer, Float, Date
from app.db import Base

class HealthMetric(Base):
    __tablename__ = "health_metrics"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    hrv = Column(Integer)
    sleep = Column(Float)
    fatigue = Column(Integer)
