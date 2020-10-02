from typing import Optional
from fastapi import FastAPI
from torch import FloatTensor
from evaluator import evaluator


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/predict")
def read_anomaly(input: str):
    # Read file details from the request
    input = input[1:-1].replace(',', '')
    input = input.split()
    input = [float(x) for x in input]
    input = FloatTensor(input)

    # Run evaluator on input
    prediction = evaluator(input)

    return {
        "prediction": prediction
    }
