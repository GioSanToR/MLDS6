from music21 import *
import glob
import numpy as np
import random

umbral = 50
freq_notes=dict(filter(lambda x:x[1]>=umbral,freq.items()))
#creamos nuevas notas usando la frecuencia 
new_notes=[[i for i in j if i in freq_notes] for j in corpus]

#diccionario con el índice de nota como key y la nota como value
ind2note=dict(enumerate(freq_notes))
#diccionario con la nota como key y el índice de nota como value
note2ind=dict(map(reversed,ind2note.items()))
print(ind2note.items())
print(len(note2ind))
