import os
import shutil
import zipfile
import json
from pathlib import Path

def generar_proyecto(necesidad=None, archivo=None):
    # Configuración
    base = Path("pbip_generado")
    name = "proyecto"

    # Limpieza inicial
    if base.exists():
        shutil.rmtree(base)

    # 1. Crear estructura de carpetas
    # Carpetas principales
    (base / f"{name}.Report" / "definition" / "pages").mkdir(parents=True)
    (base / f"{name}.Dataset" / "definition").mkdir(parents=True)

    # 2. Archivo raíz: proyecto.pbip
    (base / f"{name}.pbip").write_text(json.dumps({
        "version": "1.0",
        "artifacts": [{"report": {"path": f"{name}.Report"}}],
        "settings": {"enableAutoRecovery": True}
    }, indent=2))

    # 3. Archivos del Reporte (.Report)
    # definition.pbir (referencia al dataset)
    (base / f"{name}.Report" / "definition" / "definition.pbir").write_text(json.dumps({
        "version": "1.0",  # ¡Importante: "1.0" y no "4.0"!
        "datasetReference": {
            "byPath": {"path": f"../../{name}.Dataset"},
            "byConnection": None
        }
    }, indent=2))

    # report.json (con al menos una página/sección)
    (base / f"{name}.Report" / "definition" / "report.json").write_text(json.dumps({
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

    # pages.json (requerido aunque esté vacío)
    (base / f"{name}.Report" / "definition" / "pages" / "pages.json").write_text(json.dumps({
        "activePageName": "Página 1",
        "pageOrder": ["Página 1"]
    }, indent=2))

    # 4. Archivos del Dataset (.Dataset)
    # definition.pbidataset (configuración del dataset)
    (base / f"{name}.Dataset" / "definition" / "definition.pbidataset").write_text(json.dumps({
        "version": "1.0",
        "settings": {}
    }, indent=2))

    # model.bim (modelo semántico)
    (base / f"{name}.Dataset" / "definition" / "model.bim").write_text(json.dumps({
        "name": "Modelo",
        "compatibilityLevel": 1550,  # Un nivel de compatibilidad moderno
        "model": {
            "culture": "es-ES",
            "defaultPowerBIDataSourceVersion": "powerBI_V3",
            "tables": []
        }
    }, indent=2))

    # 5. Empaquetado en ZIP
    zip_path = Path("proyecto_pbip.zip")
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in base.rglob("*"):
            if file.is_file():
                z.write(file, file.relative_to(base))

    return str(zip_path)

# Ejemplo de uso
if __name__ == "__main__":
    ruta_zip = generar_proyecto()
    print(f"Proyecto generado en: {ruta_zip}")
