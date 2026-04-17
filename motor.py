import pandas as pd
import os
import zipfile
import shutil

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

    tmdl = generar_tmdl(columnas)

    base_path = "output_pbip/SemanticModel/definition/tables"
    os.makedirs(base_path, exist_ok=True)

    tmdl_path = os.path.join(base_path, "TP21.tmdl")

    with open(tmdl_path, "w", encoding="utf-8") as f:
        f.write(tmdl)

    # crear ZIP descargable
    zip_path = "output_pbip.zip"

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk("output_pbip"):
            for file in files:
                full_path = os.path.join(root, file)
                z.write(full_path, os.path.relpath(full_path, "output_pbip"))

    return zip_path
