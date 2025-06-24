"""
Módulo de Operaciones Elementales con Matrices
Contiene todas las operaciones básicas: suma, resta, multiplicación, 
transpuesta, inversa, etc.
"""
import numpy as np
import sys
import os

# Agregar ruta para importar GaussJordan y archiveUtil
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Repositories'))
from Repositories.gaussJordan import GaussJordan


class OperacionesMatrices:
    """
    Clase para realizar operaciones elementales con matrices
    Implementa las operaciones paso a paso como se hacen a mano
    """
    
    def __init__(self):
        self.nombre = "Operaciones Elementales de Matrices"
    
    # =================== OPERACIONES ELEMENTALES PASO A PASO ===================
    
    def sumaMatrices(self, matrizA, matrizB):
        """
        Suma dos matrices elemento por elemento
        Algoritmo: resultado[i,j] = A[i,j] + B[i,j]
        """
        try:
            if matrizA.shape != matrizB.shape:
                return False
            
            filas, columnas = matrizA.shape
            resultado = np.zeros((filas, columnas))
            
            # OPERACIÓN ELEMENTAL: bucles anidados
            for i in range(filas):
                for j in range(columnas):
                    resultado[i, j] = matrizA[i, j] + matrizB[i, j]
            
            return True
        except Exception:
            return False
    
    def restaMatrices(self, matrizA, matrizB):
        """
        Resta dos matrices elemento por elemento  
        Algoritmo: resultado[i,j] = A[i,j] - B[i,j]
        """
        try:
            if matrizA.shape != matrizB.shape:
                return False
            
            filas, columnas = matrizA.shape
            resultado = np.zeros((filas, columnas))
            
            # OPERACIÓN ELEMENTAL: bucles anidados
            for i in range(filas):
                for j in range(columnas):
                    resultado[i, j] = matrizA[i, j] - matrizB[i, j]
            
            return True
        except Exception:
            return False
    
    def multiplicacionEscalar(self, matriz, escalar):
        """
        Multiplica cada elemento de la matriz por el escalar
        Algoritmo: resultado[i,j] = escalar × matriz[i,j]
        """
        try:
            filas, columnas = matriz.shape
            resultado = np.zeros((filas, columnas))
            
            # OPERACIÓN ELEMENTAL: bucles anidados
            for i in range(filas):
                for j in range(columnas):
                    resultado[i, j] = escalar * matriz[i, j]
            
            return True
        except Exception:
            return False
    
    def multiplicacionMatrices(self, matrizA, matrizB):
        """
        Multiplica dos matrices usando el algoritmo elemental
        Algoritmo: resultado[i,j] = Σ(A[i,k] × B[k,j]) para k=0 hasta n-1
        """
        try:
            if matrizA.shape[1] != matrizB.shape[0]:
                return False
            
            filasA, columnasA = matrizA.shape
            filasB, columnasB = matrizB.shape
            resultado = np.zeros((filasA, columnasB))
            
            # OPERACIÓN ELEMENTAL: triple bucle anidado
            for i in range(filasA):              # Para cada fila de A
                for j in range(columnasB):       # Para cada columna de B
                    suma = 0.0
                    for k in range(columnasA):   # Suma de productos
                        suma += matrizA[i, k] * matrizB[k, j]
                    resultado[i, j] = suma
            
            return True
        except Exception:
            return False
    
    def transpuesta(self, matriz):
        """
        Calcula la transpuesta intercambiando filas y columnas
        Algoritmo: resultado[i,j] = matriz[j,i]
        """
        try:
            filas, columnas = matriz.shape
            resultado = np.zeros((columnas, filas))
            
            # OPERACIÓN ELEMENTAL: intercambio de índices
            for i in range(filas):
                for j in range(columnas):
                    resultado[j, i] = matriz[i, j]
            
            return True
        except Exception:
            return False
    
    def matrizInversa(self, matriz):
        """
        Calcula la matriz inversa usando el método de Gauss-Jordan
        Algoritmo: [A|I] -> [I|A^-1] mediante eliminación gaussiana
        Utiliza la clase GaussJordan existente
        """
        try:
            # Verificar que la matriz sea cuadrada
            filas, columnas = matriz.shape
            if filas != columnas:
                return False
            
            n = filas
            
            # Crear matriz identidad del mismo tamaño
            identidad = np.eye(n)
            
            # Crear matriz aumentada [A|I]
            matrizAumentada = np.hstack((matriz.copy(), identidad))
            
            # Usar la clase GaussJordan existente
            try:
                solver = GaussJordan(matrizAumentada)
                # La matriz resultante está en solver.augmentedMatrix
                matrizResultado = solver.augmentedMatrix
                
                # Verificar que la parte izquierda sea la identidad
                parteIzquierda = matrizResultado[:, :n]
                if np.allclose(parteIzquierda, np.eye(n), rtol=1e-9, atol=1e-9):
                    # La operación fue exitosa
                    # La inversa está en la parte derecha
                    return True
                else:
                    # La matriz no es invertible
                    return False
                    
            except Exception:
                # Si GaussJordan lanza una excepción (por ejemplo, pivote cero), 
                # la matriz no es invertible
                return False
                
        except Exception:
            return False
    
    def calcularTranspuesta(self, matriz):
        """
        Calcula y retorna la transpuesta de una matriz
        """
        filas, columnas = matriz.shape
        resultado = np.zeros((columnas, filas))
        
        for i in range(filas):
            for j in range(columnas):
                resultado[j, i] = matriz[i, j]
        
        return resultado
    
    def calcularInversa(self, matriz):
        """
        Calcula y retorna la inversa de una matriz
        Retorna None si la matriz no es invertible
        """
        # Verificar que la matriz sea cuadrada
        filas, columnas = matriz.shape
        if filas != columnas:
            return None
        
        n = filas
        
        # Crear matriz identidad del mismo tamaño
        identidad = np.eye(n)
        
        # Crear matriz aumentada [A|I]
        matrizAumentada = np.hstack((matriz.copy(), identidad))
        
        try:
            solver = GaussJordan(matrizAumentada)
            matrizResultado = solver.augmentedMatrix
            
            # Verificar que la parte izquierda sea la identidad
            parteIzquierda = matrizResultado[:, :n]
            if np.allclose(parteIzquierda, np.eye(n), rtol=1e-9, atol=1e-9):
                # Retornar la inversa que está en la parte derecha
                return matrizResultado[:, n:]
            else:
                return None
                
        except Exception:
            return None
    
    def aplicarEscalar(self, matriz, escalar):
        """
        Multiplica una matriz por un escalar y retorna el resultado
        """
        filas, columnas = matriz.shape
        resultado = np.zeros((filas, columnas))
        
        for i in range(filas):
            for j in range(columnas):
                resultado[i, j] = escalar * matriz[i, j]
        
        return resultado
    
    def sumarMatrices(self, matrizA, matrizB):
        """
        Suma dos matrices y retorna el resultado
        """
        if matrizA.shape != matrizB.shape:
            return None
            
        filas, columnas = matrizA.shape
        resultado = np.zeros((filas, columnas))
        
        for i in range(filas):
            for j in range(columnas):
                resultado[i, j] = matrizA[i, j] + matrizB[i, j]
        
        return resultado 