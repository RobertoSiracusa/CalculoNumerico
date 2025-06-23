import numpy as np
from datetime import datetime
import re

class OperacionesElementalesMatrices:
    """
    Clase para realizar operaciones elementales con matrices
    Implementa las operaciones paso a paso como se hacen a mano
    No imprime resultados, solo valida que las operaciones funcionen
    """
    
    def __init__(self):
        self.nombre = "Operaciones Elementales de Matrices"
        self.matrices_disponibles = {}
    
    def registrar_matriz(self, nombre, matriz):
        """Registra una matriz en el sistema"""
        try:
            if not isinstance(matriz, np.ndarray):
                matriz = np.array(matriz, dtype=float)
            self.matrices_disponibles[nombre] = matriz
            return True
        except Exception:
            return False
    
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
    
    # =================== VALIDACIÓN DE FÓRMULAS ===================
    
    def validar_estructura_formula(self, formula):
        """Valida si una fórmula tiene estructura correcta"""
        try:
            formula_limpia = formula.replace(" ", "")
            
            if not formula_limpia:
                return False
            
            # Patrón para términos válidos: [signo][escalar][matriz][transpuesta]
            patron_termino_valido = r'([+-]?)(\d*\.?\d*)([A-Z])(\^T)?'
            matches = list(re.finditer(patron_termino_valido, formula_limpia))
            terminos_validos = ''.join(match.group() for match in matches)
            
            # Verificar que toda la fórmula consiste solo de términos válidos
            if formula_limpia != terminos_validos:
                return False
            
            return True
        except Exception:
            return False
    
    def validar_matrices_disponibles(self, formula):
        """Valida si todas las matrices de la fórmula están disponibles"""
        try:
            formula_limpia = formula.replace(" ", "")
            formula_sin_transpuestas = re.sub(r'\^T', '', formula_limpia)
            matrices_encontradas = set(re.findall(r'[A-Z]', formula_sin_transpuestas))
            
            for matriz in matrices_encontradas:
                if matriz not in self.matrices_disponibles:
                    return False
            
            return True
        except Exception:
            return False
    
    def validar_dimensiones_compatibles(self, formula):
        """Valida si las dimensiones de las matrices son compatibles"""
        try:
            terminos = self.extraer_terminos_formula(formula)
            if not terminos:
                return False
            
            # Obtener dimensión esperada del primer término
            primer_termino = terminos[0]
            matriz_base = self.matrices_disponibles[primer_termino['matriz']]
            
            if primer_termino['transpuesta']:
                dimension_esperada = (matriz_base.shape[1], matriz_base.shape[0])
            else:
                dimension_esperada = matriz_base.shape
            
            # Verificar que todos los términos tengan la misma dimensión
            for termino in terminos[1:]:
                matriz = self.matrices_disponibles[termino['matriz']]
                
                if termino['transpuesta']:
                    dimension_actual = (matriz.shape[1], matriz.shape[0])
                else:
                    dimension_actual = matriz.shape
                
                if dimension_actual != dimension_esperada:
                    return False
            
            return True
        except Exception:
            return False
    
    # =================== PROCESAMIENTO DE FÓRMULAS ===================
    
    def extraer_terminos_formula(self, formula):
        """Extrae y procesa los términos de una fórmula"""
        try:
            formula_limpia = formula.replace(" ", "")
            patron_termino = r'([+-]?)(\d*\.?\d*)([A-Z])(\^T)?'
            matches = re.findall(patron_termino, formula_limpia)
            
            terminos = []
            for i, (signo, escalar_str, nombre_matriz, transpuesta_str) in enumerate(matches):
                # Determinar escalar
                if escalar_str == '':
                    escalar_base = 1.0
                else:
                    escalar_base = float(escalar_str)
                
                # Aplicar signo
                if i == 0 and signo == '':
                    escalar_final = escalar_base
                elif signo == '-':
                    escalar_final = -escalar_base
                else:
                    escalar_final = escalar_base
                
                terminos.append({
                    'escalar': escalar_final,
                    'matriz': nombre_matriz,
                    'transpuesta': transpuesta_str == '^T',
                    'tiene_escalar_explicito': escalar_str != ''
                })
            
            return terminos
        except Exception:
            return []
    
    def evaluar_formula_interna(self, formula):
        """
        Evalúa una fórmula internamente usando operaciones elementales
        """
        try:
            terminos = self.extraer_terminos_formula(formula)
            if not terminos:
                return False
            
            resultado = None
            
            for termino in terminos:
                # Obtener matriz original
                matriz_original = self.matrices_disponibles[termino['matriz']]
                
                # Aplicar transpuesta si es necesario (usando operación elemental)
                if termino['transpuesta']:
                    filas, columnas = matriz_original.shape
                    matriz_transpuesta = np.zeros((columnas, filas))
                    
                    # TRANSPUESTA ELEMENTAL
                    for i in range(filas):
                        for j in range(columnas):
                            matriz_transpuesta[j, i] = matriz_original[i, j]
                    
                    matriz_procesada = matriz_transpuesta
                else:
                    matriz_procesada = matriz_original.copy()
                
                # Aplicar multiplicación escalar si es necesario (usando operación elemental)
                if termino['tiene_escalar_explicito'] or termino['escalar'] != 1.0:
                    filas, columnas = matriz_procesada.shape
                    matriz_escalada = np.zeros((filas, columnas))
                    
                    # MULTIPLICACIÓN ESCALAR ELEMENTAL
                    for i in range(filas):
                        for j in range(columnas):
                            matriz_escalada[i, j] = termino['escalar'] * matriz_procesada[i, j]
                    
                    matriz_procesada = matriz_escalada
                
                # Sumar al resultado (usando operación elemental)
                if resultado is None:
                    resultado = matriz_procesada.copy()
                else:
                    filas, columnas = resultado.shape
                    
                    # SUMA ELEMENTAL
                    for i in range(filas):
                        for j in range(columnas):
                            resultado[i, j] = resultado[i, j] + matriz_procesada[i, j]
            
            return True
        except Exception:
            return False
    
    # =================== FUNCIÓN PRINCIPAL ===================
    
    def validar_formula(self, formula):
        """
        Función principal que valida completamente una fórmula
        Realiza todas las operaciones elementales internamente pero solo retorna True/False
        """
        try:
            # 1. Validar estructura
            if not self.validar_estructura_formula(formula):
                return False
            
            # 2. Validar matrices disponibles
            if not self.validar_matrices_disponibles(formula):
                return False
            
            # 3. Validar dimensiones compatibles
            if not self.validar_dimensiones_compatibles(formula):
                return False
            
            # 4. Intentar evaluar la fórmula usando operaciones elementales
            if not self.evaluar_formula_interna(formula):
                return False
            
            return True
        except Exception:
            return False
    
    # =================== UTILIDADES ===================
    
    def obtener_info_sistema(self):
        """Retorna información básica del sistema"""
        return {
            'matrices_registradas': len(self.matrices_disponibles),
            'nombres_matrices': list(self.matrices_disponibles.keys())
        }
    
    def limpiar_matrices(self):
        """Limpia todas las matrices registradas"""
        self.matrices_disponibles.clear()
        return True
