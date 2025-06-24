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
        self.matricesDisponibles = {}
        self.operaciones = OperacionesMatrices()
    
    def registrarMatriz(self, nombre, matriz):
        """Registra una matriz en el sistema"""
        try:
            if not isinstance(matriz, np.ndarray):
                matriz = np.array(matriz, dtype=float)
            self.matricesDisponibles[nombre] = matriz
            return True
        except Exception:
            return False
    
    # =================== ANÁLISIS DE FÓRMULAS SIN REGEX ===================
    
    def esDigito(self, caracter):
        """Verifica si un caracter es dígito"""
        return caracter in '0123456789'
    
    def esLetraMayuscula(self, caracter):
        """Verifica si un caracter es letra mayúscula"""
        return caracter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def extraerNumeroDecimal(self, texto, inicio):
        """
        Extrae un número decimal desde la posición inicio
        Retorna (numero_como_string, nueva_posicion)
        """
        pos = inicio
        numeroStr = ""
        puntoEncontrado = False
        
        # Extraer dígitos y punto decimal
        while pos < len(texto):
            char = texto[pos]
            if self.esDigito(char):
                numeroStr += char
                pos += 1
            elif char == '.' and not puntoEncontrado:
                numeroStr += char
                puntoEncontrado = True
                pos += 1
            else:
                break
        
        return numeroStr, pos
    
    def extraerTerminosFormula(self, formula):
        """
        Extrae términos de una fórmula SIN USAR REGEX
        Procesa manualmente caracter por caracter
        """
        try:
            formulaLimpia = formula.replace(" ", "")
            terminos = []
            pos = 0
            
            while pos < len(formulaLimpia):
                # Inicializar término
                signo = "+"
                escalarStr = ""
                nombreMatriz = ""
                transpuesta = False
                inversa = False
                
                # Leer signo
                if pos < len(formulaLimpia) and formulaLimpia[pos] in "+-":
                    signo = formulaLimpia[pos]
                    pos += 1
                elif len(terminos) == 0:
                    # Primer término sin signo explícito
                    signo = "+"
                
                # Leer escalar (número decimal)
                escalarStr, pos = self.extraerNumeroDecimal(formulaLimpia, pos)
                
                # Leer nombre de matriz (una letra mayúscula)
                if pos < len(formulaLimpia) and self.esLetraMayuscula(formulaLimpia[pos]):
                    nombreMatriz = formulaLimpia[pos]
                    pos += 1
                else:
                    return []  # Error: se esperaba una matriz
                
                # Leer operaciones sobre la matriz (transpuesta o inversa)
                if pos < len(formulaLimpia) and formulaLimpia[pos] == '^':
                    pos += 1
                    if pos < len(formulaLimpia):
                        if formulaLimpia[pos] == 'T':
                            transpuesta = True
                            pos += 1
                        elif formulaLimpia[pos] == '-' and pos + 1 < len(formulaLimpia) and formulaLimpia[pos + 1] == '1':
                            inversa = True
                            pos += 2
                        else:
                            return []  # Error: se esperaba T o -1 después de ^
                
                # Procesar escalar
                if escalarStr == "":
                    escalarValor = 1.0
                else:
                    try:
                        escalarValor = float(escalarStr)
                    except ValueError:
                        return []  # Error: escalar inválido
                
                # Aplicar signo
                if signo == "-":
                    escalarValor = -escalarValor
                
                # Agregar término
                terminos.append({
                    'escalar': escalarValor,
                    'matriz': nombreMatriz,
                    'transpuesta': transpuesta,
                    'inversa': inversa,
                    'tieneEscalarExplicito': escalarStr != ""
                })
            
            return terminos
        except Exception:
            return []
    
    def validarEstructuraFormula(self, formula):
        """
        Valida la estructura de una fórmula SIN USAR REGEX
        Verifica que solo contenga elementos válidos
        """
        try:
            formulaLimpia = formula.replace(" ", "")
            
            if not formulaLimpia:
                return False
            
            # Intentar extraer términos
            terminos = self.extraerTerminosFormula(formula)
            if not terminos:
                return False
            
            return True
        except Exception:
            return False
    
    def validarMatricesDisponibles(self, formula):
        """Valida si todas las matrices de la fórmula están disponibles"""
        try:
            terminos = self.extraerTerminosFormula(formula)
            if not terminos:
                return False
            
            for termino in terminos:
                if termino['matriz'] not in self.matricesDisponibles:
                    return False
            
            return True
        except Exception:
            return False
    
    def validarDimensionesCompatibles(self, formula):
        """Valida si las dimensiones de las matrices son compatibles"""
        try:
            terminos = self.extraerTerminosFormula(formula)
            if not terminos:
                return False
            
            # Primero, verificar que las matrices que se quieren invertir sean cuadradas
            for termino in terminos:
                if termino.get('inversa', False):
                    matriz = self.matricesDisponibles[termino['matriz']]
                    if matriz.shape[0] != matriz.shape[1]:
                        return False  # No se puede invertir una matriz no cuadrada
            
            # Calcular dimensión esperada del primer término
            primerTermino = terminos[0]
            matrizBase = self.matricesDisponibles[primerTermino['matriz']]
            
            if primerTermino.get('inversa', False):
                dimensionEsperada = matrizBase.shape  # La inversa mantiene las dimensiones
            elif primerTermino['transpuesta']:
                dimensionEsperada = (matrizBase.shape[1], matrizBase.shape[0])
            else:
                dimensionEsperada = matrizBase.shape
            
            # Verificar que todos los términos tengan la misma dimensión
            for termino in terminos[1:]:
                matriz = self.matricesDisponibles[termino['matriz']]
                
                if termino.get('inversa', False):
                    dimensionActual = matriz.shape  # La inversa mantiene las dimensiones
                elif termino['transpuesta']:
                    dimensionActual = (matriz.shape[1], matriz.shape[0])
                else:
                    dimensionActual = matriz.shape
                
                if dimensionActual != dimensionEsperada:
                    return False
            
            return True
        except Exception:
            return False
    
    def evaluarFormulaInterna(self, formula):
        """
        Evalúa una fórmula internamente usando operaciones elementales
        """
        try:
            terminos = self.extraerTerminosFormula(formula)
            if not terminos:
                return False
            
            resultado = None
            
            for termino in terminos:
                # Obtener matriz original
                matrizOriginal = self.matricesDisponibles[termino['matriz']]
                
                # Aplicar inversa si es necesario
                if termino.get('inversa', False):
                    # Verificar que la matriz inversa sea válida
                    if not self.operaciones.matrizInversa(matrizOriginal):
                        return False
                    
                    # Calcular la inversa
                    matrizProcesada = self.operaciones.calcularInversa(matrizOriginal)
                    if matrizProcesada is None:
                        return False
                        
                # Aplicar transpuesta si es necesario
                elif termino['transpuesta']:
                    matrizProcesada = self.operaciones.calcularTranspuesta(matrizOriginal)
                else:
                    matrizProcesada = matrizOriginal.copy()
                
                # Aplicar multiplicación escalar si es necesario
                if termino['tieneEscalarExplicito'] or termino['escalar'] != 1.0:
                    matrizProcesada = self.operaciones.aplicarEscalar(
                        matrizProcesada, termino['escalar']
                    )
                
                # Sumar al resultado
                if resultado is None:
                    resultado = matrizProcesada.copy()
                else:
                    nuevaSuma = self.operaciones.sumarMatrices(resultado, matrizProcesada)
                    if nuevaSuma is None:
                        return False
                    resultado = nuevaSuma
            
            return True
        except Exception:
            return False
    
    # =================== FUNCIÓN PRINCIPAL ===================
    
    def validarFormula(self, formula):
        """
        Función principal que valida completamente una fórmula
        """
        try:
            # 1. Validar estructura
            if not self.validarEstructuraFormula(formula):
                return False
            
            # 2. Validar matrices disponibles
            if not self.validarMatricesDisponibles(formula):
                return False
            
            # 3. Validar dimensiones compatibles
            if not self.validarDimensionesCompatibles(formula):
                return False
            
            # 4. Intentar evaluar la fórmula usando operaciones elementales
            if not self.evaluarFormulaInterna(formula):
                return False
            
            return True
        except Exception:
            return False
    
    # =================== UTILIDADES ===================
    
    def obtenerInfoSistema(self):
        """Retorna información básica del sistema"""
        return {
            'matricesRegistradas': len(self.matricesDisponibles),
            'nombresMatrices': list(self.matricesDisponibles.keys())
        }
    
    def limpiarMatrices(self):
        """Limpia todas las matrices registradas"""
        self.matricesDisponibles.clear()
        return True 