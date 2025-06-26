from fastapi import FastAPI
from routers import predict
from core.config import Settings
from database.connection import create_tables

create_tables

app = FastAPI(
    title = Settings.APP_NAME
)

app.include_router(predict.router, prefix="/predict", tags=['Predict'])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Crab Age Prediction API. Go to /docs for documentation."}