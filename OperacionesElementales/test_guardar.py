import numpy as np
from EO import OperacionesElementalesMatrices

# Crear sistema y registrar matrices
sistema = OperacionesElementalesMatrices()
sistema.registrar_matriz('A', np.array([[1, 2], [3, 4]]))
sistema.registrar_matriz('B', np.array([[5, 6], [7, 8]]))
sistema.registrar_matriz('C', np.array([[1, 0], [0, 1]]))

# Guardar resultados usando archiveUtil
archivo_generado = sistema.guardar_resultados_txt("formulas_ejemplo.txt")

if archivo_generado:
    print(f"✅ Archivo generado: {archivo_generado}")
else:
    print("❌ Error al generar archivo") 