from __future__ import annotations
import ast, csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"
NOTEBOOK = ROOT / "mcdi502_s2_g3.ipynb"

required = [
    DATA / "deportista.csv", DATA / "deportista2.csv", DATA / "equipo.csv",
    DATA / "evento.csv", DATA / "resultados.csv", DATA / "juegos.json", NOTEBOOK,
]
for path in required:
    if not path.exists():
        raise SystemExit(f"ERROR: falta {path.relative_to(ROOT)}")

# Validación de nombre.
stem = NOTEBOOK.stem
if len(stem) > 20 or not re.fullmatch(r"[A-Za-z0-9_]+", stem):
    raise SystemExit("ERROR: nombre de notebook inválido")

# Conteos de datos fuente.
def parse_deportistas(path):
    total = 0
    with path.open(encoding="utf-8-sig", newline="") as fh:
        for i, row in enumerate(csv.reader(fh), 1):
            if len(row) == 8 and row[-1].strip() == "": row = row[:-1]
            if len(row) != 7: raise SystemExit(f"ERROR: {path.name}:{i}")
            total += 1
    return total

athletes = parse_deportistas(DATA/"deportista.csv") + parse_deportistas(DATA/"deportista2.csv")
if athletes != 135571: raise SystemExit(f"ERROR: deportistas={athletes}")

with (DATA/"equipo.csv").open(encoding="utf-8-sig") as f:
    teams = sum(1 for _ in csv.DictReader(f))
with (DATA/"resultados.csv").open(encoding="utf-8-sig") as f:
    results = sum(1 for _ in csv.DictReader(f, delimiter=";"))
with (DATA/"juegos.json").open(encoding="utf-8") as f:
    games = len(json.load(f))
if (teams, results, games) != (1184, 271116, 51):
    raise SystemExit(f"ERROR: conteos inesperados {(teams, results, games)}")

nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
source = "\n".join("".join(c.get("source", [])) for c in nb["cells"])
tokens = [
    'pyspark[connect]==4.0.1', 'SparkSession.builder', 'repartition(6)',
    'deportistaTotal', 'MayorEdad', 'Deportistas_mujer', 'createDataFrame',
    'Evento', 'Resultado', 'Equipos', 'Juego', 'broadcast', 'repartition(5',
    'IMC', 'Descripción_sexo', 'medallas_por_equipo',
    'estadisticas_edad_medalla', 'temporada = spark.sql', 'sexo = spark.sql',
    'explain(mode="formatted")', 'Validaciones completadas correctamente',
]
missing = [t for t in tokens if t not in source]
if missing: raise SystemExit(f"ERROR: faltan evidencias {missing}")

# Sintaxis Python de las celdas, excluyendo comandos de notebook.
for idx, cell in enumerate(nb["cells"]):
    if cell.get("cell_type") != "code": continue
    lines = [line for line in "".join(cell.get("source", [])).splitlines() if not line.lstrip().startswith(("!", "%"))]
    try: ast.parse("\n".join(lines))
    except SyntaxError as exc: raise SystemExit(f"ERROR sintaxis celda {idx}: {exc}")

print("Repositorio validado correctamente.")
print(f"Deportistas: {athletes:,}")
print(f"Equipos: {teams:,}")
print(f"Resultados: {results:,}")
print(f"Juegos: {games:,}")
print(f"Notebook: {NOTEBOOK.name}")
