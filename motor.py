import os
import shutil
import zipfile
import json

def generar_proyecto(necesidad, archivo):

    base = "pbip_generado"
    name = "proyecto"

    if os.path.exists(base):
        shutil.rmtree(base)

    os.makedirs(f"{base}/{name}.Report")
    os.makedirs(f"{base}/{name}.Dataset")

    # =========================
    # PBIP (FORMATO QUE TU POWER BI EXIGE)
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
    with open(f"{base}/{name}.Report/definition.pbir", "w") as f:
        json.dump({
            "version": "4.0",
            "datasetReference": {
                "byPath": {
                    "path": f"../{name}.Dataset"
                }
            }
        }, f, indent=2)

    with open(f"{base}/{name}.Report/report.json", "w") as f:
        json.dump({
            "sections": []
        }, f, indent=2)

    # =========================
    # DATASET
    # =========================
    with open(f"{base}/{name}.Dataset/definition.pbidataset", "w") as f:
        json.dump({
            "version": "1.0",
            "model": {
                "tables": []
            }
        }, f, indent=2)

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
