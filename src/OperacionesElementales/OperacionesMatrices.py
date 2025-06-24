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
    
    def suma_matrices(self, matriz_a, matriz_b):
        """
        Suma dos matrices elemento por elemento
        Algoritmo: resultado[i,j] = A[i,j] + B[i,j]
        """
        try:
            if matriz_a.shape != matriz_b.shape:
                return False
            
            filas, columnas = matriz_a.shape
            resultado = np.zeros((filas, columnas))
            
            # OPERACIÓN ELEMENTAL: bucles anidados
            for i in range(filas):
                for j in range(columnas):
                    resultado[i, j] = matriz_a[i, j] + matriz_b[i, j]
            
            return True
        except Exception:
            return False
    
    def resta_matrices(self, matriz_a, matriz_b):
        """
        Resta dos matrices elemento por elemento  
        Algoritmo: resultado[i,j] = A[i,j] - B[i,j]
        """
        try:
            if matriz_a.shape != matriz_b.shape:
                return False
            
            filas, columnas = matriz_a.shape
            resultado = np.zeros((filas, columnas))
            
            # OPERACIÓN ELEMENTAL: bucles anidados
            for i in range(filas):
                for j in range(columnas):
                    resultado[i, j] = matriz_a[i, j] - matriz_b[i, j]
            
            return True
        except Exception:
            return False
    
    def multiplicacion_escalar(self, matriz, escalar):
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
    
    def multiplicacion_matrices(self, matriz_a, matriz_b):
        """
        Multiplica dos matrices usando el algoritmo elemental
        Algoritmo: resultado[i,j] = Σ(A[i,k] × B[k,j]) para k=0 hasta n-1
        """
        try:
            if matriz_a.shape[1] != matriz_b.shape[0]:
                return False
            
            filas_a, columnas_a = matriz_a.shape
            filas_b, columnas_b = matriz_b.shape
            resultado = np.zeros((filas_a, columnas_b))
            
            # OPERACIÓN ELEMENTAL: triple bucle anidado
            for i in range(filas_a):              # Para cada fila de A
                for j in range(columnas_b):       # Para cada columna de B
                    suma = 0.0
                    for k in range(columnas_a):   # Suma de productos
                        suma += matriz_a[i, k] * matriz_b[k, j]
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
    
    def matriz_inversa(self, matriz):
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
            matriz_aumentada = np.hstack((matriz.copy(), identidad))
            
            # Usar la clase GaussJordan existente
            try:
                solver = GaussJordan(matriz_aumentada)
                # La matriz resultante está en solver.augmentedMatrix
                matriz_resultado = solver.augmentedMatrix
                
                # Verificar que la parte izquierda sea la identidad
                parte_izquierda = matriz_resultado[:, :n]
                if np.allclose(parte_izquierda, np.eye(n), rtol=1e-9, atol=1e-9):
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
    
    def calcular_transpuesta(self, matriz):
        """
        Calcula y retorna la transpuesta de una matriz
        """
        filas, columnas = matriz.shape
        resultado = np.zeros((columnas, filas))
        
        for i in range(filas):
            for j in range(columnas):
                resultado[j, i] = matriz[i, j]
        
        return resultado
    
    def calcular_inversa(self, matriz):
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
        matriz_aumentada = np.hstack((matriz.copy(), identidad))
        
        try:
            solver = GaussJordan(matriz_aumentada)
            matriz_resultado = solver.augmentedMatrix
            
            # Verificar que la parte izquierda sea la identidad
            parte_izquierda = matriz_resultado[:, :n]
            if np.allclose(parte_izquierda, np.eye(n), rtol=1e-9, atol=1e-9):
                # Retornar la inversa que está en la parte derecha
                return matriz_resultado[:, n:]
            else:
                return None
                
        except Exception:
            return None
    
    def aplicar_escalar(self, matriz, escalar):
        """
        Multiplica una matriz por un escalar y retorna el resultado
        """
        filas, columnas = matriz.shape
        resultado = np.zeros((filas, columnas))
        
        for i in range(filas):
            for j in range(columnas):
                resultado[i, j] = escalar * matriz[i, j]
        
        return resultado
    
    def sumar_matrices(self, matriz_a, matriz_b):
        """
        Suma dos matrices y retorna el resultado
        """
        if matriz_a.shape != matriz_b.shape:
            return None
            
        filas, columnas = matriz_a.shape
        resultado = np.zeros((filas, columnas))
        
        for i in range(filas):
            for j in range(columnas):
                resultado[i, j] = matriz_a[i, j] + matriz_b[i, j]
        
        return resultado 