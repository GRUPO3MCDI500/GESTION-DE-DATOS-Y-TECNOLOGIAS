# Evaluación Sumativa 2 — Taller I

Repositorio completo para **MCDI502: Gestión de Datos y Tecnologías**, adaptado al análisis histórico de los Juegos Olímpicos con Apache Spark.

## Integrantes

- Eduardo Garrido
- Luis Espinosa
- Mauricio Ortega
- Wilson Arévalo

## Estructura

```text
GESTION-DE-DATOS-Y-TECNOLOGIAS-completo/
├── .github/workflows/validate.yml
├── data/raw/
│   ├── deportista.csv
│   ├── deportista2.csv
│   ├── equipo.csv
│   ├── evento.csv
│   ├── juegos.json
│   └── resultados.csv
├── docs/
│   ├── checklist_entrega.md
│   ├── guion_video.md
│   └── orden_ejecucion.md
├── scripts/validate_repository.py
├── .gitignore
├── mcdi502_s2_g3.ipynb
├── README.md
└── requirements.txt
```

## Ejecución en Google Colab

1. Descargue `mcdi502_s2_g3.ipynb` y el ZIP del repositorio.
2. En Colab seleccione **Archivo > Subir notebook**.
3. Ejecute la celda de instalación.
4. Cuando la celda de carga lo solicite, suba el ZIP completo.
5. Ejecute las celdas de arriba hacia abajo.
6. Compruebe que la última validación muestre `Validaciones completadas correctamente`.

El notebook usa **PySpark 4.0.1** en Colab para mantener compatibilidad con `dataproc-spark-connect`.

## Ejecución local

Requisitos: Python 3.10 o superior y Java 17.

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
# .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## Validación estática

```bash
python scripts/validate_repository.py
```

## Entrega institucional

El ZIP final de entrega debe contener únicamente:

- `mcdi502_s2_g3.ipynb`
- `mcdi502_s2_g3_video.mp4`

El video debe durar entre 7 y 10 minutos y todos los integrantes deben participar.
