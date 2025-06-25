import numpy as np

from Repositories.significantFigures import significantFigures
from Repositories.numericSystem import numericSystem



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

    dataArray = np.full((filas, max_columnas), "0", dtype='U256')
    
    return dataArray

    
            
            

    