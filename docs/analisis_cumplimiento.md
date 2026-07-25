# Análisis de cumplimiento

| Paso | Exigencia | Evidencia en el notebook |
|---|---|---|
| 1 | SparkSession y SparkContext | Variables `spark` y `sc` |
| 2 | RDD con 6 particiones, unión, conteo y DataFrame | `deportista`, `deportista2`, `deportistaTotal`, `cantidad_deportistas` y DataFrame `deportista` |
| 3 | Mayores de edad, mujeres y mayúsculas | `MayorEdad`, `Deportistas_mujer` y `Deportistas_mayusculas` |
| 4 | Cuatro DataFrames, caché e integración | `Evento`, `Resultado`, `Equipos`, `Juego`, llamadas `.cache()` y `dataframe_maestro` |
| 5 | Cinco particiones | `dataframe_maestro.repartition(5)` |
| 6 | Filas, tipos y esquema | `count()`, `dtypes` y `printSchema()` |
| 7 | IMC y descripción del sexo | Columnas `IMC` y `Descripción_sexo` |
| 8 | Agregaciones | `medallas_por_equipo`, `estadisticas_edad_medalla`, `temporada` y `sexo` |

## Tratamientos de calidad de datos

- Se tolera una fila de deportista con una columna vacía adicional.
- Los valores `#N/A` en identificadores de eventos se convierten en nulos.
- Los eventos con comillas irregulares son interpretados con `csv.reader`.
- Los equipos no encontrados se conservan como `Equipo no informado`.
- El archivo de juegos se normaliza para que `temporada` represente Verano o Invierno.

## Nomenclatura

`mcdi502_s2_g3.ipynb` no contiene tildes, espacios ni ñ, usa solamente guiones bajos y tiene menos de 20 caracteres sin considerar la extensión.
