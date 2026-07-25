# Orden de ejecución

Ejecute el notebook de arriba hacia abajo:

1. Detectar Colab e instalar Java 17 y PySpark 4.0.1.
2. Importar librerías y definir variables de entorno.
3. Crear `SparkSession` y `SparkContext`.
4. Localizar o cargar los seis archivos.
5. Crear y unir los RDD.
6. Convertir `deportistaTotal` al DataFrame `deportista`.
7. Ejecutar las transformaciones de RDD.
8. Crear y cachear los cuatro DataFrames restantes.
9. Construir `dataframe_maestro`.
10. Reparticionar a 5 particiones.
11. Inspeccionar filas, tipos y esquema.
12. Crear IMC y Descripción_sexo.
13. Crear la vista temporal `olimpicos`.
14. Ejecutar las cuatro agregaciones.
15. Revisar el plan de ejecución.
16. Ejecutar las validaciones finales.
17. Liberar la caché solamente al terminar.
