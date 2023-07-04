# Informe de salida

## Resumen Ejecutivo

A continuación se describen los resultados del proyecto Music Generation desarrollado durante el tercer módulo del diplomado en Machine Learning and Data Science avanzado.

## Resultados del proyecto

- En cada etapa se entregaron los documentos requeridos en formato .ipynb y .py, además se utilizó el formato sugerido para realizar las contribuciones en cada etapa del proyecto 
- El modelo final, basado en una red neuronal LSTM, alcanzó una exactitud de 0.57 en los datos de validación, lo cual es aceptable para la generación de música automática.
- Se pudieron generar melodías en formato MIDI las cuales tienen algunos elementos característicos del compositor elegido (Edvard Grieg) pero son muy diferentes e incluso en ocasiones se escuchan notas "equivocadas" o armonías que no son convencionales en el estilo romántico-nacionalista, en el cual está enmarcada la obra del compositor estudiado.

## Lecciones aprendidas

- La gran cantidad de datos que se generan a partir de los archivo MIDI impidió que se pudieran incluir en el proyecto otros compositores o más obras del compositor estudiado. 
- En la selección de los archivos MIDI se observó que si el estilo compositivo no es muy uniforme, se obtienen exactitudes muy bajas, alrededor de 0.2, por lo cual se decidió utilizar las composiciones de Edvard Grieg para el presente proyecto
- En la generación de música automática se tienen mejores resultados si los datos utilizados en el modelo LSTM son uniformes en cuanto a género y estilo y a sus elementos compositivos, ya que de lo contrario se producen composiciones automáticas con sonidos que un oyente podría identificar como notas equivocadas o armonías extrañas.

## Impacto del proyecto

- La música generada automáticamente puede emplearse como base para composiciones más elaboradas en la industria del entretenimiento, videojuegos, cine, entre otros.

## Conclusiones

- Se logró implementar un modelo LSTM para la generación de música automática.
- El modelo se desplegó mediante fastAPI en dónde el usuario puede descargar el archivo MIDI generado automáticamente con el número de notas deseado como parámetro.

