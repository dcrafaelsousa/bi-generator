import shutil
import zipfile
import json
import uuid
from pathlib import Path

# ---------------------------------------------------------------------------
# Tipos de datos Excel → TMDL
# ---------------------------------------------------------------------------
EXCEL_TO_TMDL_TYPE = {
    "int64":   "int64",
    "float64": "double",
    "bool":    "boolean",
    "datetime64[ns]": "dateTime",
    "object":  "string",
}

def _tmdl_type(dtype_str: str) -> str:
    return EXCEL_TO_TMDL_TYPE.get(dtype_str, "string")


# ---------------------------------------------------------------------------
# Generador de tabla .tmdl
# ---------------------------------------------------------------------------
def _generar_tabla_tmdl(table_name: str, columns: list[dict]) -> str:
    """
    columns: lista de {"name": str, "dataType": str}
    Devuelve el contenido del archivo <table_name>.tmdl
    """
    lines = [
        f"table {table_name}",
        "\tlineageTag: " + str(uuid.uuid4()),
        "",
    ]
    for col in columns:
        lines += [
            f"\tcolumn {col['name']}",
            f"\t\tdataType: {col['dataType']}",
            f"\t\tlineageTag: {str(uuid.uuid4())}",
            f"\t\tsummarizeBy: none",
            f"\t\tsourceColumn: {col['name']}",
            "",
            f"\t\tannotation SummarizationSetBy = Automatic",
            "",
        ]
    lines += [
        "\tpartition " + table_name + " = m",
        "\t\tmode: import",
        "\t\tsource =",
        '\t\t\tlet',
        f'\t\t\t\tSource = Excel.Workbook(File.Contents(""), null, true),',
        f'\t\t\t\t{table_name}_Sheet = Source{{[Item="{table_name}",Kind="Sheet"]}}[Data]',
        '\t\t\tin',
        f'\t\t\t\t{table_name}_Sheet',
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Generador principal
# ---------------------------------------------------------------------------
def generar_proyecto(necesidad=None, archivo=None):
    """
    Genera la estructura PBIP completa.

    Si se pasa `archivo` (ruta a un .xlsx), lee las hojas y crea una tabla
    .tmdl por hoja con las columnas detectadas.
    Si no se pasa archivo, genera el SemanticModel vacío.
    """
    base = Path("pbip_generado")
    name = "proyecto"

    if base.exists():
        shutil.rmtree(base)

    # ── Carpetas ────────────────────────────────────────────────────────────
    report_root = base / f"{name}.Report"
    report_def  = report_root / "definition"
    pages_dir   = report_def / "pages"
    dataset_root = base / f"{name}.SemanticModel"

    report_root.mkdir(parents=True)
    report_def.mkdir(parents=True)
    pages_dir.mkdir(parents=True)
    dataset_root.mkdir(parents=True)

    # ── 1. proyecto.pbip ────────────────────────────────────────────────────
    (base / f"{name}.pbip").write_text(json.dumps({
        "version": "1.0",
        "artifacts": [
            {"report": {"path": f"{name}.Report"}}
        ],
        "settings": {"enableAutoRecovery": True}
    }, indent=2))

    # ── 2. proyecto.Report/.platform ────────────────────────────────────────
    # NUEVO: requerido con logicalId y type = Report
    (report_root / ".platform").write_text(json.dumps({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {
            "type": "Report",
            "displayName": name
        },
        "config": {
            "version": "2.0",
            "logicalId": str(uuid.uuid4())
        }
    }, indent=2))

    # ── 3. definition.pbir ──────────────────────────────────────────────────
    (report_root / "definition.pbir").write_text(json.dumps({
        "version": "1.0",
        "datasetReference": {
            "byPath": {"path": f"../{name}.SemanticModel"},
            "byConnection": None
        }
    }, indent=2))

    # ── 4. report.json ──────────────────────────────────────────────────────
    (report_def / "report.json").write_text(json.dumps({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/1.0.0/schema.json",
        "themeCollection": {
            "baseTheme": {
                "name": "CY23SU11",
                "version": "5.49",
                "type": 2
            }
        },
        "config": json.dumps({
            "version": "5.49",
            "themeCollection": {
                "baseTheme": {
                    "name": "CY23SU11",
                    "version": "5.49",
                    "type": 2
                }
            },
            "activeSectionIndex": 0,
            "defaultDrillFilterOtherVisuals": True,
            "settings": {
                "useNewFilterPaneExperience": True,
                "allowChangeFilterTypes": True,
                "useStylableVisualContainerHeader": True,
                "queryLimitOption": 6,
                "exportDataMode": 1,
                "useDefaultAggregateDisplayName": True
            }
        }),
        "layoutOptimization": 0,
        "resourcePackages": []
    }, indent=2))

    # ── 5. version.json ─────────────────────────────────────────────────────
    # NUEVO: requerido en definition/
    (report_def / "version.json").write_text(json.dumps({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/version/1.0.0/schema.json",
        "version": "1.0"
    }, indent=2))

    # ── 6. pages/pages.json + página vacía ──────────────────────────────────
    page_name    = "ReportSection"
    page_display = "Página 1"

    (pages_dir / "pages.json").write_text(json.dumps({
        "activePageName": page_name,
        "pageOrder": [page_name]
    }, indent=2))

    page_dir = pages_dir / page_name
    page_dir.mkdir(parents=True)
    (page_dir / "page.json").write_text(json.dumps({
        "displayName": page_display,
        "displayOption": 1,
        "filters": "[]",
        "height": 720.0,
        "name": page_name,
        "visualContainers": [],
        "width": 1280.0,
        "config": "{}"
    }, indent=2))

    # ── 7. SemanticModel/.platform ──────────────────────────────────────────
    (dataset_root / ".platform").write_text(json.dumps({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {
            "type": "SemanticModel",
            "displayName": name
        },
        "config": {
            "version": "2.0",
            "logicalId": str(uuid.uuid4())
        }
    }, indent=2))

    # ── 8. definition.pbism con versión 4.2 ─────────────────────────────────
    # CORREGIDO: ahora incluye version 4.2
    (dataset_root / "definition.pbism").write_text(json.dumps({
        "version": "4.2",
        "settings": {}
    }, indent=2))

    # ── 9. Leer Excel y generar archivos TMDL ───────────────────────────────
    tables_info = []   # [{"name": str, "columns": [...]}]

    if archivo:
        try:
            import pandas as pd
            xl = pd.ExcelFile(archivo)
            for sheet in xl.sheet_names:
                df = xl.parse(sheet, nrows=0)   # solo encabezados
                cols = [
                    {"name": col, "dataType": _tmdl_type(str(df[col].dtype))}
                    for col in df.columns
                ]
                tables_info.append({"name": sheet, "columns": cols})
        except Exception as e:
            print(f"[WARN] No se pudo leer el Excel: {e}")

    # Tabla placeholder si no hay Excel
    if not tables_info:
        tables_info = [{"name": "Tabla1", "columns": [
            {"name": "ID",     "dataType": "int64"},
            {"name": "Nombre", "dataType": "string"},
        ]}]

    # ── 10. model.tmdl ──────────────────────────────────────────────────────
    # NUEVO: reemplaza model.bim
    table_refs = "\n".join(f"\tref table {t['name']}" for t in tables_info)
    model_tmdl = (
        "model Model\n"
        f"\tculture: es-ES\n"
        f"\tdataAccessOptions\n"
        f"\t\tlegacyRedirects: true\n"
        f"\t\treturnErrorValuesAsNull: true\n"
        f"\n"
        f"{table_refs}\n"
    )
    (dataset_root / "model.tmdl").write_text(model_tmdl)

    # ── 11. database.tmdl ───────────────────────────────────────────────────
    # NUEVO
    (dataset_root / "database.tmdl").write_text(
        f"database {name}\n"
        f"\tcompatibilityLevel: 1550\n"
    )

    # ── 12. Una tabla .tmdl por hoja ─────────────────────────────────────────
    # NUEVO
    for table in tables_info:
        tmdl_content = _generar_tabla_tmdl(table["name"], table["columns"])
        (dataset_root / f"{table['name']}.tmdl").write_text(tmdl_content)

    # ── 13. Empaquetar en ZIP ────────────────────────────────────────────────
    zip_path = Path("proyecto_pbip.zip")
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in base.rglob("*"):
            if file.is_file():
                z.write(file, file.relative_to(base))

    return str(zip_path)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print(generar_proyecto())
