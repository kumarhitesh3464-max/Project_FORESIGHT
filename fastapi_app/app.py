from fastapi import FastAPI
from schema import PredictionInput
from predict import predict

app = FastAPI(
    title="Project FORESIGHT API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Project FORESIGHT API is Running Successfully 🚀"
    }


@app.post("/predict")
def predict_demand(data: PredictionInput):

    result = predict(data.dict())

    return {
        "Predicted_Demand": result
    }