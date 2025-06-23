import numpy as np

def mostrar_operacion_matematica():
    """
    Muestra EXACTAMENTE cómo Python/NumPy resuelve las operaciones matemáticamente
    """
    print("=" * 60)
    print("COMO PYTHON RESUELVE LAS OPERACIONES DE MATRICES MATEMATICAMENTE")
    print("=" * 60)
    
    # Crear matrices de ejemplo
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=float)
    
    B = np.array([[9, 8, 7],
                  [6, 5, 4],
                  [3, 2, 1]], dtype=float)
    
    print("\nMatriz A:")
    print(A)
    print("\nMatriz B:")
    print(B)
    
    # 1. SUMA DE MATRICES - Algoritmo matemático
    print("\n" + "="*50)
    print("1. SUMA DE MATRICES: A + B")
    print("="*50)
    print("Algoritmo: Para cada posicion (i,j) -> resultado[i,j] = A[i,j] + B[i,j]")
    
    # Mostrar el cálculo paso a paso
    print("\nCalculo manual elemento por elemento:")
    resultado_suma_manual = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            resultado_suma_manual[i,j] = A[i,j] + B[i,j]
            print(f"Posicion [{i},{j}]: {A[i,j]} + {B[i,j]} = {resultado_suma_manual[i,j]}")
    
    # Comparar con NumPy
    resultado_suma_numpy = A + B
    print(f"\nResultado manual:\n{resultado_suma_manual}")
    print(f"\nResultado NumPy (A + B):\n{resultado_suma_numpy}")
    print(f"¿Son iguales? {np.array_equal(resultado_suma_manual, resultado_suma_numpy)}")
    
    # 2. MULTIPLICACIÓN POR ESCALAR
    print("\n" + "="*50)
    print("2. MULTIPLICACION POR ESCALAR: 2 * A")
    print("="*50)
    print("Algoritmo: Para cada posicion (i,j) -> resultado[i,j] = escalar * A[i,j]")
    
    escalar = 2
    resultado_escalar_manual = np.zeros((3, 3))
    print(f"\nCalculo manual (escalar = {escalar}):")
    for i in range(3):
        for j in range(3):
            resultado_escalar_manual[i,j] = escalar * A[i,j]
            print(f"Posicion [{i},{j}]: {escalar} * {A[i,j]} = {resultado_escalar_manual[i,j]}")
    
    resultado_escalar_numpy = escalar * A
    print(f"\nResultado manual:\n{resultado_escalar_manual}")
    print(f"\nResultado NumPy (2 * A):\n{resultado_escalar_numpy}")
    print(f"¿Son iguales? {np.array_equal(resultado_escalar_manual, resultado_escalar_numpy)}")
    
    # 3. MULTIPLICACIÓN DE MATRICES
    print("\n" + "="*50)
    print("3. MULTIPLICACION DE MATRICES: A * B")
    print("="*50)
    print("Algoritmo: resultado[i,j] = SUMA(k=0 to n-1) A[i,k] * B[k,j]")
    
    # Matriz más pequeña para mostrar el cálculo completo
    A_small = np.array([[1, 2],
                        [3, 4]], dtype=float)
    B_small = np.array([[5, 6],
                        [7, 8]], dtype=float)
    
    print(f"\nMatrices más pequeñas para mostrar el cálculo:")
    print(f"A = \n{A_small}")
    print(f"B = \n{B_small}")
    
    resultado_mult_manual = np.zeros((2, 2))
    print(f"\nCalculo manual de multiplicacion:")
    
    for i in range(2):
        for j in range(2):
            suma = 0
            calculo = []
            for k in range(2):
                producto = A_small[i,k] * B_small[k,j]
                suma += producto
                calculo.append(f"{A_small[i,k]}*{B_small[k,j]}")
            
            resultado_mult_manual[i,j] = suma
            print(f"Posicion [{i},{j}]: {' + '.join(calculo)} = {suma}")
    
    resultado_mult_numpy = np.dot(A_small, B_small)
    print(f"\nResultado manual:\n{resultado_mult_manual}")
    print(f"\nResultado NumPy (np.dot):\n{resultado_mult_numpy}")
    print(f"¿Son iguales? {np.array_equal(resultado_mult_manual, resultado_mult_numpy)}")
    
    # 4. TRANSPUESTA
    print("\n" + "="*50)
    print("4. TRANSPUESTA: A^T")
    print("="*50)
    print("Algoritmo: resultado[i,j] = A[j,i] (intercambiar filas y columnas)")
    
    resultado_trans_manual = np.zeros((3, 3))
    print(f"\nCalculo manual de transpuesta:")
    for i in range(3):
        for j in range(3):
            resultado_trans_manual[i,j] = A[j,i]  # Intercambiar índices
            print(f"Posicion [{i},{j}]: A[{j},{i}] = {A[j,i]}")
    
    resultado_trans_numpy = A.T
    print(f"\nResultado manual:\n{resultado_trans_manual}")
    print(f"\nResultado NumPy (A.T):\n{resultado_trans_numpy}")
    print(f"¿Son iguales? {np.array_equal(resultado_trans_manual, resultado_trans_numpy)}")
    
    # 5. DETERMINANTE (algoritmo complejo)
    print("\n" + "="*50)
    print("5. DETERMINANTE: det(A)")
    print("="*50)
    print("Para matriz 2x2: det = a*d - b*c")
    print("Para matriz 3x3: Usa expansión de cofactores o eliminación gaussiana")
    
    # Ejemplo con matriz 2x2
    print(f"\nEjemplo con matriz 2x2:")
    print(f"A_small = \n{A_small}")
    det_manual_2x2 = A_small[0,0]*A_small[1,1] - A_small[0,1]*A_small[1,0]
    det_numpy_2x2 = np.linalg.det(A_small)
    
    print(f"Calculo manual: {A_small[0,0]}*{A_small[1,1]} - {A_small[0,1]}*{A_small[1,0]} = {det_manual_2x2}")
    print(f"Resultado NumPy: {det_numpy_2x2}")
    print(f"¿Son iguales? {abs(det_manual_2x2 - det_numpy_2x2) < 1e-10}")
    
    print("\n" + "="*60)
    print("CONCLUSIÓN: NumPy usa algoritmos matemáticos optimizados")
    print("- BLAS (Basic Linear Algebra Subprograms)")
    print("- LAPACK (Linear Algebra Package)")
    print("- Algoritmos en C/Fortran para máximo rendimiento")
    print("="*60)

if __name__ == "__main__":
    mostrar_operacion_matematica() 