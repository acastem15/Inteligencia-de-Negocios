from typing import Optional
from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import os

import re, string, unicodedata

#import functions
#from functions import lemmatizer,tokenizar,softPreprocessing,preprocessing,applyLemmatizer, softPreprocessingTransformer,tokenizarTransformer,applyLemmatizerTransformer,preprocessingTransformer

from tqdm.notebook import tqdm

import re, string, unicodedata
from tqdm.notebook import tqdm

from joblib import load
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

path = os.path.join(os.path.dirname(__file__), 'assets/modelLemmatizer.joblib')
model = load(path)

class ModelParams(BaseModel):
    resena: str
    def columns(self):
        return ['resena']


    

def get_prediction(dataModel):
    print(dataModel,type(dataModel))
    
    df = pd.Series(dataModel.dict())


    y = model.predict(df)[0] 
    print({'prediccion': int(y)})
    return {'prediccion': int(y)}

@app.post("/predicciones")
def predict(params: ModelParams):
    print(params)

    pred = get_prediction(params)

    return pred

@app.get("/predicciones/ping")
def ping():
    return "Pong!"