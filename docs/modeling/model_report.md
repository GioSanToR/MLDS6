# Reporte del Modelo Final

## Resumen Ejecutivo

En esta sección se presentará un resumen de los resultados obtenidos del modelo final. Es importante incluir los resultados de las métricas de evaluación y la interpretación de los mismos.

## Descripción del Problema

Se busca generar música a partir de archivos MIDI para piano de compositores clásicos y románticos. Para este fin se utilizan modelos de Deep Learning que implementan redes neuronales LSTM (long short-term memory)

## Descripción del Modelo

El modelo para la generación de música final es un modelo de Deep Learning con dos capas LSTM, dos capas de Dropout y dos capas densas con activaciones relu y softmax respectivamente, en el cual se definieron 288 para las unidades de las capas LSTM, durante el entrenamiento se empleó un optimizador Adam con una tasa de aprendizaje de 0.003 y 100 epochs.


## Evaluación del Modelo

Se obtiene un accuracy de 0.56 en los datos de validación.

## Conclusiones y Recomendaciones

El modelo requiere un entrenamiento durante más epochs y más archivos MIDI para mejorar el accuracy en los datos de validación.

## Referencias

En esta sección se deben incluir las referencias bibliográficas y fuentes de información utilizadas en el desarrollo del modelo.
