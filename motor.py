import pandas as pd
import os
import zipfile

def generar_proyecto(necesidad, archivo):

    df = pd.read_excel(archivo)

    # limpieza básica
    df_clean = df.copy()

    # guardar archivo limpio
    output_excel = "modelo_limpio.xlsx"
    df_clean.to_excel(output_excel, index=False)

    # generar archivo de métricas sugeridas
    medidas = [
        "Total Ventas = SUM(Tabla[PrecioProformaPEN])",
        "Promedio Precio = AVERAGE(Tabla[PrecioProformaPEN])",
        "Conteo = COUNTROWS(Tabla)"
    ]

    with open("medidas.txt", "w") as f:
        for m in medidas:
            f.write(m + "\n")

    # empaquetar todo
    zip_path = "proyecto_bi.zip"

    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, 'w') as z:
        z.write(output_excel)
        z.write("medidas.txt")

    return zip_path
