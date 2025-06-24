import numpy as np
from datetime import datetime
import sys
import os

# Agregar ruta para importar archiveUtil
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Repositories'))
from Repositories.archiveUtil import ArchiveUtil

# Importar los módulos modularizados
from OperacionesMatrices import OperacionesMatrices
from ValidadorFormulas import ValidadorFormulas

class OperacionesElementalesMatrices:
    """
    Clase principal que integra operaciones matriciales y validación de fórmulas
    Actúa como una fachada (facade) para los módulos especializados
    """
    
    def __init__(self):
        self.nombre = "Operaciones Elementales de Matrices"
        self.operaciones = OperacionesMatrices()
        self.validador = ValidadorFormulas()
        # Referencia directa para compatibilidad
        self.matricesDisponibles = self.validador.matricesDisponibles
    
    def registrarMatriz(self, nombre, matriz):
        """Registra una matriz en el sistema"""
        return self.validador.registrarMatriz(nombre, matriz)
    
    # =================== OPERACIONES ELEMENTALES (DELEGADAS) ===================
    
    def sumaMatrices(self, matrizA, matrizB):
        """Suma dos matrices elemento por elemento"""
        return self.operaciones.sumaMatrices(matrizA, matrizB)
    
    def restaMatrices(self, matrizA, matrizB):
        """Resta dos matrices elemento por elemento"""
        return self.operaciones.restaMatrices(matrizA, matrizB)
    
    def multiplicacionEscalar(self, matriz, escalar):
        """Multiplica cada elemento de la matriz por el escalar"""
        return self.operaciones.multiplicacionEscalar(matriz, escalar)
    
    def multiplicacionMatrices(self, matrizA, matrizB):
        """Multiplica dos matrices usando el algoritmo elemental"""
        return self.operaciones.multiplicacionMatrices(matrizA, matrizB)
    
    def transpuesta(self, matriz):
        """Calcula la transpuesta intercambiando filas y columnas"""
        return self.operaciones.transpuesta(matriz)
    
    def matrizInversa(self, matriz):
        """Calcula la matriz inversa usando el método de Gauss-Jordan"""
        return self.operaciones.matrizInversa(matriz)
    
    # =================== ANÁLISIS DE FÓRMULAS (DELEGADAS) ===================
    
    def esDigito(self, caracter):
        """Verifica si un caracter es dígito"""
        return self.validador.esDigito(caracter)
    
    def esLetraMayuscula(self, caracter):
        """Verifica si un caracter es letra mayúscula"""
        return self.validador.esLetraMayuscula(caracter)
    
    def extraerNumeroDecimal(self, texto, inicio):
        """Extrae un número decimal desde la posición inicio"""
        return self.validador.extraerNumeroDecimal(texto, inicio)
    
    def extraerTerminosFormulaManual(self, formula):
        """Extrae términos de una fórmula SIN USAR REGEX"""
        return self.validador.extraerTerminosFormula(formula)
    
    def validarEstructuraFormulaManual(self, formula):
        """Valida la estructura de una fórmula SIN USAR REGEX"""
        return self.validador.validarEstructuraFormula(formula)
    
    def validarMatricesDisponibles(self, formula):
        """Valida si todas las matrices de la fórmula están disponibles"""
        return self.validador.validarMatricesDisponibles(formula)
    
    def validarDimensionesCompatibles(self, formula):
        """Valida si las dimensiones de las matrices son compatibles"""
        return self.validador.validarDimensionesCompatibles(formula)
    
    def evaluarFormulaInterna(self, formula):
        """Evalúa una fórmula internamente usando operaciones elementales"""
        return self.validador.evaluarFormulaInterna(formula)
    
    # =================== FUNCIÓN PRINCIPAL ===================
    
    def validarFormula(self, formula):
        """Función principal que valida completamente una fórmula"""
        return self.validador.validarFormula(formula)
    
    # =================== FUNCIONES DE COMPATIBILIDAD ===================
    
    def extraerTerminosFormula(self, formula):
        """Función de compatibilidad que usa el nuevo método manual"""
        return self.extraerTerminosFormulaManual(formula)
    
    def validarEstructuraFormula(self, formula):
        """Función de compatibilidad que usa el nuevo método manual"""
        return self.validarEstructuraFormulaManual(formula)
    
    # =================== UTILIDADES ===================
    
    def obtenerInfoSistema(self):
        """Retorna información básica del sistema"""
        return self.validador.obtenerInfoSistema()
    
    def limpiarMatrices(self):
        """Limpia todas las matrices registradas"""
        return self.validador.limpiarMatrices()
    
    def guardarResultadosTxt(self, formulasArchivo):
        """
        Guarda resultados de validación en txt usando setCreateArchive
        Lee fórmulas de un archivo y escribe: fórmula, válida o no
        """
        try:
            # Leer fórmulas del archivo
            archiveUtil = ArchiveUtil(".")
            formulas = []
            
            with archiveUtil.getArchive(formulasArchivo) as archivo:
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
                resultado = self.validarFormula(formula)
                validez = "VÁLIDA" if resultado else "NO VÁLIDA"
                
                contenido += f"Fórmula: {formula}\n"
                contenido += f"Resultado: {validez}\n"
                contenido += "-" * 30 + "\n"
            
            # Guardar usando setCreateArchive
            nombreArchivo = f"resultados_validacion_{timestamp}"
            archiveUtil.setCreateArchive(contenido, nombreArchivo, append_newline=False, booleano=True)
            
            return f"{nombreArchivo}.txt"
            
        except Exception as e:
            return None 