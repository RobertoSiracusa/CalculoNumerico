import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Repositories'))
from Repositories.gaussJordan import GaussJordan


class MatrixOperations:
    def __init__(self):
        self.name = "Operaciones Elementales de Matrices"
    
    def addMatrices(self, matrixA, matrixB):
        try:
            if matrixA.shape != matrixB.shape:
                return False
            
            rows, columns = matrixA.shape
            result = np.zeros((rows, columns))
            
            for i in range(rows):
                for j in range(columns):
                    result[i, j] = matrixA[i, j] + matrixB[i, j]
            
            return True
        except Exception:
            return False
    
    def subtractMatrices(self, matrixA, matrixB):
        try:
            if matrixA.shape != matrixB.shape:
                return False
            
            rows, columns = matrixA.shape
            result = np.zeros((rows, columns))
            
            for i in range(rows):
                for j in range(columns):
                    result[i, j] = matrixA[i, j] - matrixB[i, j]
            
            return True
        except Exception:
            return False
    
    def scalarMultiplication(self, matrix, scalar):
        try:
            rows, columns = matrix.shape
            result = np.zeros((rows, columns))
            
            for i in range(rows):
                for j in range(columns):
                    result[i, j] = scalar * matrix[i, j]
            
            return True
        except Exception:
            return False
    
    def matrixMultiplication(self, matrixA, matrixB):
        try:
            if matrixA.shape[1] != matrixB.shape[0]:
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
        except Exception:
            return False
    
    def transpose(self, matrix):
        try:
            rows, columns = matrix.shape
            result = np.zeros((columns, rows))

            for i in range(rows):
                for j in range(columns):
                    result[j, i] = matrix[i, j]
            
            return True
        except Exception:
            return False
    
    def matrixInverse(self, matrix):
        try:
            rows, columns = matrix.shape
            if rows != columns:
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
                    return False
                    
            except Exception:
                return False
                
        except Exception:
            return False
    
    def calculateTranspose(self, matrix):
        rows, columns = matrix.shape
        result = np.zeros((columns, rows))
        
        for i in range(rows):
            for j in range(columns):
                result[j, i] = matrix[i, j]
        
        return result
    
    def calculateInverse(self, matrix):
        rows, columns = matrix.shape
        if rows != columns:
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
                return None
                
        except Exception:
            return None
    
    def applyScalar(self, matrix, scalar):
        rows, columns = matrix.shape
        result = np.zeros((rows, columns))
        
        for i in range(rows):
            for j in range(columns):
                result[i, j] = scalar * matrix[i, j]
        
        return result
    
    def addMatricesResult(self, matrixA, matrixB):
        if matrixA.shape != matrixB.shape:
            return None
            
        rows, columns = matrixA.shape
        result = np.zeros((rows, columns))
        
        for i in range(rows):
            for j in range(columns):
                result[i, j] = matrixA[i, j] + matrixB[i, j]
        
        return result 