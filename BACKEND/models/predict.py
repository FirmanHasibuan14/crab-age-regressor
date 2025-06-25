from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database.connection import Base

class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sex = Column(String)
    length = Column(Float)
    diameter = Column(Float)
    height = Column(Float)
    weight = Column(Float)
    shucked_weight = Column(Float)
    viscera_weight = Column(Float)
    shell_weight = Column(Float)

    age = Column(Integer)
