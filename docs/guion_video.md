# Guion sugerido para el video grupal

Duración objetivo: **8 minutos**. Todos los integrantes deben compartir pantalla o intervenir verbalmente.

## 0:00–0:40 — Introducción — Integrante 1

- Presentar la asignatura, el objetivo del taller y los cinco conjuntos de datos.
- Explicar que Resultado es la tabla central que conecta deportistas, equipos, juegos y eventos.

## 0:40–2:20 — Configuración y RDDs — Integrante 1

- Mostrar la instalación de Java y PySpark.
- Presentar `SparkSession` y `SparkContext`.
- Explicar el RDD `deportista` con seis particiones, el RDD `deportista2` y la unión `deportistaTotal`.
- Mostrar el conteo y las transformaciones: mayoría de edad, mujeres y mayúsculas.

## 2:20–4:10 — DataFrames y calidad de datos — Integrante 2

- Explicar los esquemas explícitos.
- Mostrar la limpieza de la fila irregular de deportistas.
- Explicar por qué `evento.csv` necesita un parser especial.
- Mostrar el tratamiento de `#N/A` en resultados y la normalización de temporada en el JSON.

## 4:10–5:40 — Integración y optimización — Integrante 3

- Explicar los joins desde Resultado.
- Justificar `cache`, `persist`, AQE y los `broadcast joins`.
- Mostrar el DataFrame integrado y el reparticionamiento a cinco particiones.
- Enseñar cantidad de filas, tipos y esquema.

## 5:40–7:20 — Columnas y Spark SQL — Integrante 4

- Explicar el cálculo de IMC y el tratamiento de valores cero como faltantes.
- Mostrar `Descripción_sexo`.
- Presentar las cuatro consultas: medallas por equipo, edades por medalla, alturas por temporada y edades por sexo.
- Enseñar brevemente el plan con `explain`.

## 7:20–8:00 — Cierre — Todos

- Resumir cómo se cumplieron los indicadores 3.1, 3.2, 3.3 y 3.4.
- Mencionar las decisiones técnicas más importantes.
- Confirmar que el Notebook se ejecuta secuencialmente y contiene validaciones automáticas.
