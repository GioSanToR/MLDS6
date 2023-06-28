import tensorflow as tf
import numpy as np
from music21 import *

from fastapi import FastAPI
from fastapi.response import FileResponse
from pydantic import BaseModel

file_path = '/GioSanToR/MLDS6/tree/main/src/nombre_paquete/deployment'

model = tf.keras.models.load_model('LSTM.h5')

app = FastAPI()

class UserInput(BaseModel):
    user_input: int

@app.get('/')
async def index():
    return {"Message": "Alive"}

@app.post('/midi/')
async def predict(UserInput: UserInput):
    if user_input > 0:
      prediction = midi_gen([UserInput.user_input])
    else:
      return ("número inválido de notas")

    return FileResponse(path = file_path, filename = prediction)
