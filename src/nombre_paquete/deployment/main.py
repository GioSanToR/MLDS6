import numpy as np
from music21 import *
import tensorflow as tf
import pickle

x_test = np.load('x_test_saved.npy')

with open('ind2note.pkl', 'rb') as fp:
    ind2note = pickle.load(fp)

def note_prediction(n): #n se refiere al número de notas generadas
  #cargamos el modelo
  model = tf.keras.models.load_model("LSTM.h5")
  #generamos un índice aleatoriamente
  index = np.random.randint(0,len(x_test)-1)
  #Datos generados a partir del index de x_test
  music_pattern = x_test[index]
  out_pred=[]

  for i in range(n):
    #redimensionamos la variable music_pattern
    music_pattern = music_pattern.reshape(1,len(music_pattern),1)
    #Buscamos los valores con mayor probabilidad
    pred_index = np.argmax(model.predict(music_pattern))
    out_pred.append(ind2note[pred_index])
    music_pattern = np.append(music_pattern,pred_index)
    #Actualizamos music_pattern con un intervalo entre notas más adelante
    music_pattern = music_pattern[1:]
  return out_pred


def midi_gen(n):
  output_notes = []
  for offset,pattern in enumerate(note_prediction(n)):
    #si el patrón es un acorde
    if ('.' in pattern) or pattern.isdigit():
      #dividimos las notas del acorde
      notes_in_chord = pattern.split('.')
      notes = []
      for current_note in notes_in_chord:
          i_curr_note=int(current_note)
          new_note = note.Note(i_curr_note)
          new_note.storedInstrument = instrument.Piano()
          notes.append(new_note)

      new_chord = chord.Chord(notes)
      new_chord.offset = offset
      output_notes.append(new_chord)

    else:
      #aplicamos el offset
      new_note = note.Note(pattern)
      new_note.offset = offset
      new_note.storedInstrument = instrument.Piano()
      output_notes.append(new_note)

  #guardamos el archivo MIDI
  midi_stream = stream.Stream(output_notes)
  preds = midi_stream.write('midi', fp='pred_music.mid')
  return preds

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
async def index():
    return {"Message": "Alive"}

@app.get("/midi/{notes}/", response_class=FileResponse)
async def generate(notes: int):
   if notes > 0:
      return midi_gen(notes)
