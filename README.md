# Análisis de datos de la Copa Mundial con Apache Spark

## Información académica

- **Asignatura:** 202681.2558 | Gestión de Datos y Tecnologías
- **Tipo de actividad:** Guía formativa de ejercicios
- **Tecnología principal:** Apache Spark con PySpark
- **Entorno de ejecución:** Google Colab

### Integrantes

- Eduardo Garrido
- Luis Espinosa
- Mauricio Ortega
- Wilson Arévalo

## Objetivo

Implementar un análisis reproducible que cubra los siguientes aspectos:

- Creación, unión y transformación de RDD.
- Conversión de RDD a DataFrame con esquema explícito.
- Integración de múltiples fuentes mediante `join`.
- Aplicación de caché, persistencia y reparticionamiento.
- Construcción de columnas calculadas.
- Desarrollo de consultas analíticas con Spark SQL.
- Validación de resultados mediante operaciones de inspección.

## Estructura del repositorio

```text
202681-2558-gestion-datos-tecnologias/
├── .github/
│   └── workflows/
│       └── validate.yml
├── data/
│   ├── README.md
│   └── raw/
│       ├── equipos.csv
│       ├── estadios.csv
│       ├── jugadores.csv
│       ├── partidos.csv
│       └── torneos.json
├── docs/
│   └── guia_ejercicios_apache_spark.pdf
├── notebooks/
│   └── 01_analisis_mundial_pyspark.ipynb
├── scripts/
│   └── validate_repository.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Datos utilizados

| Archivo | Formato | Registros |
|---|---:|---:|
| `jugadores.csv` | CSV | 80 |
| `equipos.csv` | CSV | 15 |
| `partidos.csv` | CSV | 100 |
| `estadios.csv` | CSV | 10 |
| `torneos.json` | JSON | 3 |

Los archivos originales se conservan en `data/raw/` y no deben modificarse
directamente.

## Ejecución en Google Colab

1. Abra `notebooks/01_analisis_mundial_pyspark.ipynb` en Google Colab.
2. Cargue los cinco archivos ubicados en `data/raw/`.
3. Ejecute las celdas en el orden definido.
4. Revise los resultados mostrados mediante `.show()`.

El Notebook instala Java y PySpark dentro del entorno de Colab.

## Ejecución local

### Requisitos

- Python 3.10 o superior.
- Java 17.
- JupyterLab o Jupyter Notebook.

### Instalación

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

Instale las dependencias:

```bash
pip install -r requirements.txt
```

Inicie Jupyter:

```bash
jupyter lab
```

> El Notebook está preparado principalmente para Google Colab. Para una
> ejecución local, ajuste `BASE_PATH` y omita la celda de carga con
> `google.colab.files`.

## Validación del repositorio

Ejecute:

```bash
python scripts/validate_repository.py
```

La validación comprueba:

- Presencia de los archivos obligatorios.
- Columnas esperadas en los CSV.
- Cantidad de registros de cada dataset.
- Estructura del archivo JSON.
- Validez estructural del Notebook.

La misma validación se ejecuta automáticamente mediante GitHub Actions.

## Contenido del análisis

El Notebook incluye:

1. Configuración de Spark.
2. Creación y unión de RDD.
3. Transformaciones sobre RDD.
4. Construcción e integración de DataFrames.
5. Persistencia, caché y particionamiento.
6. Inspección del DataFrame integrado.
7. Cálculo de IMC, categoría de edad y resultado del partido.
8. Diez consultas mediante Spark SQL.
9. Filtros, selecciones, ordenamientos y análisis avanzados.


## Integrantes

- Eduardo Garrido
- Luis Espinosa
- Mauricio Ortega
- Wilson Arévalo
