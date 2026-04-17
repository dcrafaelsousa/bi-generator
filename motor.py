import shutil
import zipfile
import json
import uuid
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Tipos de datos Excel → TMDL / BIM
# ---------------------------------------------------------------------------
EXCEL_TO_TMDL_TYPE = {
    "int64":          "int64",
    "float64":        "double",
    "bool":           "boolean",
    "datetime64[ns]": "dateTime",
    "object":         "string",
}

NUMERIC_TYPES = {"int64", "float64", "double"}

def _tmdl_type(dtype_str: str) -> str:
    return EXCEL_TO_TMDL_TYPE.get(dtype_str, "string")


# ---------------------------------------------------------------------------
# Generador de tabla .tmdl
# ---------------------------------------------------------------------------
def _generar_tabla_tmdl(table_name: str, columns: list, excel_rel_path: str) -> str:
    safe = excel_rel_path.replace("\\", "/")
    lines = [
        f"table {table_name}",
        f"\tlineageTag: {uuid.uuid4()}",
        "",
    ]
    for col in columns:
        lines += [
            f"\tcolumn {col['name']}",
            f"\t\tdataType: {col['dataType']}",
            f"\t\tlineageTag: {uuid.uuid4()}",
            f"\t\tsummarizeBy: {'sum' if col['dataType'] in NUMERIC_TYPES else 'none'}",
            f"\t\tsourceColumn: {col['name']}",
            "",
            f"\t\tannotation SummarizationSetBy = Automatic",
            "",
        ]
    lines += [
        f"\tpartition {table_name} = m",
        "\t\tmode: import",
        "\t\tsource =",
        "\t\t\tlet",
        f'\t\t\t\tSource = Excel.Workbook(File.Contents("{safe}"), null, true),',
        f'\t\t\t\t{table_name}_Sheet = Source{{[Item="{table_name}",Kind="Sheet"]}}[Data],',
        f'\t\t\t\t#"Encabezados promovidos" = Table.PromoteHeaders({table_name}_Sheet, [PromoteAllScalars=true])',
        "\t\t\tin",
        '\t\t\t\t#"Encabezados promovidos"',
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Generador de visuales automáticos
# ---------------------------------------------------------------------------
def _inferir_visuales(tables_info: list) -> list:
    visuals = []
    x_offset = 20
    y_offset = 20
    w, h = 400, 280

    for table in tables_info:
        cols = table["columns"]
        numerics   = [c for c in cols if c["dataType"] in NUMERIC_TYPES]
        categorics = [c for c in cols if c["dataType"] == "string"]
        dates      = [c for c in cols if c["dataType"] == "dateTime"]

        table_cols_config = [
            {"Column": {"Expression": {"SourceRef": {"Entity": table["name"]}},
                        "Property": c["name"]}}
            for c in cols[:8]
        ]
        visuals.append({
            "type": "tableEx",
            "x": x_offset, "y": y_offset, "width": w * 2 + 20, "height": h,
            "table": table["name"],
            "dataRoles": {"Values": table_cols_config},
        })
        y_offset += h + 20

        if categorics and numerics:
            visuals.append({
                "type": "barChart",
                "x": x_offset, "y": y_offset, "width": w, "height": h,
                "table": table["name"],
                "dataRoles": {
                    "Category": [{"Column": {"Expression": {"SourceRef": {"Entity": table["name"]}},
                                             "Property": categorics[0]["name"]}}],
                    "Y": [{"Measure": {"Expression": {"SourceRef": {"Entity": table["name"]}},
                                       "Property": numerics[0]["name"]}}],
                },
            })

        if dates and numerics:
            visuals.append({
                "type": "lineChart",
                "x": x_offset + w + 20, "y": y_offset, "width": w, "height": h,
                "table": table["name"],
                "dataRoles": {
                    "Category": [{"Column": {"Expression": {"SourceRef": {"Entity": table["name"]}},
                                             "Property": dates[0]["name"]}}],
                    "Y": [{"Measure": {"Expression": {"SourceRef": {"Entity": table["name"]}},
                                       "Property": numerics[0]["name"]}}],
                },
            })

        y_offset += h + 40

    return visuals


def _build_visual_container(visual_info: dict) -> dict:
    vtype = visual_info["type"]
    x, y = visual_info["x"], visual_info["y"]
    width, height = visual_info["width"], visual_info["height"]

    visual_config = {
        "name": str(uuid.uuid4()).replace("-", "")[:20],
        "visualType": vtype,
        "projections": {},
        "prototypeQuery": {
            "Version": 2,
            "From": [{"Name": "t", "Entity": visual_info["table"], "Type": 0}],
            "Select": [],
        }
    }

    data_roles = visual_info.get("dataRoles", {})
    select_items = []
    projections = {}

    for role, items in data_roles.items():
        projections[role] = []
        for item in items:
            if "Column" in item:
                prop = item["Column"]["Property"]
                qname = f"t.{prop}"
                select_items.append({
                    "Column": {
                        "Expression": {"SourceRef": {"Source": "t"}},
                        "Property": prop
                    },
                    "Name": qname
                })
                projections[role].append({"queryRef": qname})
            elif "Measure" in item:
                prop = item["Measure"]["Property"]
                qname = f"t.{prop}"
                select_items.append({
                    "Aggregation": {
                        "Expression": {
                            "Column": {
                                "Expression": {"SourceRef": {"Source": "t"}},
                                "Property": prop
                            }
                        },
                        "Function": 0
                    },
                    "Name": qname
                })
                projections[role].append({"queryRef": qname})

    visual_config["prototypeQuery"]["Select"] = select_items
    visual_config["projections"] = projections

    return {
        "x": x, "y": y,
        "z": 1000,
        "width": width, "height": height,
        "config": json.dumps({"singleVisual": visual_config}),
        "filters": "[]",
        "tabOrder": 0
    }


# ---------------------------------------------------------------------------
# Generador principal
# ---------------------------------------------------------------------------
def generar_proyecto(necesidad=None, archivo=None):
    """
    Genera la estructura PBIP completa.
    FIX: El Excel se copia DENTRO del ZIP (mismo nivel que proyecto.pbip)
    y las queries M usan ruta relativa "datos.xlsx".
    """
    base = Path("pbip_generado")
    name = "proyecto"

    if base.exists():
        shutil.rmtree(base)

    # El Excel se copia a la raíz del proyecto con nombre fijo
    excel_filename = "datos.xlsx"
    # Power BI Desktop resuelve rutas relativas desde la carpeta del .pbip
    excel_rel_path_m = excel_filename

    # ── Carpetas ─────────────────────────────────────────────────────────────
    report_root  = base / f"{name}.Report"
    report_def   = report_root / "definition"
    pages_dir    = report_def / "pages"
    dataset_root = base / f"{name}.SemanticModel"

    for d in [report_root, report_def, pages_dir, dataset_root]:
        d.mkdir(parents=True, exist_ok=True)

    # Copiar Excel al proyecto
    if archivo:
        shutil.copy2(archivo, base / excel_filename)

    # ── 1. proyecto.pbip ─────────────────────────────────────────────────────
    (base / f"{name}.pbip").write_text(json.dumps({
        "version": "1.0",
        "artifacts": [{"report": {"path": f"{name}.Report"}}],
        "settings": {"enableAutoRecovery": True}
    }, indent=2))

    # ── 2. Report/.platform ──────────────────────────────────────────────────
    (report_root / ".platform").write_text(json.dumps({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {"type": "Report", "displayName": name},
        "config": {"version": "2.0", "logicalId": str(uuid.uuid4())}
    }, indent=2))

    # ── 3. definition.pbir ───────────────────────────────────────────────────
    (report_root / "definition.pbir").write_text(json.dumps({
        "version": "1.0",
        "datasetReference": {
            "byPath": {"path": f"../{name}.SemanticModel"},
            "byConnection": None
        }
    }, indent=2))

    # ── 4. report.json ───────────────────────────────────────────────────────
    (report_def / "report.json").write_text(json.dumps({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/1.0.0/schema.json",
        "themeCollection": {"baseTheme": {"name": "CY23SU11", "version": "5.49", "type": 2}},
        "config": json.dumps({
            "version": "5.49",
            "themeCollection": {"baseTheme": {"name": "CY23SU11", "version": "5.49", "type": 2}},
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

    # ── 5. version.json ──────────────────────────────────────────────────────
    (report_def / "version.json").write_text(json.dumps({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/version/1.0.0/schema.json",
        "version": "1.0"
    }, indent=2))

    # ── 6. Leer Excel → tablas ───────────────────────────────────────────────
    tables_info = []
    if archivo:
        try:
            import pandas as pd
            xl = pd.ExcelFile(archivo)
            for sheet in xl.sheet_names:
                df = xl.parse(sheet, nrows=5)
                cols = [
                    {"name": col, "dataType": _tmdl_type(str(df[col].dtype))}
                    for col in df.columns
                ]
                tables_info.append({"name": sheet, "columns": cols, "df_sample": df})
        except Exception as e:
            print(f"[WARN] No se pudo leer el Excel: {e}")

    if not tables_info:
        tables_info = [{"name": "Tabla1", "columns": [
            {"name": "ID",     "dataType": "int64"},
            {"name": "Nombre", "dataType": "string"},
        ], "df_sample": None}]

    # ── 7. Inferir y generar visuales ────────────────────────────────────────
    visuals_info = _inferir_visuales(tables_info)
    visual_containers = [_build_visual_container(v) for v in visuals_info]

    # ── 8. pages.json + page.json ────────────────────────────────────────────
    page_name    = "ReportSection"
    page_display = "Página 1"

    (pages_dir / "pages.json").write_text(json.dumps({
        "activePageName": page_name,
        "pageOrder": [page_name]
    }, indent=2))

    page_dir = pages_dir / page_name
    page_dir.mkdir(parents=True, exist_ok=True)
    (page_dir / "page.json").write_text(json.dumps({
        "displayName": page_display,
        "displayOption": 1,
        "filters": "[]",
        "height": 720.0,
        "name": page_name,
        "visualContainers": visual_containers,
        "width": 1280.0,
        "config": "{}"
    }, indent=2))

    # ── 9. SemanticModel/.platform ───────────────────────────────────────────
    (dataset_root / ".platform").write_text(json.dumps({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {"type": "SemanticModel", "displayName": name},
        "config": {"version": "2.0", "logicalId": str(uuid.uuid4())}
    }, indent=2))

    # ── 10. definition.pbism ─────────────────────────────────────────────────
    (dataset_root / "definition.pbism").write_text(json.dumps({
        "version": "4.2",
        "settings": {}
    }, indent=2))

    # ── 11. model.bim ────────────────────────────────────────────────────────
    safe = excel_rel_path_m.replace("\\", "/")
    bim_tables = []
    for t in tables_info:
        bim_cols = [
            {
                "name": c["name"],
                "dataType": c["dataType"],
                "lineageTag": str(uuid.uuid4()),
                "summarizeBy": "sum" if c["dataType"] in NUMERIC_TYPES else "none",
                "sourceColumn": c["name"],   # FIX: campo que faltaba
                "annotations": [{"name": "SummarizationSetBy", "value": "Automatic"}]
            }
            for c in t["columns"]
        ]
        bim_tables.append({
            "name": t["name"],
            "lineageTag": str(uuid.uuid4()),
            "columns": bim_cols,
            "partitions": [{
                "name": t["name"],
                "mode": "import",
                "source": {
                    "type": "m",
                    "expression": [
                        "let",
                        f'    Source = Excel.Workbook(File.Contents("{safe}"), null, true),',
                        f'    {t["name"]}_Sheet = Source{{[Item="{t["name"]}",Kind="Sheet"]}}[Data],',
                        f'    #"Encabezados promovidos" = Table.PromoteHeaders({t["name"]}_Sheet, [PromoteAllScalars=true])',
                        "in",
                        '    #"Encabezados promovidos"'
                    ]
                }
            }]
        })

    (dataset_root / "model.bim").write_text(json.dumps({
        "compatibilityLevel": 1550,
        "model": {
            "culture": "es-ES",
            "dataAccessOptions": {
                "legacyRedirects": True,
                "returnErrorValuesAsNull": True
            },
            "defaultPowerBIDataSourceVersion": "powerBI_V3",
            "sourceQueryCulture": "es-PE",
            "tables": bim_tables
        }
    }, indent=2))

    # ── 12. model.tmdl ───────────────────────────────────────────────────────
    table_refs = "\n".join(f"\tref table {t['name']}" for t in tables_info)
    (dataset_root / "model.tmdl").write_text(
        "model Model\n"
        "\tculture: es-ES\n"
        "\tdataAccessOptions\n"
        "\t\tlegacyRedirects: true\n"
        "\t\treturnErrorValuesAsNull: true\n"
        "\n"
        f"{table_refs}\n"
    )

    # ── 13. database.tmdl ────────────────────────────────────────────────────
    (dataset_root / "database.tmdl").write_text(
        f"database {name}\n"
        f"\tcompatibilityLevel: 1550\n"
    )

    # ── 14. Una tabla .tmdl por hoja (ruta relativa) ─────────────────────────
    for table in tables_info:
        tmdl_content = _generar_tabla_tmdl(table["name"], table["columns"], excel_rel_path_m)
        (dataset_root / f"{table['name']}.tmdl").write_text(tmdl_content)

    # ── 15. ZIP ───────────────────────────────────────────────────────────────
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
