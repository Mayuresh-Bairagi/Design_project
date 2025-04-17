from fastapi import FastAPI, HTTPException, UploadFile,File
from models.fruit_quality import FruitQualityModel
from models.fruit_counting import FruitCounter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from typing import Literal, Annotated
from fastapi.responses import JSONResponse
import os
import shutil
from models.groq_model.groqmodel import GroqModel


app = FastAPI(title="Fruit Quality API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


fc= FruitCounter()
fq = FruitQualityModel()
gm = GroqModel()


@app.get("/")
def home():
    return {"message": "Welcome to the Fruit Quality API"}


@app.post("/predict_quality")
async def predict_quality(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open (file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        result = fq.predict_image(file_path)

        os.remove(file_path)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/count_fruits")
async def count_fruits(file: UploadFile = File(...)):
    try :
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open (file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        result = fc.count_fruits(file_path)

        os.remove(file_path)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/groq_model_sugeestion")
async def groq_model_sugeestion(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open (file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        result = gm.get_suggestions(file_path)

        os.remove(file_path)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))