import numpy as np
from datetime import datetime
import re

class OperacionesElementalesMatrices:
    """
    Clase para realizar operaciones elementales con matrices usando numpy
    """
    
    def __init__(self):
        self.nombre = "Operaciones Elementales de Matrices"
        self.resultados = []
        self.matrices_disponibles = {}
    
    def agregar_resultado(self, texto):
        """Agrega un resultado a la lista para guardar en archivo"""
        self.resultados.append(texto)
    
    def registrar_matriz(self, nombre, matriz):
        """Registra una matriz en el sistema para usar en fórmulas"""
        self.matrices_disponibles[nombre] = matriz
        self.agregar_resultado(f"Matriz {nombre} registrada:\n{matriz}\n")
    
    def operacion_basica(self, matriz_a, matriz_b=None, operacion="suma", escalar=None):
        """Función modular para operaciones básicas"""
        try:
            if operacion == "suma":
                if matriz_a.shape != matriz_b.shape:
                    raise ValueError("Las matrices deben tener el mismo tamaño")
                return matriz_a + matriz_b
            elif operacion == "resta":
                if matriz_a.shape != matriz_b.shape:
                    raise ValueError("Las matrices deben tener el mismo tamaño")
                return matriz_a - matriz_b
            elif operacion == "multiplicacion_escalar":
                return matriz_a * escalar
            elif operacion == "multiplicacion_matrices":
                if matriz_a.shape[1] != matriz_b.shape[0]:
                    raise ValueError("Dimensiones incompatibles para multiplicación")
                return np.dot(matriz_a, matriz_b)
            elif operacion == "transpuesta":
                return matriz_a.T
            elif operacion == "determinante":
                if matriz_a.shape[0] != matriz_a.shape[1]:
                    raise ValueError("La matriz debe ser cuadrada")
                return np.linalg.det(matriz_a)
        except Exception as e:
            self.agregar_resultado(f"Error en {operacion}: {e}\n")
            return None
    
    def validar_formula(self, formula):
        """Valida si una fórmula cumple con las reglas establecidas"""
        formula_limpia = formula.replace(" ", "")
        
        # Patrón para términos válidos
        patron_termino_valido = r'([+-]?)(\d*\.?\d*)([A-Z])(\^T)?'
        matches = re.finditer(patron_termino_valido, formula_limpia)
        terminos_validos = [match.group() for match in matches]
        formula_reconstruida = ''.join(terminos_validos)
        
        if formula_limpia != formula_reconstruida:
            return False, "Error: La fórmula contiene elementos inválidos. Solo se permiten escalares pegados a matrices"
        
        # Verificar matrices existentes
        formula_sin_transpuestas = re.sub(r'\^T', '', formula_limpia)
        matrices_encontradas = set(re.findall(r'[A-Z]', formula_sin_transpuestas))
        
        for matriz in matrices_encontradas:
            if matriz not in self.matrices_disponibles:
                return False, f"Error: Matriz '{matriz}' no está registrada"
        
        return True, "Fórmula válida"
    
    def parsear_termino(self, signo, escalar_str, nombre_matriz, transpuesta_str, es_primer_termino):
        """Parsea un término individual y retorna información procesada"""
        # Determinar escalar
        hay_escalar_explicito = bool(escalar_str)
        escalar_base = float(escalar_str) if escalar_str else 1.0
        
        # Aplicar signo
        if es_primer_termino and signo == '':
            escalar = escalar_base
        elif signo == '-':
            escalar = -escalar_base
        else:
            escalar = escalar_base
        
        # Obtener matriz y aplicar transpuesta
        matriz = self.matrices_disponibles[nombre_matriz]
        es_transpuesta = transpuesta_str == '^T'
        if es_transpuesta:
            matriz = matriz.T
            self.agregar_resultado(f"Aplicando transpuesta a {nombre_matriz}: {nombre_matriz}^T\n")
        
        return {
            'escalar': escalar,
            'matriz': matriz,
            'nombre_matriz': nombre_matriz,
            'es_transpuesta': es_transpuesta,
            'hay_escalar_explicito': hay_escalar_explicito
        }
    
    def procesar_termino(self, info_termino, num_termino):
        """Procesa un término y genera la salida correspondiente"""
        escalar = info_termino['escalar']
        matriz = info_termino['matriz']
        nombre_matriz = info_termino['nombre_matriz']
        es_transpuesta = info_termino['es_transpuesta']
        hay_escalar_explicito = info_termino['hay_escalar_explicito']
        
        sufijo_transpuesta = '^T' if es_transpuesta else ''
        
        if hay_escalar_explicito:
            signo_mostrar = '+' if escalar >= 0 and num_termino > 1 else ''
            texto = f"Término {num_termino}: ESCALAR PEGADO: {signo_mostrar}{escalar} × {nombre_matriz}{sufijo_transpuesta} (OPERACIÓN ESCALAR APLICADA)"
            resultado = matriz * escalar
        else:
            if escalar == -1.0:
                texto = f"Término {num_termino}: MATRIZ NEGATIVA: -{nombre_matriz}{sufijo_transpuesta} (factor -1 implícito)"
                resultado = matriz * escalar
            else:
                texto = f"Término {num_termino}: MATRIZ SOLA: {nombre_matriz}{sufijo_transpuesta} (sin escalar explícito)"
                resultado = matriz
        
        self.agregar_resultado(f"{texto}\n")
        self.agregar_resultado(f"Resultado del término:\n{resultado}\n")
        return resultado
    
    def evaluar_formula(self, formula):
        """Evalúa una fórmula matemática con matrices"""
        try:
            # Validar fórmula
            es_valida, mensaje = self.validar_formula(formula)
            if not es_valida:
                self.agregar_resultado(f"FÓRMULA INVÁLIDA: {formula}\n{mensaje}\n")
                return None
            
            self.agregar_resultado(f"Evaluando fórmula: {formula}\n")
            
            # Parsear términos
            formula_limpia = formula.replace(" ", "")
            patron_termino = r'([+-]?)(\d*\.?\d*)([A-Z])(\^T)?'
            matches = re.findall(patron_termino, formula_limpia)
            
            if not matches:
                raise ValueError("No se encontraron términos válidos")
            
            # Procesar cada término
            resultado = None
            for i, (signo, escalar_str, nombre_matriz, transpuesta_str) in enumerate(matches, 1):
                info_termino = self.parsear_termino(signo, escalar_str, nombre_matriz, transpuesta_str, i == 1)
                termino_resultado = self.procesar_termino(info_termino, i)
                
                resultado = termino_resultado if resultado is None else resultado + termino_resultado
            
            self.agregar_resultado(f"RESULTADO FINAL de '{formula}':\n{resultado}\n")
            return resultado
            
        except Exception as e:
            self.agregar_resultado(f"Error al evaluar fórmula '{formula}': {e}\n")
            return None
    
    def guardar_resultados(self, nombre_archivo="resultados_matrices.txt"):
        """Guarda todos los resultados en un archivo de texto"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(f"=== RESULTADOS DE OPERACIONES ELEMENTALES DE MATRICES ===\n")
                archivo.write(f"Fecha y hora: {timestamp}\n")
                archivo.write(f"=" * 60 + "\n\n")
                
                for resultado in self.resultados:
                    archivo.write(resultado)
                    archivo.write("-" * 50 + "\n\n")
                
                archivo.write("=== FIN DE RESULTADOS ===\n")
            
            return f"Resultados guardados exitosamente en: {nombre_archivo}"
        except Exception as e:
            return f"Error al guardar archivo: {e}"
    
    def limpiar_resultados(self):
        """Limpia la lista de resultados"""
        self.resultados = []
