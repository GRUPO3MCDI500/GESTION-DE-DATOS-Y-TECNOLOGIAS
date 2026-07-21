\
from pathlib import Path
import csv
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"
NOTEBOOK = ROOT / "notebooks" / "01_analisis_mundial_pyspark.ipynb"

EXPECTED_CSV = {
    "jugadores.csv": {
        "rows": 80,
        "columns": [
            "jugador_id", "nombre", "apellido", "edad",
            "altura", "peso", "posicion", "equipo_id",
        ],
    },
    "equipos.csv": {
        "rows": 15,
        "columns": [
            "equipo_id", "nombre", "confederacion", "ranking_fifa",
        ],
    },
    "partidos.csv": {
        "rows": 100,
        "columns": [
            "partido_id", "equipo_local_id", "equipo_visitante_id",
            "goles_local", "goles_visitante", "estadio_id",
            "torneo_id", "fase",
        ],
    },
    "estadios.csv": {
        "rows": 10,
        "columns": [
            "estadio_id", "nombre", "ciudad", "pais", "capacidad",
        ],
    },
}

EXPECTED_JSON_KEYS = {
    "torneo_id", "nombre", "anio", "pais_sede", "campeon", "subcampeon",
}


def fail(message: str) -> None:
    print(f"[ERROR] {message}")
    sys.exit(1)


def validate_csv(filename: str, specification: dict) -> None:
    path = DATA / filename
    if not path.exists():
        fail(f"No existe {path.relative_to(ROOT)}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames or []
        rows = list(reader)

    if columns != specification["columns"]:
        fail(
            f"Columnas inválidas en {filename}. "
            f"Esperadas: {specification['columns']}; obtenidas: {columns}"
        )

    if len(rows) != specification["rows"]:
        fail(
            f"Cantidad de registros inválida en {filename}. "
            f"Esperados: {specification['rows']}; obtenidos: {len(rows)}"
        )

    print(f"[OK] {filename}: {len(rows)} registros")


def validate_json() -> None:
    path = DATA / "torneos.json"
    if not path.exists():
        fail(f"No existe {path.relative_to(ROOT)}")

    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list):
        fail("torneos.json debe contener una lista de objetos")

    if len(records) != 3:
        fail(
            "Cantidad de registros inválida en torneos.json. "
            f"Esperados: 3; obtenidos: {len(records)}"
        )

    for index, record in enumerate(records, start=1):
        if set(record.keys()) != EXPECTED_JSON_KEYS:
            fail(f"Estructura inválida en torneos.json, registro {index}")

    print("[OK] torneos.json: 3 registros")


def validate_notebook() -> None:
    if not NOTEBOOK.exists():
        fail(f"No existe {NOTEBOOK.relative_to(ROOT)}")

    with NOTEBOOK.open("r", encoding="utf-8") as file:
        notebook = json.load(file)

    if notebook.get("nbformat") != 4:
        fail("El Notebook no utiliza el formato nbformat 4")

    cells = notebook.get("cells")
    if not isinstance(cells, list) or not cells:
        fail("El Notebook no contiene celdas")

    code_cells = sum(1 for cell in cells if cell.get("cell_type") == "code")
    markdown_cells = sum(
        1 for cell in cells if cell.get("cell_type") == "markdown"
    )

    if code_cells == 0 or markdown_cells == 0:
        fail("El Notebook debe contener celdas de código y Markdown")

    print(
        f"[OK] Notebook válido: {len(cells)} celdas "
        f"({code_cells} de código y {markdown_cells} Markdown)"
    )


def main() -> None:
    for filename, specification in EXPECTED_CSV.items():
        validate_csv(filename, specification)

    validate_json()
    validate_notebook()
    print("[OK] Repositorio validado correctamente")


if __name__ == "__main__":
    main()
