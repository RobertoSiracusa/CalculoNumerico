import numpy as np
from seidal import gaussSeidel, GaussSeidel  # Importa la función y la clase

# ===== Ejemplo usando la función de compatibilidad =====
print("===== USO DE LA FUNCIÓN DE COMPATIBILIDAD =====\n")

# Ejemplo de Uso [1]:
aEjemplo = np.array(
        [[10.0, -1.0, 2.0, 0.0],
        [-1.0, 11.0, -1.0, 3.0],
        [2.0, -1.0, 10.0, -1.0],
        [0.0, 3.0, -1.0, 8.0]]
)
x0Ejemplo = np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float64)

print("--- Ejemplo 1 (función) ---")
resultado, iteraciones = gaussSeidel(aEjemplo, x0Ejemplo)
print(f"Vector resultado: {resultado}")
print(f"Iteraciones realizadas: {iteraciones}")

# ===== Ejemplo usando la clase GaussSeidel =====
print("\n\n===== USO DE LA CLASE GAUSSSEIDEL =====\n")

# Crear objeto GaussSeidel
print("--- Ejemplo 1 (clase) ---")
solver1 = GaussSeidel(aEjemplo, tol=1e-10, maxIter=1000)
solucion1 = solver1.solve(x0Ejemplo)
solver1.printSummary()

# Ejemplo 2 con historial
print("\n--- Ejemplo 2 (clase con historial) ---")
aEjemplo2 = np.array(
        [[4.0, 1.0, 2.0],
         [3.0, 5.0, 1.0],
         [1.0, 1.0, 3.0]]
)
x0Ejemplo2 = np.array([0.5, 0.5, 0.5], dtype=np.float64)

solver2 = GaussSeidel(aEjemplo2, tol=1e-10, maxIter=25)
solucion2 = solver2.solve(x0Ejemplo2, saveHistory=True)

# Acceder a los resultados usando los métodos
print(f"\nSolución: {solver2.getSolution()}")
print(f"Convergió: {solver2.isConverged()}")
print(f"Iteraciones: {solver2.getIterations()}")
print(f"Tamaño del historial: {len(solver2.getHistory())}")

# Mostrar algunas iteraciones del historial
if solver2.getHistory():
    print("\nPrimeras 3 iteraciones del historial:")
    for i, vec in enumerate(solver2.getHistory()[:3]):
        print(f"  Iteración {i}: {vec}")

# Ejemplo 3: Sistema que podría no converger bien
print("\n--- Ejemplo 3 (tolerancia más estricta) ---")
aEjemplo3 = np.array(
        [[2.0, -1.0, 0.0],
         [-1.0, 2.0, -1.0],
         [0.0, -1.0, 2.0]]
)
x0Ejemplo3 = np.array([0.0, 0.0, 0.0], dtype=np.float64)

solver3 = GaussSeidel(aEjemplo3, tol=1e-12, maxIter=100)
solucion3 = solver3.solve(x0Ejemplo3)
solver3.printSummary()

# Ejemplo 4: Usando diferentes configuraciones en el mismo objeto
print("\n--- Ejemplo 4 (reutilizando objeto con diferentes vectores iniciales) ---")
solver4 = GaussSeidel(aEjemplo, tol=1e-8, maxIter=50)

# Primera solución con un vector inicial
print("Con vector inicial [0, 0, 0, 0]:")
x0A = np.zeros(4)
solA = solver4.solve(x0A)
print(f"  Iteraciones: {solver4.getIterations()}")
print(f"  Solución: {solA}")

# Segunda solución con otro vector inicial
print("\nCon vector inicial [10, 10, 10, 10]:")
x0B = np.ones(4) * 10
solB = solver4.solve(x0B)
print(f"  Iteraciones: {solver4.getIterations()}")
print(f"  Solución: {solB}")

# Verificar que ambas soluciones son similares
print(f"\nDiferencia entre soluciones: {np.linalg.norm(solA - solB)}")