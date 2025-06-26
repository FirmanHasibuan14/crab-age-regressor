from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.connection import get_db
from schemas.predict import PredictionRequest, PredictResponse, PredictionHistory, PredictionHistoryBase
from service.ml_services import ml_service
from crud.predict import create_prediction, get_predictions

router = APIRouter()

@router.post("/predict", response_model=PredictResponse)
def predict_age_crab(request: PredictionRequest, db: Session = Depends(get_db)):
    try:
        result = ml_service.predict(request)
        predicted_age = result['age']

        history_entry = PredictionHistoryBase(
            sex=request.sex,
            length=request.length,
            diameter=request.diameter,
            height=request.height,
            weight=request.weight,
            shucked_weight=request.shucked_weight,
            viscera_weight=request.viscera_weight,
            shell_weight=request.shell_weight,
            age=predicted_age  
        )

        create_prediction(db=db, prediction=history_entry)

        return PredictResponse(age=predicted_age)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Terjadi kesalahan internal: {e}")

@router.get("/history", response_model=List[PredictionHistory])
def read_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    history = get_predictions(db, skip=skip, limit=limit)
    return history