from fastapi import FastAPI
from torch import FloatTensor
from torchmodels.evaluator import evaluator

# Instantiate app
app = FastAPI()

# Root call
@app.get("/")
def read_root():
    return {"status": "ready"}

# Prediction endpoint
@app.get("/predict")
def read_anomaly(input: str):
    # Parse input string to extract data
    input = input[1:-1].replace(',', '')
    input = input.split()
    input = [float(x) for x in input]
    input = FloatTensor(input)

    # Run evaluator on input
    prediction = evaluator(input)

    return {
        "prediction": prediction
    }
