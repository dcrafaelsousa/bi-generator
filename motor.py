import os
import shutil
import zipfile
import json

def generar_proyecto(necesidad, archivo):
    output = "pbip_generado"
    project_name = "proyecto"

    if os.path.exists(output):
        shutil.rmtree(output)
    os.makedirs(output)

    # archivo pbip
    pbip_content = {
        "version": "1.0",
        "artifacts": [
            {
                "report": {
                    "path": f"{project_name}.Report"
                }
            }
        ]
    }

    with open(os.path.join(output, f"{project_name}.pbip"), "w") as f:
        json.dump(pbip_content, f, indent=2)

    # carpeta Report
    report_dir = os.path.join(output, f"{project_name}.Report")
    os.makedirs(report_dir)

    with open(os.path.join(report_dir, "definition.pbir"), "w") as f:
        json.dump({
            "version": "4.0",
            "datasetReference": {
                "byPath": {
                    "path": f"../{project_name}.Dataset"
                }
            }
        }, f, indent=2)

    with open(os.path.join(report_dir, "report.json"), "w") as f:
        json.dump({
            "id": "00000000-0000-0000-0000-000000000001",
            "sections": []
        }, f, indent=2)

    # carpeta Dataset
    dataset_dir = os.path.join(output, f"{project_name}.Dataset")
    os.makedirs(dataset_dir)

    with open(os.path.join(dataset_dir, "definition.pbidataset"), "w") as f:
        json.dump({
            "version": "1.0",
            "model": {
                "tables": []
            }
        }, f, indent=2)

    # zip correcto
    zip_path = "proyecto_pbip.zip"

    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(output):
            for file in files:
                full = os.path.join(root, file)
                arcname = os.path.relpath(full, output)
                z.write(full, arcname)

    return zip_path
