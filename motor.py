import pandas as pd
import os
import zipfile

def generar_proyecto(necesidad, archivo):

    df = pd.read_excel(archivo)
    columnas = df.columns.tolist()

    base = "pbip_project"

    # crear estructura
    os.makedirs(f"{base}/SemanticModel/definition/tables", exist_ok=True)
    os.makedirs(f"{base}/Report", exist_ok=True)

    # tabla TMDL básica
    with open(f"{base}/SemanticModel/definition/tables/TP21.tmdl", "w") as f:
        f.write("table TP21 {}")

    # modelo
    with open(f"{base}/SemanticModel/definition/model.tmdl", "w") as f:
        f.write("model Model {}")

    # pbism
    with open(f"{base}/SemanticModel/definition.pbism", "w") as f:
        f.write('{"version":"1.0"}')

    # report
    with open(f"{base}/Report/definition.pbir", "w") as f:
        f.write('{}')

    # 🔥 PBIP CORRECTO REAL
    with open(f"{base}/proyecto.pbip", "w") as f:
        f.write('''
{
  "version": "1.0",
  "artifacts": [
    {
      "name": "Report",
      "path": "Report",
      "type": "report"
    },
    {
      "name": "SemanticModel",
      "path": "SemanticModel",
      "type": "semanticModel"
    }
  ]
}
''')

    # zip
    zip_path = "proyecto_pbip.zip"

    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, 'w') as z:
        for root, dirs, files in os.walk(base):
            for file in files:
                full = os.path.join(root, file)
                z.write(full, os.path.relpath(full, base))

    return zip_path
