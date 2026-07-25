# Evaluación Sumativa 2 — Taller I

Repositorio adaptado para la actividad **MCDI502: Gestión de Datos y Tecnologías**. El caso anterior de la Copa Mundial fue reemplazado por el modelo histórico de los Juegos Olímpicos solicitado en la pauta.

## Integrantes

- Eduardo Garrido
- Luis Espinosa
- Mauricio Ortega
- Wilson Arévalo

## Estructura

```text
GESTION-DE-DATOS-Y-TECNOLOGIAS-adaptado/
├── .github/workflows/validate.yml
├── data/raw/
│   ├── deportista.csv
│   ├── deportista2.csv
│   ├── equipo.csv
│   ├── evento.csv
│   ├── juegos.json
│   └── resultados.csv
├── docs/
│   ├── analisis_cumplimiento.md
│   └── guion_video.md
├── notebooks/
│   └── mcdi502_s2_g3.ipynb
├── scripts/
│   └── validate_repository.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Cobertura de la evaluación

El Notebook incluye:

1. Instalación de Java y PySpark 4.2.0.
2. Creación de `SparkSession` y `SparkContext`.
3. RDD `deportista` con 6 particiones, RDD `deportista2` y unión `deportistaTotal`.
4. Filtros de mayoría de edad y género femenino, además de conversión a mayúsculas.
5. DataFrames de deportistas, eventos, equipos, resultados y juegos con esquemas explícitos.
6. Limpieza de filas irregulares en `evento.csv` y tratamiento de `#N/A` en `resultados.csv`.
7. Caché, persistencia, Adaptive Query Execution y *broadcast joins*.
8. Integración de las cinco tablas y reparticionamiento a 5 particiones.
9. Columnas `IMC` y `Descripción_sexo`.
10. Agregaciones requeridas mediante Spark SQL.
11. Validaciones automáticas finales.

## Ejecución

### Google Colab

1. Abra `notebooks/mcdi502_s2_g3.ipynb` en Colab.
2. Cargue el repositorio o los seis archivos de `data/raw/`.
3. Ejecute todas las celdas en orden.

El Notebook acepta también los nombres alternativos indicados en la pauta: `eventos.csv`, `equipos.csv`, `resultado.csv` y `juego.json`.

### Local

Requisitos: Python 3.10 o superior y Java 17.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

En Windows, active el entorno con:

```powershell
.venv\Scripts\activate
```

## Validación del repositorio

```bash
python scripts/validate_repository.py
```

La validación comprueba archivos, cantidades, esquemas básicos, JSON, estructura del Notebook, nomenclatura y presencia de los puntos obligatorios.

## Archivos de entrega

La entrega institucional debe contener únicamente:

- `mcdi502_s2_g3.ipynb`
- `mcdi502_s2_g3_video.mp4`

Ambos se comprimen en un único archivo ZIP. El video no está incluido en este repositorio porque debe ser grabado por el grupo.
