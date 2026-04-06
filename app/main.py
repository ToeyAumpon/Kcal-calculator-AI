from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io

from .model import predict
from .calorie_db import CALORIE_DB

app = FastAPI(title="LitteFood AI API")

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.post("/predict")
async def predict_food(file: UploadFile = File(...)):

    img_bytes = await file.read()
    image = Image.open(io.BytesIO(img_bytes))
    food_name, confidence = predict(image)
    kcal = CALORIE_DB.get(food_name, 0)

    return{
        "food": food_name,
        "confidence":round(confidence,2),
        "kcal_per_100g":kcal,
        "portion_note":"Esimate assumes 100g. Adjust for actual portion."
    }





