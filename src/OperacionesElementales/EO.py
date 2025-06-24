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
        self.matrices_disponibles = self.validador.matrices_disponibles
    
    def registrar_matriz(self, nombre, matriz):
        """Registra una matriz en el sistema"""
        return self.validador.registrar_matriz(nombre, matriz)
    
    # =================== OPERACIONES ELEMENTALES (DELEGADAS) ===================
    
    def suma_matrices(self, matriz_a, matriz_b):
        """Suma dos matrices elemento por elemento"""
        return self.operaciones.suma_matrices(matriz_a, matriz_b)
    
    def resta_matrices(self, matriz_a, matriz_b):
        """Resta dos matrices elemento por elemento"""
        return self.operaciones.resta_matrices(matriz_a, matriz_b)
    
    def multiplicacion_escalar(self, matriz, escalar):
        """Multiplica cada elemento de la matriz por el escalar"""
        return self.operaciones.multiplicacion_escalar(matriz, escalar)
    
    def multiplicacion_matrices(self, matriz_a, matriz_b):
        """Multiplica dos matrices usando el algoritmo elemental"""
        return self.operaciones.multiplicacion_matrices(matriz_a, matriz_b)
    
    def transpuesta(self, matriz):
        """Calcula la transpuesta intercambiando filas y columnas"""
        return self.operaciones.transpuesta(matriz)
    
    def matriz_inversa(self, matriz):
        """Calcula la matriz inversa usando el método de Gauss-Jordan"""
        return self.operaciones.matriz_inversa(matriz)
    
    # =================== ANÁLISIS DE FÓRMULAS (DELEGADAS) ===================
    
    def es_digito(self, caracter):
        """Verifica si un caracter es dígito"""
        return self.validador.es_digito(caracter)
    
    def es_letra_mayuscula(self, caracter):
        """Verifica si un caracter es letra mayúscula"""
        return self.validador.es_letra_mayuscula(caracter)
    
    def extraer_numero_decimal(self, texto, inicio):
        """Extrae un número decimal desde la posición inicio"""
        return self.validador.extraer_numero_decimal(texto, inicio)
    
    def extraer_terminos_formula_manual(self, formula):
        """Extrae términos de una fórmula SIN USAR REGEX"""
        return self.validador.extraer_terminos_formula(formula)
    
    def validar_estructura_formula_manual(self, formula):
        """Valida la estructura de una fórmula SIN USAR REGEX"""
        return self.validador.validar_estructura_formula(formula)
    
    def validar_matrices_disponibles(self, formula):
        """Valida si todas las matrices de la fórmula están disponibles"""
        return self.validador.validar_matrices_disponibles(formula)
    
    def validar_dimensiones_compatibles(self, formula):
        """Valida si las dimensiones de las matrices son compatibles"""
        return self.validador.validar_dimensiones_compatibles(formula)
    
    def evaluar_formula_interna(self, formula):
        """Evalúa una fórmula internamente usando operaciones elementales"""
        return self.validador.evaluar_formula_interna(formula)
    
    # =================== FUNCIÓN PRINCIPAL ===================
    
    def validar_formula(self, formula):
        """Función principal que valida completamente una fórmula"""
        return self.validador.validar_formula(formula)
    
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
        return self.validador.obtener_info_sistema()
    
    def limpiar_matrices(self):
        """Limpia todas las matrices registradas"""
        return self.validador.limpiar_matrices()
    
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