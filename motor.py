import pandas as pd
import os
import zipfile

def mapear_tipo(col):
    if "Fecha" in col:
        return "dateTime"
    if "Precio" in col or "Area" in col:
        return "double"
    return "string"

def generar_tmdl(columnas):
    lines = ["createOrReplace", "", "table TP21"]

    for col in columnas:
        tipo = mapear_tipo(col)
        lines.append(f"    column {col}")
        lines.append(f"        dataType: {tipo}")
        lines.append("")

    lines.append("    measure Total = SUM(TP21[PrecioProformaPEN])")

    return "\n".join(lines)

def generar_proyecto(necesidad, archivo):

    df = pd.read_excel(archivo)
    columnas = df.columns.tolist()

    base = "pbip_project"

    # estructura
    os.makedirs(f"{base}/SemanticModel/definition/tables", exist_ok=True)
    os.makedirs(f"{base}/Report", exist_ok=True)

    # TMDL tabla
    tmdl = generar_tmdl(columnas)
    with open(f"{base}/SemanticModel/definition/tables/TP21.tmdl", "w") as f:
        f.write(tmdl)

    # model.tmdl mínimo
    with open(f"{base}/SemanticModel/definition/model.tmdl", "w") as f:
        f.write("model Model {}")

    # definition.pbism
    with open(f"{base}/SemanticModel/definition.pbism", "w") as f:
        f.write('{"version":"1.0"}')

    # report mínimo
    with open(f"{base}/Report/definition.pbir", "w") as f:
        f.write('{}')

    # archivo pbip
    with open(f"{base}/proyecto.pbip", "w") as f:
        f.write('{"version":"1.0","artifacts":[]}')

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
