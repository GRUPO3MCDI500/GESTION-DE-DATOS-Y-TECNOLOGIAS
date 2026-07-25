# Análisis de cumplimiento

## Estado encontrado

El repositorio contenía una estructura válida, automatización básica y los archivos olímpicos, pero el `README` y el Notebook seguían desarrollando un caso de Copa Mundial con jugadores, partidos, estadios y torneos. Por tanto, no respondían a la Evaluación Sumativa 2.

## Cambios realizados

- Reemplazo del caso Mundial por el modelo olímpico de cinco tablas.
- Reorganización de los archivos en `data/raw/`.
- Nuevo Notebook con el nombre formal `mcdi502_s2_g3.ipynb`.
- Uso real de `deportista.csv` y `deportista2.csv`, sin duplicar una misma fuente.
- RDD inicial con seis particiones y unión completa de 135.571 deportistas.
- Parser robusto para una fila irregular de deportistas y para los eventos entrecomillados.
- Lectura de resultados con separador `;` y conversión de `#N/A` a nulo.
- Normalización de `juegos.json`: `temporada` original contiene el año y `ciudad` contiene Verano/Invierno.
- Integración centralizada a través de Resultado.
- Persistencia, caché, AQE, *broadcast joins* y reparticionamiento a cinco particiones.
- IMC, descripción de sexo y cuatro agregaciones con Spark SQL.
- Guion distribuido para un video de aproximadamente ocho minutos.
- Script y workflow de validación actualizados.

## Decisiones técnicas relevantes

1. **Mayor de edad:** se utiliza `edad >= 18`.
2. **Valores cero:** edad, altura y peso iguales a cero se tratan como faltantes en estadísticas e IMC para evitar sesgos.
3. **Resultados sin evento:** nueve filas contienen `#N/A`; se conservan mediante un `left join` para no perder resultados históricos.
4. **Temporada:** se corrige la semántica del JSON para agrupar por Verano/Invierno, no por año.
5. **Optimización:** las tablas pequeñas se transmiten con `broadcast`, mientras las tablas grandes se persisten en memoria y disco.

## Pendiente externo

El único elemento que no puede generarse a partir del repositorio es el video final del equipo. Debe grabarse con la participación de todos los integrantes y guardarse como `mcdi502_s2_g3_video.mp4`.
