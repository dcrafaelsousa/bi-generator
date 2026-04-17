import shutil
import zipfile
import json
from pathlib import Path

def generar_proyecto(necesidad=None, archivo=None):
    base = Path("pbip_generado")
    name = "proyecto"

    if base.exists():
        shutil.rmtree(base)

    # Carpetas
    report_def = base / f"{name}.Report" / "definition"
    pages_dir = report_def / "pages"
    dataset_def = base / f"{name}.Dataset" / "definition"

    report_def.mkdir(parents=True)
    pages_dir.mkdir(parents=True)
    dataset_def.mkdir(parents=True)

    # 1. Archivo raíz .pbip
    (base / f"{name}.pbip").write_text(json.dumps({
        "version": "1.0",
        "artifacts": [
            {"report": {"path": f"{name}.Report"}},
            {"dataset": {"path": f"{name}.Dataset"}}
        ],
        "settings": {"enableAutoRecovery": True}
    }, indent=2))

    # 2. report.json (incluye datasetReference)
    (report_def / "report.json").write_text(json.dumps({
        "version": "1.0",
        "datasetReference": {
            "byPath": {"path": f"../../{name}.Dataset"},
            "byConnection": None
        },
        "sections": [{
            "displayName": "Página 1",
            "displayOption": 1,
            "filters": "[]",
            "height": 720.00,
            "name": "ReportSection",
            "visualContainers": [],
            "width": 1280.00,
            "config": "{}"
        }],
        "config": "{\"version\":\"5.49\",\"themeCollection\":{\"baseTheme\":{\"name\":\"CY23SU11\",\"version\":\"5.49\",\"type\":2}},\"activeSectionIndex\":0,\"defaultDrillFilterOtherVisuals\":true,\"settings\":{\"useNewFilterPaneExperience\":true,\"allowChangeFilterTypes\":true,\"useStylableVisualContainerHeader\":true,\"queryLimitOption\":6,\"exportDataMode\":1,\"useDefaultAggregateDisplayName\":true}}",
        "layoutOptimization": 0,
        "resourcePackages": [{
            "resourcePackage": {
                "disabled": False,
                "items": [{"name": "CY23SU11", "path": "BaseThemes/CY23SU11.json", "type": 202}],
                "name": "SharedResources",
                "type": 2
            }
        }]
    }, indent=2))

    # 3. dataset.json (en report/definition) - opcional, pero algunos validadores lo piden
    (report_def / "dataset.json").write_text(json.dumps({
        "version": "1.0",
        "datasetReference": {
            "byPath": {"path": f"../../{name}.Dataset"}
        }
    }, indent=2))

    # 4. pages.json
    (pages_dir / "pages.json").write_text(json.dumps({
        "activePageName": "Página 1",
        "pageOrder": ["Página 1"]
    }, indent=2))

    # 5. dataset.json en dataset/definition
    (dataset_def / "dataset.json").write_text(json.dumps({
        "version": "1.0",
        "settings": {}
    }, indent=2))

    # 6. model.bim
    (dataset_def / "model.bim").write_text(json.dumps({
        "name": "Modelo",
        "compatibilityLevel": 1550,
        "model": {
            "culture": "es-ES",
            "defaultPowerBIDataSourceVersion": "powerBI_V3",
            "tables": []
        }
    }, indent=2))

    # 7. (Opcional) Archivo .pbids para conexión vacía, si es necesario
    # (base / f"{name}.Dataset" / f"{name}.pbids").write_text("...")

    # Empaquetar
    zip_path = Path("proyecto_pbip.zip")
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in base.rglob("*"):
            if file.is_file():
                z.write(file, file.relative_to(base))

    return str(zip_path)

if __name__ == "__main__":
    print(generar_proyecto())
