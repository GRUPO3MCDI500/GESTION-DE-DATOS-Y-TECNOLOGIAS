# Evaluación Sumativa 2 — Taller I

Repositorio del Grupo 3 para **MCDI502: Gestión de Datos y Tecnologías**, adaptado al análisis histórico de los Juegos Olímpicos con Apache Spark.

## Integrantes

- Eduardo Garrido
- Luis Espinosa
- Mauricio Ortega
- Wilson Arévalo

## Estructura

```text
GESTION-DE-DATOS-Y-TECNOLOGIAS-final/
├── .github/workflows/validate.yml
├── data/raw/
│   ├── deportista.csv
│   ├── deportista2.csv
│   ├── eventos.csv
│   ├── equipos.csv
│   ├── resultado.csv
│   └── juego.json
├── docs/
│   ├── analisis_cumplimiento.md
│   ├── checklist_entrega.md
│   ├── guion_video.md
│   └── orden_ejecucion.md
├── notebooks/
│   └── mcdi502_s2_g3.ipynb
├── scripts/
│   └── validate_repository.py
├── mcdi502_s2_g3.ipynb
├── requirements.txt
└── README.md
```

## Cumplimiento de la pauta

El notebook está organizado en los ocho pasos solicitados:

1. Inicia `SparkSession` y `SparkContext`.
2. Crea el RDD `deportista` con 6 particiones, carga `deportista2`, genera `deportistaTotal`, cuenta registros y crea el DataFrame `deportista`.
3. Genera `MayorEdad`, `Deportistas_mujer` y `Deportistas_mayusculas`.
4. Crea `Evento`, `Resultado`, `Equipos` y `Juego`, aplica `.cache()` y los integra en `dataframe_maestro`.
5. Reparte `dataframe_maestro` en 5 particiones.
6. Muestra cantidad de filas, tipos de datos y esquema.
7. Calcula `IMC` y `Descripción_sexo`.
8. Ejecuta las cuatro agregaciones requeridas mediante Spark SQL.

## Ejecución en Google Colab

1. Suba `mcdi502_s2_g3.ipynb` mediante **Archivo → Subir notebook**.
2. Ejecute las celdas en orden.
3. Cuando aparezca el selector, cargue el ZIP completo del repositorio.
4. Continúe con **Entorno de ejecución → Ejecutar todo**.

El notebook instala Java 17 y `pyspark[connect]==4.0.1`, versión compatible con el paquete `dataproc-spark-connect` presente en Colab.

## Ejecución local

Requisitos: Python 3.10 o superior y Java 17.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

En Windows:

```powershell
.venv\Scripts\activate
```

## Validación

```bash
python scripts/validate_repository.py
```

## Entrega institucional

El ZIP final de entrega debe contener únicamente:

- `mcdi502_s2_g3.ipynb`
- `mcdi502_s2_g3_video.mp4`

El video debe ser grabado por los integrantes y durar entre 7 y 10 minutos.
