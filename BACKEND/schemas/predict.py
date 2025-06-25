from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class SexEnum(str, Enum):
    M = "M"
    I = "I"
    F = "F"

class PredictionRequest(BaseModel):
    sex: SexEnum
    length: float
    diameter : float
    height : float
    weight : float
    shucked_weight : float
    viscera_weight : float
    shell_weight : float

class PredictResponse(BaseModel):
    age: int

class PredictionHistoryBase(PredictionRequest):
    age: int

class PredictionHistory(PredictionHistoryBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True