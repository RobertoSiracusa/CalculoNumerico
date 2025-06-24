"""
Módulo de Validación de Fórmulas con Matrices
Contiene toda la lógica para analizar, validar y evaluar fórmulas
con operaciones matriciales como A + B, 2A^T, A^-1, etc.
"""
import numpy as np
from OperacionesMatrices import OperacionesMatrices


class ValidadorFormulas:
    """
    Clase para validar y evaluar fórmulas con matrices
    """
    
    def __init__(self):
        self.matrices_disponibles = {}
        self.operaciones = OperacionesMatrices()
    
    def registrar_matriz(self, nombre, matriz):
        """Registra una matriz en el sistema"""
        try:
            if not isinstance(matriz, np.ndarray):
                matriz = np.array(matriz, dtype=float)
            self.matrices_disponibles[nombre] = matriz
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
    
    def extraer_terminos_formula(self, formula):
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
                inversa = False
                
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
                
                # Leer operaciones sobre la matriz (transpuesta o inversa)
                if pos < len(formula_limpia) and formula_limpia[pos] == '^':
                    pos += 1
                    if pos < len(formula_limpia):
                        if formula_limpia[pos] == 'T':
                            transpuesta = True
                            pos += 1
                        elif formula_limpia[pos] == '-' and pos + 1 < len(formula_limpia) and formula_limpia[pos + 1] == '1':
                            inversa = True
                            pos += 2
                        else:
                            return []  # Error: se esperaba T o -1 después de ^
                
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
                    'inversa': inversa,
                    'tiene_escalar_explicito': escalar_str != ""
                })
            
            return terminos
        except Exception:
            return []
    
    def validar_estructura_formula(self, formula):
        """
        Valida la estructura de una fórmula SIN USAR REGEX
        Verifica que solo contenga elementos válidos
        """
        try:
            formula_limpia = formula.replace(" ", "")
            
            if not formula_limpia:
                return False
            
            # Intentar extraer términos
            terminos = self.extraer_terminos_formula(formula)
            if not terminos:
                return False
            
            return True
        except Exception:
            return False
    
    def validar_matrices_disponibles(self, formula):
        """Valida si todas las matrices de la fórmula están disponibles"""
        try:
            terminos = self.extraer_terminos_formula(formula)
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
            terminos = self.extraer_terminos_formula(formula)
            if not terminos:
                return False
            
            # Primero, verificar que las matrices que se quieren invertir sean cuadradas
            for termino in terminos:
                if termino.get('inversa', False):
                    matriz = self.matrices_disponibles[termino['matriz']]
                    if matriz.shape[0] != matriz.shape[1]:
                        return False  # No se puede invertir una matriz no cuadrada
            
            # Calcular dimensión esperada del primer término
            primer_termino = terminos[0]
            matriz_base = self.matrices_disponibles[primer_termino['matriz']]
            
            if primer_termino.get('inversa', False):
                dimension_esperada = matriz_base.shape  # La inversa mantiene las dimensiones
            elif primer_termino['transpuesta']:
                dimension_esperada = (matriz_base.shape[1], matriz_base.shape[0])
            else:
                dimension_esperada = matriz_base.shape
            
            # Verificar que todos los términos tengan la misma dimensión
            for termino in terminos[1:]:
                matriz = self.matrices_disponibles[termino['matriz']]
                
                if termino.get('inversa', False):
                    dimension_actual = matriz.shape  # La inversa mantiene las dimensiones
                elif termino['transpuesta']:
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
            terminos = self.extraer_terminos_formula(formula)
            if not terminos:
                return False
            
            resultado = None
            
            for termino in terminos:
                # Obtener matriz original
                matriz_original = self.matrices_disponibles[termino['matriz']]
                
                # Aplicar inversa si es necesario
                if termino.get('inversa', False):
                    # Verificar que la matriz inversa sea válida
                    if not self.operaciones.matriz_inversa(matriz_original):
                        return False
                    
                    # Calcular la inversa
                    matriz_procesada = self.operaciones.calcular_inversa(matriz_original)
                    if matriz_procesada is None:
                        return False
                        
                # Aplicar transpuesta si es necesario
                elif termino['transpuesta']:
                    matriz_procesada = self.operaciones.calcular_transpuesta(matriz_original)
                else:
                    matriz_procesada = matriz_original.copy()
                
                # Aplicar multiplicación escalar si es necesario
                if termino['tiene_escalar_explicito'] or termino['escalar'] != 1.0:
                    matriz_procesada = self.operaciones.aplicar_escalar(
                        matriz_procesada, termino['escalar']
                    )
                
                # Sumar al resultado
                if resultado is None:
                    resultado = matriz_procesada.copy()
                else:
                    nueva_suma = self.operaciones.sumar_matrices(resultado, matriz_procesada)
                    if nueva_suma is None:
                        return False
                    resultado = nueva_suma
            
            return True
        except Exception:
            return False
    
    # =================== FUNCIÓN PRINCIPAL ===================
    
    def validar_formula(self, formula):
        """
        Función principal que valida completamente una fórmula
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