import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Repositories'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Helpers'))

from Repositories.gaussJordan import GaussJordan
from Helpers.utils import logWriter


class MatrixOperations:
    def __init__(self, matrix):
        self.matriz = matrix.astype(float)
        self.checkMatrixEO()

    def checkMatrixEO(self):
        """Método que ejecuta todas las operaciones elementales de matrices"""
        self.addMatrices()
        self.subtractMatrices()
        self.scalarMultiplication()
        self.matrixMultiplication()
        self.transpose()
        self.matrixInverse()

    def addMatrices(self):
        try:
            # Usar la matriz del atributo como A y B
            matrixA = self.matriz
            matrixB = self.matriz  # B = A según condiciones
            
            if matrixA.shape != matrixB.shape:
                errorMsg = "Error: No se puede realizar la suma de las matrices - dimensiones incompatibles"
                logWriter(errorMsg, True)
                return False
            
            rows, columns = matrixA.shape
            result = np.zeros((rows, columns))
            
            for i in range(rows):
                for j in range(columns):
                    result[i, j] = matrixA[i, j] + matrixB[i, j]
            
            return True
        except Exception as e:
            errorMsg = f"Error: No se puede realizar la suma de las matrices - {str(e)}"
            logWriter(errorMsg, True)
            return False
    
    def subtractMatrices(self):
        try:
            # Usar la matriz del atributo como A y B
            matrixA = self.matriz
            matrixB = self.matriz  # B = A según condiciones
            
            if matrixA.shape != matrixB.shape:
                errorMsg = "Error: No se puede realizar la resta de las matrices - dimensiones incompatibles"
                logWriter(errorMsg, True)
                return False
            
            rows, columns = matrixA.shape
            result = np.zeros((rows, columns))
            
            for i in range(rows):
                for j in range(columns):
                    result[i, j] = matrixA[i, j] - matrixB[i, j]
            
            return True
        except Exception as e:
            errorMsg = f"Error: No se puede realizar la resta de las matrices - {str(e)}"
            logWriter(errorMsg, True)
            return False
    
    def scalarMultiplication(self):
        try:
            # Usar escalar = 2 según condiciones
            scalar = 2
            matrix = self.matriz
            
            rows, columns = matrix.shape
            result = np.zeros((rows, columns))
            
            for i in range(rows):
                for j in range(columns):
                    result[i, j] = scalar * matrix[i, j]
            
            return True
        except Exception as e:
            errorMsg = f"Error: No se puede realizar la multiplicacion escalar - {str(e)}"
            logWriter(errorMsg, True)
            return False
    
    def matrixMultiplication(self):
        try:
            # Usar la matriz del atributo como A y B
            matrixA = self.matriz
            matrixB = self.matriz  # B = A según condiciones
            
            if matrixA.shape[1] != matrixB.shape[0]:
                errorMsg = "Error: No se puede realizar la multiplicacion de matrices - dimensiones incompatibles"
                logWriter(errorMsg, True)
                return False
            
            rowsA, columnsA = matrixA.shape
            rowsB, columnsB = matrixB.shape
            result = np.zeros((rowsA, columnsB))
            
            for i in range(rowsA):              
                for j in range(columnsB):      
                    sum = 0.0
                    for k in range(columnsA):   
                        sum += matrixA[i, k] * matrixB[k, j]
                    result[i, j] = sum
            
            return True
        except Exception as e:
            errorMsg = f"Error: No se puede realizar la multiplicacion de matrices - {str(e)}"
            logWriter(errorMsg, True)
            return False
    
    def transpose(self):
        try:
            matrix = self.matriz
            rows, columns = matrix.shape
            result = np.zeros((columns, rows))

            for i in range(rows):
                for j in range(columns):
                    result[j, i] = matrix[i, j]
            
            return True
        except Exception as e:
            errorMsg = f"Error: No se puede realizar la transpuesta de la matriz - {str(e)}"
            logWriter(errorMsg, True)
            return False
    
    def matrixInverse(self):
        try:
            matrix = self.matriz
            rows, columns = matrix.shape
            if rows != columns:
                errorMsg = "Error: No se puede calcular la inversa - la matriz no es cuadrada"
                logWriter(errorMsg, True)
                return False
            
            n = rows
            identity = np.eye(n)
            augmentedMatrix = np.hstack((matrix.copy(), identity))
            
            try:
                solver = GaussJordan(augmentedMatrix)
                resultMatrix = solver.augmentedMatrix

                leftPart = resultMatrix[:, :n]
                if np.allclose(leftPart, np.eye(n), rtol=1e-9, atol=1e-9):
                    return True
                else:
                    errorMsg = "Error: No se puede calcular la inversa - la matriz es singular"
                    logWriter(errorMsg, True)
                    return False
                    
            except Exception as e:
                errorMsg = f"Error: No se puede calcular la inversa - error en Gauss-Jordan: {str(e)}"
                logWriter(errorMsg, True)
                return False
                
        except Exception as e:
            errorMsg = f"Error: No se puede calcular la inversa de la matriz - {str(e)}"
            logWriter(errorMsg, True)
            return False
    
    def calculateTranspose(self):
        try:
            matrix = self.matriz
            rows, columns = matrix.shape
            result = np.zeros((columns, rows))
            
            for i in range(rows):
                for j in range(columns):
                    result[j, i] = matrix[i, j]
            
            return result
        except Exception as e:
            errorMsg = f"Error: No se puede calcular la transpuesta - {str(e)}"
            logWriter(errorMsg, True)
            return None
    
    def calculateInverse(self):
        try:
            matrix = self.matriz
            rows, columns = matrix.shape
            if rows != columns:
                errorMsg = "Error: No se puede calcular la inversa - la matriz no es cuadrada"
                logWriter(errorMsg, True)
                return None
            
            n = rows
            identity = np.eye(n)
            augmentedMatrix = np.hstack((matrix.copy(), identity))
            
            try:
                solver = GaussJordan(augmentedMatrix)
                resultMatrix = solver.augmentedMatrix
                leftPart = resultMatrix[:, :n]

                if np.allclose(leftPart, np.eye(n), rtol=1e-9, atol=1e-9):
                    return resultMatrix[:, n:]
                else:
                    errorMsg = "Error: No se puede calcular la inversa - la matriz es singular"
                    logWriter(errorMsg, True)
                    return None
                    
            except Exception as e:
                errorMsg = f"Error: No se puede calcular la inversa - error en Gauss-Jordan: {str(e)}"
                logWriter(errorMsg, True)
                return None
        except Exception as e:
            errorMsg = f"Error: No se puede calcular la inversa - {str(e)}"
            logWriter(errorMsg, True)
            return None
    
    def applyScalar(self):
        try:
            # Usar escalar = 2 según condiciones
            scalar = 2
            matrix = self.matriz
            
            rows, columns = matrix.shape
            result = np.zeros((rows, columns))
            
            for i in range(rows):
                for j in range(columns):
                    result[i, j] = scalar * matrix[i, j]
            
            return result
        except Exception as e:
            errorMsg = f"Error: No se puede aplicar el escalar a la matriz - {str(e)}"
            logWriter(errorMsg, True)
            return None
    
    def addMatricesResult(self):
        try:
            # Usar la matriz del atributo como A y B
            matrixA = self.matriz
            matrixB = self.matriz  # B = A según condiciones
            
            if matrixA.shape != matrixB.shape:
                errorMsg = "Error: No se puede realizar la suma - dimensiones incompatibles"
                logWriter(errorMsg, True)
                return None
                
            rows, columns = matrixA.shape
            result = np.zeros((rows, columns))
            
            for i in range(rows):
                for j in range(columns):
                    result[i, j] = matrixA[i, j] + matrixB[i, j]
            
            return result
        except Exception as e:
            errorMsg = f"Error: No se puede realizar la suma de matrices - {str(e)}"
            logWriter(errorMsg, True)
            return None
    
    def getMatrix(self):
        """Método para obtener la matriz actual"""
        try:
            return self.matriz.copy()
        except Exception as e:
            errorMsg = f"Error: No se puede obtener la matriz - {str(e)}"
            logWriter(errorMsg, True)
            return None
    
    def setMatrix(self, newMatrix):
        """Método para actualizar la matriz"""
        self.matriz = newMatrix 