from typing import Optional
from fastapi import FastAPI
import pandas as pd
from joblib import load
from pydantic import BaseModel
import os

app = FastAPI()

path = os.path.join(os.path.dirname(__file__), 'assets/modelLemmatizer.joblib')
model = load(path)

class ModelParams(BaseModel):
    resena: str

def get_prediction(resena):
    
    x = [[resena]]

    y = model.predict(x)[0] 
    prob = model.predict_proba(x)[0].tolist() 

    return {'prediccion': int(y), 'probabilidad': prob}

@app.post("/predicciones")
def predict(params: ModelParams):

    pred = get_prediction(params.resena)

    return pred

@app.get("/predicciones/ping")
def ping():
    return "Pong!"