from sqlalchemy import Column, Integer, Float, String, Date
from app.db import Base

class TrainingLog(Base):
    __tablename__ = "training_logs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    distance = Column(Float)
    pace = Column(String)
    rpe = Column(Integer)
    type = Column(String)
    notes = Column(String)
