import numpy as np
from EO import OperacionesElementalesMatrices

# Crear sistema y registrar matrices
sistema = OperacionesElementalesMatrices()
sistema.registrarMatriz('A', np.array([[1, 2], [3, 4]]))
sistema.registrarMatriz('B', np.array([[5, 6], [7, 8]]))
sistema.registrarMatriz('C', np.array([[1, 0], [0, 1]]))

# Guardar resultados usando archiveUtil
archivoGenerado = sistema.guardarResultadosTxt("formulas_ejemplo.txt")

if archivoGenerado:
    print(f"✅ Archivo generado: {archivoGenerado}")
else:
    print("❌ Error al generar archivo") 