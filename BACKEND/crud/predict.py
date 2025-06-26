from sqlalchemy.orm import Session
from models.predict import PredictionHistory
from schemas.predict import PredictionHistoryBase

def create_prediction(db: Session, prediction: PredictionHistory) -> PredictionHistoryBase:
    db_entry = PredictionHistory(**prediction.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_predictions(db: Session, skip: int = 0, limit: int = 100) -> list[PredictionHistory]:
    return db.query(PredictionHistory).offset(skip).limit(limit).all()