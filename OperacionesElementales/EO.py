import numpy as np
from datetime import datetime
import sys
import os

# Agregar ruta para importar archiveUtil
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from Repositories.archiveUtil import ArchiveUtil

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
    
    # =================== ANÁLISIS DE FÓRMULAS SIN REGEX ===================
    
    def es_digito(self, caracter):
        """Verifica si un caracter es dígito"""
        return caracter in '0123456789'
    
    def es_letra_mayuscula(self, caracter):
        """Verifica si un caracter es letra mayúscula"""
        return caracter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def extraer_numero_decimal(self, texto, inicio):
        """
        Extrae un número decimal desde la posición inicio
        Retorna (numero_como_string, nueva_posicion)
        """
        pos = inicio
        numero_str = ""
        punto_encontrado = False
        
        # Extraer dígitos y punto decimal
        while pos < len(texto):
            char = texto[pos]
            if self.es_digito(char):
                numero_str += char
                pos += 1
            elif char == '.' and not punto_encontrado:
                numero_str += char
                punto_encontrado = True
                pos += 1
            else:
                break
        
        return numero_str, pos
    
    def extraer_terminos_formula_manual(self, formula):
        """
        Extrae términos de una fórmula SIN USAR REGEX
        Procesa manualmente caracter por caracter
        """
        try:
            formula_limpia = formula.replace(" ", "")
            terminos = []
            pos = 0
            
            while pos < len(formula_limpia):
                # Inicializar término
                signo = "+"
                escalar_str = ""
                nombre_matriz = ""
                transpuesta = False
                
                # Leer signo
                if pos < len(formula_limpia) and formula_limpia[pos] in "+-":
                    signo = formula_limpia[pos]
                    pos += 1
                elif len(terminos) == 0:
                    # Primer término sin signo explícito
                    signo = "+"
                
                # Leer escalar (número decimal)
                escalar_str, pos = self.extraer_numero_decimal(formula_limpia, pos)
                
                # Leer nombre de matriz (una letra mayúscula)
                if pos < len(formula_limpia) and self.es_letra_mayuscula(formula_limpia[pos]):
                    nombre_matriz = formula_limpia[pos]
                    pos += 1
                else:
                    return []  # Error: se esperaba una matriz
                
                # Leer transpuesta (^T)
                if pos < len(formula_limpia) and formula_limpia[pos] == '^':
                    pos += 1
                    if pos < len(formula_limpia) and formula_limpia[pos] == 'T':
                        transpuesta = True
                        pos += 1
                    else:
                        return []  # Error: se esperaba T después de ^
                
                # Procesar escalar
                if escalar_str == "":
                    escalar_valor = 1.0
                else:
                    try:
                        escalar_valor = float(escalar_str)
                    except ValueError:
                        return []  # Error: escalar inválido
                
                # Aplicar signo
                if signo == "-":
                    escalar_valor = -escalar_valor
                
                # Agregar término
                terminos.append({
                    'escalar': escalar_valor,
                    'matriz': nombre_matriz,
                    'transpuesta': transpuesta,
                    'tiene_escalar_explicito': escalar_str != ""
                })
            
            return terminos
        except Exception:
            return []
    
    def validar_estructura_formula_manual(self, formula):
        """
        Valida la estructura de una fórmula SIN USAR REGEX
        Verifica que solo contenga elementos válidos
        """
        try:
            formula_limpia = formula.replace(" ", "")
            
            if not formula_limpia:
                return False
            
            # Intentar extraer términos
            terminos = self.extraer_terminos_formula_manual(formula)
            if not terminos:
                return False
            
            return True
        except Exception:
            return False
    
    def validar_matrices_disponibles(self, formula):
        """Valida si todas las matrices de la fórmula están disponibles"""
        try:
            terminos = self.extraer_terminos_formula_manual(formula)
            if not terminos:
                return False
            
            for termino in terminos:
                if termino['matriz'] not in self.matrices_disponibles:
                    return False
            
            return True
        except Exception:
            return False
    
    def validar_dimensiones_compatibles(self, formula):
        """Valida si las dimensiones de las matrices son compatibles"""
        try:
            terminos = self.extraer_terminos_formula_manual(formula)
            if not terminos:
                return False
            
            # Calcular dimensión esperada del primer término
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
    
    def evaluar_formula_interna(self, formula):
        """
        Evalúa una fórmula internamente usando operaciones elementales
        """
        try:
            terminos = self.extraer_terminos_formula_manual(formula)
            if not terminos:
                return False
            
            resultado = None
            
            for termino in terminos:
                # Obtener matriz original
                matriz_original = self.matrices_disponibles[termino['matriz']]
                
                # Aplicar transpuesta si es necesario
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
                
                # Aplicar multiplicación escalar si es necesario
                if termino['tiene_escalar_explicito'] or termino['escalar'] != 1.0:
                    filas, columnas = matriz_procesada.shape
                    matriz_escalada = np.zeros((filas, columnas))
                    
                    # MULTIPLICACIÓN ESCALAR ELEMENTAL
                    for i in range(filas):
                        for j in range(columnas):
                            matriz_escalada[i, j] = termino['escalar'] * matriz_procesada[i, j]
                    
                    matriz_procesada = matriz_escalada
                
                # Sumar al resultado
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
        Ahora sin regex
        """
        try:
            # 1. Validar estructura
            if not self.validar_estructura_formula_manual(formula):
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
    
    # =================== FUNCIONES DE COMPATIBILIDAD ===================
    
    def extraer_terminos_formula(self, formula):
        """Función de compatibilidad que usa el nuevo método manual"""
        return self.extraer_terminos_formula_manual(formula)
    
    def validar_estructura_formula(self, formula):
        """Función de compatibilidad que usa el nuevo método manual"""
        return self.validar_estructura_formula_manual(formula)
    
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
    
    def guardar_resultados_txt(self, formulas_archivo):
        """
        Guarda resultados de validación en txt usando setCreateArchive
        Lee fórmulas de un archivo y escribe: fórmula, válida o no
        """
        try:
            # Leer fórmulas del archivo
            archive_util = ArchiveUtil(".")
            formulas = []
            
            with archive_util.getArchive(formulas_archivo) as archivo:
                for linea in archivo:
                    formula = linea.decode('utf-8').strip()
                    if formula:
                        formulas.append(formula)
            
            # Crear contenido del reporte
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            contenido = f"REPORTE VALIDACIÓN - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            contenido += "=" * 50 + "\n\n"
            
            # Procesar cada fórmula
            for formula in formulas:
                resultado = self.validar_formula(formula)
                validez = "VÁLIDA" if resultado else "NO VÁLIDA"
                
                contenido += f"Fórmula: {formula}\n"
                contenido += f"Resultado: {validez}\n"
                contenido += "-" * 30 + "\n"
            
            # Guardar usando setCreateArchive
            nombre_archivo = f"resultados_validacion_{timestamp}"
            archive_util.setCreateArchive(contenido, nombre_archivo, append_newline=False, booleano=True)
            
            return f"{nombre_archivo}.txt"
            
        except Exception as e:
            return None
