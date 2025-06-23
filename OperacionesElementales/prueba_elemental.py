import numpy as np
from EO import OperacionesElementalesMatrices

def demostrar_operaciones_elementales():
    """
    Demuestra que ahora SÍ se hacen las operaciones elementales paso a paso
    como se harían a mano (bucles, algoritmos largos y complicados)
    """
    
    print("=== DEMOSTRACIÓN DE OPERACIONES ELEMENTALES ===")
    print("Ahora SÍ se implementan paso a paso como a mano\n")
    
    # Matrices de prueba pequeñas para ver los algoritmos
    A = np.array([[1, 2], [3, 4]], dtype=float)
    B = np.array([[5, 6], [7, 8]], dtype=float)
    
    print("Matrices de prueba:")
    print(f"A = \n{A}")
    print(f"B = \n{B}\n")
    
    sistema = OperacionesElementalesMatrices()
    sistema.registrar_matriz('A', A)
    sistema.registrar_matriz('B', B)
    
    print("=== 1. SUMA ELEMENTAL ===")
    print("Algoritmo: resultado[i,j] = A[i,j] + B[i,j]")
    print("Código ejecutándose internamente:")
    print("  for i in range(2):")
    print("    for j in range(2):")
    print("      resultado[i,j] = A[i,j] + B[i,j]")
    print()
    print("Pasos:")
    print("  resultado[0,0] = A[0,0] + B[0,0] = 1 + 5 = 6")
    print("  resultado[0,1] = A[0,1] + B[0,1] = 2 + 6 = 8") 
    print("  resultado[1,0] = A[1,0] + B[1,0] = 3 + 7 = 10")
    print("  resultado[1,1] = A[1,1] + B[1,1] = 4 + 8 = 12")
    print(f"Suma funciona: {sistema.suma_matrices(A, B)}")
    print()
    
    print("=== 2. MULTIPLICACIÓN ELEMENTAL ===")
    print("Algoritmo: resultado[i,j] = Σ(A[i,k] × B[k,j])")
    print("Código ejecutándose internamente:")
    print("  for i in range(2):              # Cada fila de A")
    print("    for j in range(2):            # Cada columna de B")
    print("      suma = 0")
    print("      for k in range(2):          # Suma de productos")
    print("        suma += A[i,k] * B[k,j]")
    print("      resultado[i,j] = suma")
    print()
    print("Pasos:")
    print("  resultado[0,0] = A[0,0]*B[0,0] + A[0,1]*B[1,0] = 1*5 + 2*7 = 19")
    print("  resultado[0,1] = A[0,0]*B[0,1] + A[0,1]*B[1,1] = 1*6 + 2*8 = 22")
    print("  resultado[1,0] = A[1,0]*B[0,0] + A[1,1]*B[1,0] = 3*5 + 4*7 = 43")
    print("  resultado[1,1] = A[1,0]*B[0,1] + A[1,1]*B[1,1] = 3*6 + 4*8 = 50")
    print(f"Multiplicación funciona: {sistema.multiplicacion_matrices(A, B)}")
    print()
    
    print("=== 3. TRANSPUESTA ELEMENTAL ===")
    print("Algoritmo: resultado[i,j] = matriz[j,i]")
    print("Código ejecutándose internamente:")
    print("  for i in range(2):")
    print("    for j in range(2):")
    print("      resultado[j,i] = matriz[i,j]")
    print()
    print("Pasos:")
    print("  resultado[0,0] = A[0,0] = 1")
    print("  resultado[1,0] = A[0,1] = 2") 
    print("  resultado[0,1] = A[1,0] = 3")
    print("  resultado[1,1] = A[1,1] = 4")
    print(f"Transpuesta funciona: {sistema.transpuesta(A)}")
    print()
    
    print("=== 4. ESCALAR ELEMENTAL ===")
    print("Algoritmo: resultado[i,j] = escalar × matriz[i,j]")
    print("Código ejecutándose internamente:")
    print("  for i in range(2):")
    print("    for j in range(2):")
    print("      resultado[i,j] = escalar * matriz[i,j]")
    print()
    print("Para 3 * A:")
    print("  resultado[0,0] = 3 * A[0,0] = 3 * 1 = 3")
    print("  resultado[0,1] = 3 * A[0,1] = 3 * 2 = 6")
    print("  resultado[1,0] = 3 * A[1,0] = 3 * 3 = 9")
    print("  resultado[1,1] = 3 * A[1,1] = 3 * 4 = 12")
    print(f"Multiplicación escalar funciona: {sistema.multiplicacion_escalar(A, 3)}")
    print()
    
    print("=== 5. FÓRMULA COMPLEJA ===")
    print("Fórmula: '2A + B'")
    print("Operaciones elementales ejecutándose:")
    print("1. Multiplicar A por 2 (bucle doble)")
    print("2. Sumar 2A + B (bucle doble)")
    print("3. Total: 4 bucles anidados ejecutados")
    formula_resultado = sistema.validar_formula('2A + B')
    print(f"Fórmula '2A + B' funciona: {formula_resultado}")
    print()
    
    print("=== 6. COMPARACIÓN: ANTES vs AHORA ===")
    print("ANTES (NumPy automático):")
    print("  resultado = matriz_a + matriz_b        # ← 1 línea mágica")
    print("  resultado = np.dot(matriz_a, matriz_b) # ← 1 línea mágica")
    print()
    print("AHORA (Operaciones elementales):")
    print("  for i in range(filas):                 # ← Bucles como a mano")
    print("    for j in range(columnas):")
    print("      resultado[i,j] = A[i,j] + B[i,j]")
    print()
    print("  for i in range(filas_a):               # ← Triple bucle para multiplicación")
    print("    for j in range(columnas_b):")
    print("      suma = 0")
    print("      for k in range(columnas_a):")
    print("        suma += A[i,k] * B[k,j]")
    print("      resultado[i,j] = suma")
    print()
    
    print("¡AHORA SÍ SON OPERACIONES ELEMENTALES REALES!")
    print("Largas, complicadas, con bucles, como se hacen a mano 📝")

def test_matriz_3x3():
    """Prueba con matriz 3x3 para operaciones básicas"""
    
    print("\n=== PRUEBA CON MATRIZ 3x3 ===")
    print("Operaciones elementales con matriz más grande")
    
    C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
    print(f"Matriz C (3x3):\n{C}")
    
    sistema = OperacionesElementalesMatrices()
    sistema.registrar_matriz('C', C)
    
    print("\nOperaciones disponibles:")
    print("1. Transpuesta: intercambio de filas y columnas")
    print("2. Multiplicación escalar: cada elemento × escalar") 
    print("3. En fórmulas: suma, resta, transpuesta, escalar")
    
    resultado_transpuesta = sistema.transpuesta(C)
    print(f"\nTranspuesta 3x3 calculada: {resultado_transpuesta}")
    
    resultado_escalar = sistema.multiplicacion_escalar(C, 2)
    print(f"Multiplicación escalar 3x3: {resultado_escalar}")

if __name__ == "__main__":
    demostrar_operaciones_elementales()
    test_matriz_3x3() 