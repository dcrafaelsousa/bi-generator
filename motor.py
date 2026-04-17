import os
import shutil
import zipfile
import json
import uuid

def generar_proyecto(necesidad, archivo):

    base = "pbip_generado"
    name = "Store Sales"

    if os.path.exists(base):
        shutil.rmtree(base)

    # =========================
    # ESTRUCTURA COMPLETA
    # =========================
    os.makedirs(f"{base}/{name}.Report/definition/pages", exist_ok=True)
    os.makedirs(f"{base}/{name}.SemanticModel/definition/tables", exist_ok=True)

    # =========================
    # PBIP (MODERNO + REFERENCIA)
    # =========================
    with open(f"{base}/{name}.pbip", "w") as f:
        json.dump({
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json",
            "version": "1.0",
            "settings": {},
            "references": {
                "report": f"{name}.Report",
                "semanticModel": f"{name}.SemanticModel"
            }
        }, f, indent=2)

    # =========================
    # REPORT
    # =========================
    report_id = str(uuid.uuid4())

    with open(f"{base}/{name}.Report/.platform", "w") as f:
        json.dump({
            "logicalId": report_id,
            "type": "Report"
        }, f)

    with open(f"{base}/{name}.Report/definition/definition.pbir", "w") as f:
        json.dump({
            "version": "4.0",
            "datasetReference": {
                "byPath": {
                    "path": f"../{name}.SemanticModel"
                }
            }
        }, f, indent=2)

    with open(f"{base}/{name}.Report/definition/version.json", "w") as f:
        json.dump({
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/version/1.0.0/schema.json",
            "version": "1.0"
        }, f, indent=2)

    with open(f"{base}/{name}.Report/definition/pages/pages.json", "w") as f:
        json.dump({
            "activePageName": "Page1",
            "pageOrder": ["Page1"]
        }, f, indent=2)

    with open(f"{base}/{name}.Report/definition/report.json", "w") as f:
        json.dump({
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/1.0.0/schema.json",
            "id": report_id,
            "themeCollection": {},
            "sections": []
        }, f, indent=2)

    # =========================
    # SEMANTIC MODEL
    # =========================
    with open(f"{base}/{name}.SemanticModel/definition.pbism", "w") as f:
        json.dump({
            "version": "4.2"
        }, f, indent=2)

    with open(f"{base}/{name}.SemanticModel/definition/model.tmdl", "w") as f:
        f.write("""
model Model
    culture: "en-US"
""")

    with open(f"{base}/{name}.SemanticModel/definition/database.tmdl", "w") as f:
        f.write("""
database Database
""")

    with open(f"{base}/{name}.SemanticModel/definition/tables/Tabla.tmdl", "w") as f:
        f.write("""
table Tabla
    column Columna1
        dataType: string
""")

    # =========================
    # ZIP CORRECTO
    # =========================
    zip_path = "proyecto_pbip.zip"

    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(base):
            for file in files:
                full = os.path.join(root, file)
                arc = os.path.relpath(full, base)
                z.write(full, arc)

    return zip_path
