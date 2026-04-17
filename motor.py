
import pandas as pd
import shutil
import os

def detectar_dominio(texto):
    if texto and "venta" in texto.lower():
        return "sales"
    return "general"

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

    # medidas básicas
    lines.append("    measure Total = SUM(TP21[PrecioProformaPEN])")

    return "\n".join(lines)

def generar_proyecto(necesidad, archivo):
    df = pd.read_excel(archivo)
    columnas = df.columns.tolist()

    tmdl = generar_tmdl(columnas)

    # crear estructura mínima
    os.makedirs("output_pbip/SemanticModel/definition/tables", exist_ok=True)

    path = "output_pbip/SemanticModel/definition/tables/TP21.tmdl"

    with open(path, "w", encoding="utf-8") as f:
        f.write(tmdl)
