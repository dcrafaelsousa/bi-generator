import os
import shutil
import zipfile

def generar_proyecto(necesidad, archivo):

    template = "template_pbip"
    output = "pbip_generado"

    # limpiar salida
    if os.path.exists(output):
        shutil.rmtree(output)

    # copiar plantilla
    shutil.copytree(template, output)

    # zip final
    zip_path = "proyecto_pbip.zip"

    if os.path.exists(zip_path):
        os.remove(zip_path)

    with zipfile.ZipFile(zip_path, 'w') as z:
        for root, dirs, files in os.walk(output):
            for file in files:
                full = os.path.join(root, file)
                z.write(full, os.path.relpath(full, output))

    return zip_path
