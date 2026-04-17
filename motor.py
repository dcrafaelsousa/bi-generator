import os
import shutil
import zipfile
import json
from pathlib import Path

def generar_proyecto(necesidad=None, archivo=None):
    base = Path("pbip_generado")
    name = "proyecto"

    if base.exists():
        shutil.rmtree(base)

    # Crear carpetas según estructura PBIP correcta
    report_def = base / f"{name}.Report" / "definition"
    pages_dir = report_def / "pages"
    dataset_def = base / f"{name}.Dataset" / "definition"

    report_def.mkdir(parents=True)
    pages_dir.mkdir(parents=True)
    dataset_def.mkdir(parents=True)

    # 1. Archivo raíz .pbip
    (base / f"{name}.pbip").write_text(json.dumps({
        "version": "1.0",
        "artifacts": [{"report": {"path": f"{name}.Report"}}]
    }, indent=2))

    # 2. definition.pbir dentro de definition/
    (report_def / "definition.pbir").write_text(json.dumps({
        "version": "4.0",
        "datasetReference": {"byPath": {"path": f"../../{name}.Dataset"}}
    }, indent=2))

    # 3. report.json completo
    (report_def / "report.json").write_text(json.dumps({
        "sections": [],
        "config": {},
        "layoutOptimization": 0,
        "resourcePackages": []
    }, indent=2))

    # 4. pages.json con objeto, no array
    (pages_dir / "pages.json").write_text(json.dumps({
        "activePageName": "Page1",
        "pageOrder": ["Page1"]
    }, indent=2))

    # 5. definition.pbidataset
    (dataset_def / "definition.pbidataset").write_text(json.dumps({
        "version": "1.0",
        "model": {"tables": []}
    }, indent=2))

    # 6. model.bim mínimo
    (dataset_def / "model.bim").write_text(json.dumps({
        "name": "Model",
        "compatibilityLevel": 1520,
        "model": {
            "culture": "es-ES",
            "dataSources": [],
            "tables": [],
            "relationships": []
        }
    }, indent=2))

    # Crear zip
    zip_path = Path("proyecto_pbip.zip")
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in base.rglob("*"):
            if file.is_file():
                z.write(file, file.relative_to(base))

    # Limpieza opcional
    # shutil.rmtree(base)

    return str(zip_path)
