import numpy as np
import os
import archiveUtil as ArchiveUtil
import regCount as regCount


def binNumpyArray(binaryContent,dataArray):
    
    # Obtener el contenido binario directamente desde el objeto ArchiveUtil
    decodedContent = binaryContent.decode('utf-8')
    lineas = decodedContent.splitlines()

    
    # Llenar el array con los datos
    for i, linea in enumerate(lineas):
        elementos = linea.split('#')
        for j, elemento in enumerate(elementos):
            # Si el elemento no está vacío, reemplazar el placeholder "%z"
            dataArray[i, j] = elemento
    
    return dataArray

def initArray(binaryContent):
    decodedContent = binaryContent.decode('utf-8')    

    # Contar el número de registros (filas) en el array
    lineas = decodedContent.splitlines()
    filas = len(lineas)
    max_columnas = 0
    
    for linea in lineas:
        # Contar elementos incluso si están vacíos
        elementos = linea.split('#')
        num_elementos = len(elementos)
        if num_elementos > max_columnas:
            max_columnas = num_elementos

    dataArray = np.full((filas, max_columnas), "%z", dtype='U256')
    
    return dataArray

def printArray(dataArray):
    print("Array bidimensional resultante:")
    print(dataArray)
    print(f"\nDimensiones: {dataArray.shape}")
    print(f"Número total de elementos: {dataArray.size}")
        
        # Mostrar contenido de forma estructurada
    print("\nContenido detallado:")
    for i in range(dataArray.shape[0]):
            print(f"Fila {i}:")
            for j in range(dataArray.shape[1]):
                elemento = dataArray[i, j]
                print(f"  Columna {j}: {elemento}")
    print("\nAcceso a un elemento específico:")
    elemento = dataArray[0, 4]  # Acceder al primer elemento de la quinta columna
    print(f"\nElemento específico (Fila 1, Columna 5): {elemento}")