import numpy as np

from Repositories.significantFigures import significantFigures
from Repositories.numericSystem import numericSystem
from Repositories.elementalOperations import elementalOperation


def binNumpyArray(binaryContent,dataArray):
    
    decodedContent = binaryContent.decode('utf-8')
    lineas = decodedContent.splitlines()

    for i, linea in enumerate(lineas):
        elementos = linea.split('#')
        for j, elemento in enumerate(elementos):
            
            dataArray[i, j] = elemento
    
    return dataArray

def initArray(binaryContent):
    decodedContent = binaryContent.decode('utf-8')    

    lineas = decodedContent.splitlines()
    filas = len(lineas)
    max_columnas = 0
    
    for linea in lineas:

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
        

    print("\nContenido detallado:")
    for i in range(dataArray.shape[0]):
            print(f"Fila {i}:")
            for j in range(dataArray.shape[1]):
                elemento = dataArray[i, j]
                print(f"  Columna {j}: {elemento}")
    print("\nAcceso a un elemento específico:")
    elemento = dataArray[0, 4] 
    print(f"\nElemento específico (Fila 1, Columna 5): {elemento}")
    
def processSignificantFigures(dataArray):
    print("\nProcesando cifras significativas:")
    for i in range(dataArray.shape[0]):
        for j in range(dataArray.shape[1]):
            value = dataArray[i, j]
            if value == "%z":  
                continue
            try:
                
                sf = significantFigures(value)
                numeric_system = numericSystem(value)
                eo= elementalOperation(value)
                print( sf.toString()+"\n"+numeric_system.toString()+"\n"+eo.getPrintFormat()+"\n")
            except ValueError as e:
                print(f"Error procesando '{value}': {e}")
                continue
            
            

    