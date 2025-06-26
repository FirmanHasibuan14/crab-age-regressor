from fastapi import FastAPI
from routers import predict
from core.config import setting
from database.connection import create_tables

create_tables

app = FastAPI(
    title = setting.APP_NAME
)

app.include_router(predict.router, prefix="/predict", tags=['Predict'])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Crab Age Prediction API. Go to /docs for documentation."}