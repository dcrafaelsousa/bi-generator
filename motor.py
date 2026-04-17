import shutil
import zipfile
import json
from pathlib import Path

def generar_proyecto(necesidad=None, archivo=None):
    base = Path("pbip_generado")
    name = "proyecto"

    if base.exists():
        shutil.rmtree(base)

    # 1. Crear carpetas según la estructura PBIP estándar
    # Reporte
    report_root = base / f"{name}.Report"
    report_def = report_root / "definition"
    pages_dir = report_def / "pages"
    # Dataset
    dataset_root = base / f"{name}.Dataset"
    dataset_def = dataset_root / "definition"

    report_root.mkdir(parents=True)
    report_def.mkdir(parents=True)
    pages_dir.mkdir(parents=True)
    dataset_root.mkdir(parents=True)
    dataset_def.mkdir(parents=True)

    # 2. Archivo raíz del proyecto (.pbip)
    (base / f"{name}.pbip").write_text(json.dumps({
        "version": "1.0",
        "artifacts": [
            {"report": {"path": f"{name}.Report"}},
            {"dataset": {"path": f"{name}.Dataset"}}
        ],
        "settings": {"enableAutoRecovery": True}
    }, indent=2))

    # 3. definition.pbir (en la raíz del reporte) - EL ARCHIVO CLAVE
    # Contenido según esquema actual: debe incluir "datasetReference" y "version"
    (report_root / "definition.pbir").write_text(json.dumps({
        "version": "1.0",
        "datasetReference": {
            "byPath": {"path": f"../{name}.Dataset"},
            "byConnection": None
        }
    }, indent=2))

    # 4. report.json (dentro de definition/)
    (report_def / "report.json").write_text(json.dumps({
        "version": "1.0",
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
        "resourcePackages": []
    }, indent=2))

    # 5. pages.json
    (pages_dir / "pages.json").write_text(json.dumps({
        "activePageName": "Página 1",
        "pageOrder": ["Página 1"]
    }, indent=2))

    # 6. definition.pbidataset (en la raíz del dataset)
    (dataset_root / "definition.pbidataset").write_text(json.dumps({
        "version": "1.0",
        "settings": {}
    }, indent=2))

    # 7. model.bim (dentro de definition/ del dataset)
    (dataset_def / "model.bim").write_text(json.dumps({
        "name": "Modelo",
        "compatibilityLevel": 1550,
        "model": {
            "culture": "es-ES",
            "defaultPowerBIDataSourceVersion": "powerBI_V3",
            "tables": []
        }
    }, indent=2))

    # 8. Crear ZIP (opcional)
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
