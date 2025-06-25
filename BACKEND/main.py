from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Crab Age Prediction API. Go to /docs for documentation."}