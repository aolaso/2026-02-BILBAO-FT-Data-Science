import os
import shutil
from variables import *


def crear_carpetas(ruta_base):
    for carpeta in CARPETAS:
        ruta_carpeta = os.path.join(ruta_base, carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)


def clasificar_archivo(nombre_archivo):
    _, extension = os.path.splitext(nombre_archivo)
    extension = extension.lower()
    if extension in doc_types:
        return "Documentos"
    elif extension in img_types:
        return "Imagenes"
    elif extension in software_types:
        return "Software"
    else:
        return "Otros"


def ordenar_carpeta(ruta_base):
    crear_carpetas(ruta_base)
    for elemento in os.listdir(ruta_base):
        ruta_completa = os.path.join(ruta_base, elemento)
        if os.path.isfile(ruta_completa):
            carpeta_destino = clasificar_archivo(elemento)
            destino = os.path.join(ruta_base, carpeta_destino, elemento)
            shutil.move(ruta_completa, destino)
            print(f"  {elemento}  ->  {carpeta_destino}/")
    print("\nOrdenación completada")
