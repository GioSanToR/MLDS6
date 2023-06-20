# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo para la generación de música consiste en un modelo de Deep Learning con dos capas LSTM, dos capas de Dropout y dos capas densas con activaciones relu y softmax respectivamente.

![model](https://github.com/GioSanToR/MLDS6/assets/126033865/6a1a165a-6f2d-47ab-940a-77b76c47d176)

## Variables de entrada

Los datos de entrada consisten en las notas de los archivos MIDI procesados

## Variable objetivo

Los datos de salida consisten en las notas generadas por el modelo

## Evaluación del modelo

### Métricas de evaluación

Para evaluar el modelo se utiliza la métrica Accuracy

### Resultados de evaluación

Se utilizó Keras Tuner para la búsqueda de hiperparámetros obteniendo una valor de 288 para las unidades de las capas LSTM y una tasa de aprendizaje de 0.003, con lo cual se obtiene un accuracy de 0.56 en los datos de validación (con un optimizador Adam y 100 epochs)

## Análisis de los resultados

El modelo presenta una predicción de las notas aceptable para la generación de música a partir de los archivos MIDI analizados.

## Conclusiones

Se recomienda aumentar el número de Epochs durante el entrenamiento del modelo y el número de archivos MIDI analizados

## Referencias

Para construir el modelo base se utilizaron las siguiente páginas web:
https://data-flair.training/blogs/automatic-music-generation-lstm-deep-learning/
https://www.kaggle.com/code/deadprstkrish/music-generation-using-lstm


