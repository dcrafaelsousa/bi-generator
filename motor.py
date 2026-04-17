import os
import shutil
import zipfile
import json
import uuid

def generar_proyecto(necesidad, archivo):

    base = "pbip_generado"
    name = "proyecto"

    if os.path.exists(base):
        shutil.rmtree(base)

    # =========================
    # ESTRUCTURA
    # =========================
    os.makedirs(f"{base}/{name}.Report/definition/pages", exist_ok=True)
    os.makedirs(f"{base}/{name}.SemanticModel/tables", exist_ok=True)

    # =========================
    # PBIP
    # =========================
    with open(f"{base}/{name}.pbip", "w") as f:
        json.dump({
            "version": "1.0",
            "artifacts": [
                {
                    "report": {
                        "path": f"{name}.Report"
                    }
                }
            ]
        }, f, indent=2)

    # =========================
    # REPORT
    # =========================
    with open(f"{base}/{name}.Report/.platform", "w") as f:
        json.dump({
            "logicalId": str(uuid.uuid4()),
            "type": "Report"
        }, f)

    with open(f"{base}/{name}.Report/definition/version.json", "w") as f:
        json.dump({
            "version": "1.0"
        }, f)

    with open(f"{base}/{name}.Report/definition/pages/pages.json", "w") as f:
        json.dump({
            "activePageName": "Page1",
            "pageOrder": ["Page1"]
        }, f)

    with open(f"{base}/{name}.Report/definition/report.json", "w") as f:
        json.dump({
            "name": "Report",
            "sections": []
        }, f)

    # =========================
    # SEMANTIC MODEL
    # =========================
    with open(f"{base}/{name}.SemanticModel/definition.pbism", "w") as f:
        json.dump({
            "version": "4.2"
        }, f)

    with open(f"{base}/{name}.SemanticModel/model.tmdl", "w") as f:
        f.write("model Model {}")

    with open(f"{base}/{name}.SemanticModel/database.tmdl", "w") as f:
        f.write("database Database {}")

    with open(f"{base}/{name}.SemanticModel/tables/Tabla.tmdl", "w") as f:
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
