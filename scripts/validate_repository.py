from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"
NOTEBOOK = ROOT / "notebooks" / "mcdi502_s2_g3.ipynb"

EXPECTED_FILES = [
    DATA / "deportista.csv",
    DATA / "deportista2.csv",
    DATA / "equipos.csv",
    DATA / "eventos.csv",
    DATA / "resultado.csv",
    DATA / "juego.json",
    NOTEBOOK,
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


for path in EXPECTED_FILES:
    if not path.exists():
        fail(f"Falta el archivo obligatorio: {path.relative_to(ROOT)}")


def parse_deportista(path: Path) -> list[tuple]:
    rows = []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        for line_number, values in enumerate(csv.reader(fh), start=1):
            if len(values) == 8 and values[-1].strip() == "":
                values = values[:-1]
            if len(values) != 7:
                fail(f"{path.name}:{line_number} tiene {len(values)} columnas")
            rows.append((
                int(values[0]), values[1], int(values[2]), int(float(values[3])),
                float(values[4]), float(values[5]), int(values[6]),
            ))
    return rows


def parse_event(path: Path) -> list[tuple]:
    rows = []
    with path.open(encoding="utf-8-sig") as fh:
        header = next(fh).strip()
        if header != "cod_evento,evento,deporte_id":
            fail("Encabezado inesperado en eventos.csv")
        for line_number, line in enumerate(fh, start=2):
            text = line.strip()
            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1].replace('""', '"')
            values = next(csv.reader([text]))
            if len(values) != 3:
                fail(f"eventos.csv:{line_number} no se pudo interpretar")
            deporte_id = None if values[2].strip() == "#N/A" else int(values[2])
            rows.append((int(values[0]), values[1], deporte_id))
    return rows


athletes = parse_deportista(DATA / "deportista.csv") + parse_deportista(DATA / "deportista2.csv")
if len(athletes) != 135571:
    fail(f"Se esperaban 135571 deportistas y se obtuvieron {len(athletes)}")
if len({row[0] for row in athletes}) != 135571:
    fail("Los identificadores de deportistas no son únicos")

with (DATA / "equipos.csv").open(encoding="utf-8-sig", newline="") as fh:
    teams = list(csv.DictReader(fh))
if len(teams) != 1184 or set(teams[0]) != {"id", "equipo", "sigla"}:
    fail("equipos.csv no cumple la estructura esperada")

events = parse_event(DATA / "eventos.csv")
if len(events) != 765 or {row[0] for row in events} != set(range(1, 766)):
    fail("eventos.csv debe contener los eventos 1 a 765")

with (DATA / "resultado.csv").open(encoding="utf-8-sig", newline="") as fh:
    results = list(csv.DictReader(fh, delimiter=";"))
if len(results) != 271116:
    fail(f"Se esperaban 271116 resultados y se obtuvieron {len(results)}")
if set(results[0]) != {"resultado_id", "medalla", "deportista_id", "juego_id", "evento_id"}:
    fail("resultado.csv no cumple la estructura esperada")

with (DATA / "juego.json").open(encoding="utf-8") as fh:
    games = json.load(fh)
if len(games) != 51:
    fail("juego.json debe contener 51 ediciones")
if set(games[0]) != {"juego_id", "ano", "temporada", "ciudad"}:
    fail("juego.json no cumple la estructura esperada")

stem = NOTEBOOK.stem
if len(stem) > 20:
    fail("El nombre del Notebook supera los 20 caracteres")
if not re.fullmatch(r"[A-Za-z0-9_-]+", stem):
    fail("El nombre del Notebook contiene caracteres no permitidos")
if "-" in stem and "_" in stem:
    fail("El nombre del Notebook mezcla guion medio y guion bajo")

with NOTEBOOK.open(encoding="utf-8") as fh:
    notebook = json.load(fh)
if notebook.get("nbformat") != 4 or not notebook.get("cells"):
    fail("El Notebook no posee una estructura válida")

source = "\n".join(
    "".join(cell.get("source", [])) if isinstance(cell.get("source"), list)
    else str(cell.get("source", ""))
    for cell in notebook["cells"]
)
required_tokens = [
    "SparkSession.builder",
    "deportistaTotal",
    "MayorEdad",
    "Deportistas_mujer",
    "Deportistas_mayusculas",
    "createDataFrame",
    "Evento.cache()",
    "Resultado.cache()",
    "Equipos.cache()",
    "Juego.cache()",
    "dataframe_maestro",
    "repartition(5",
    "Descripción_sexo",
    "medallas_por_equipo",
    "estadisticas_edad_medalla",
    "temporada = spark.sql",
    "sexo = spark.sql",
    "explain(mode=\"formatted\")",
]
missing = [token for token in required_tokens if token not in source]
if missing:
    fail(f"El Notebook no contiene evidencias obligatorias: {missing}")

print("Repositorio validado correctamente.")
print(f"Deportistas: {len(athletes)}")
print(f"Equipos: {len(teams)}")
print(f"Eventos: {len(events)}")
print(f"Resultados: {len(results)}")
print(f"Juegos: {len(games)}")
print(f"Notebook: {NOTEBOOK.name}")
