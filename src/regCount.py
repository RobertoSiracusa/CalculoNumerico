import numpy as np

def regisCant(archivo):
    filaColum = np.array([0, 0]) # Ahora es un arreglo de NumPy

    if (archivo == None):
        print("Objet-File: Archivo vacio.")
        return filaColum

    campo = []
    cont = 0
    band = 0
    aux = 0

    for i in archivo:
        cont = cont + 1
        campo = i.decode('utf-8').split("/")

        if (band == 0):
            aux = len(campo)
            band = 1
        elif (len(campo) > aux):
            aux = len(campo)

    filaColum[0] = aux
    filaColum[1] = cont

    return filaColum