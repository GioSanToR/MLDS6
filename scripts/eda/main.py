from music21 import *
import glob
import numpy as np
import random
import matplotlib.pyplot as plt 

def extract_notes(file):
  notes=[]
  pick=None
  #convertimos el archivo midi
  midi=converter.parse(file)
  #separamos los instrumentos del archivo
  instrmt=instrument.partitionByInstrument(midi)

  for part in instrmt.parts:
    #separamos los datos solamente para piano
    if 'Piano' in str(part):
      pick=part.recurse()

      #se itera sobre los elementos
      #Se verifica si el elemento es nota o acorde, en caso de este último se separa en notas
      
      for element in pick:
        if type(element)==note.Note:
          notes.append(str(element.pitch))
        elif type(element)==chord.Chord:
          notes.append('.'.join(str(n) for n in element.normalOrder))

  #retornamos una lista de las notas
  return notes

file_path=["music/grieg"]
all_files=glob.glob(file_path[0]+'/*.mid',recursive=True)
#conformamos el corpus con los archivos MIDI preprocesados
corpus = np.array([extract_notes(i) for i in all_files], dtype=object)

#notas únicas
notess = sum(corpus,[])
unique_notes = list(set(notess))
print("Unique Notes:",len(unique_notes))
#notas con su frecuencia
freq=dict(map(lambda x: (x,notess.count(x)),unique_notes))
recurrence = list(freq.values())
for i in range(30,200,20):
  print(i,":",len(list(filter(lambda x:x[1]>=i,freq.items()))))
#gráfica
plt.figure(figsize=(18,3))
bins = np.arange(30,max(recurrence), 50) 
plt.hist(recurrence, bins=bins, color="#97BACB")
plt.title("Distribución de las notas")
plt.xlabel("Frecuencia")
plt.ylabel("Número de notas")
plt.show()
