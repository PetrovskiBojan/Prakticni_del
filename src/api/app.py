from fastapi import FastAPI, Request
import joblib
import json

app = FastAPI()

model = joblib.load("models/dropout_model.joblib")

@app.get("/")
def read_root():
    return {"message": "Prakticni del!"}

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    X = [list(data.values())]
    prediction = model.predict(X)[0]

    with open("README.md", "a") as f:
        f.write(f"\n## New Prediction\nInput: {json.dumps(data)}\nPrediction: {prediction}\n")

    return {"predicted_class": prediction}
