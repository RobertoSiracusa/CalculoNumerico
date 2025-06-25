import numpy as np
from gaussSeidel import gaussSeidel, GaussSeidel

print("===== USO DE LA FUNCIÓN DE COMPATIBILIDAD =====\n")

exampleA = np.array(
        [[10.0, -1.0, 2.0, 0.0],
        [-1.0, 11.0, -1.0, 3.0],
        [2.0, -1.0, 10.0, -1.0],
        [0.0, 3.0, -1.0, 8.0]]
)
x0Example = np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float64)

print("--- Ejemplo 1 (función) ---")
result, iterations = gaussSeidel(exampleA, x0Example)
print(f"Vector resultado: {result}")
print(f"Iteraciones realizadas: {iterations}")

print("\n\n===== USO DE LA CLASE GAUSSSEIDEL =====\n")

print("--- Ejemplo 1 (clase) ---")
solver1 = GaussSeidel(exampleA, tol=1e-10, maxIter=1000)
solution1 = solver1.solve(x0Example)
solver1.printSummary()

print("\n--- Ejemplo 2 (clase con historial) ---")
exampleA2 = np.array(
        [[4.0, 1.0, 2.0],
         [3.0, 5.0, 1.0],
         [1.0, 1.0, 3.0]]
)
x0Example2 = np.array([0.5, 0.5, 0.5], dtype=np.float64)

solver2 = GaussSeidel(exampleA2, tol=1e-10, maxIter=25)
solution2 = solver2.solve(x0Example2, saveHistory=True)

print(f"\nSolución: {solver2.getSolution()}")
print(f"Convergió: {solver2.isConverged()}")
print(f"Iteraciones: {solver2.getIterations()}")
print(f"Tamaño del historial: {len(solver2.getHistory())}")

if solver2.getHistory():
    print("\nPrimeras 3 iteraciones del historial:")
    for i, vec in enumerate(solver2.getHistory()[:3]):
        print(f"  Iteración {i}: {vec}")

print("\n--- Ejemplo 3 (tolerancia más estricta) ---")
exampleA3 = np.array(
        [[2.0, -1.0, 0.0],
         [-1.0, 2.0, -1.0],
         [0.0, -1.0, 2.0]]
)
x0Example3 = np.array([0.0, 0.0, 0.0], dtype=np.float64)

solver3 = GaussSeidel(exampleA3, tol=1e-12, maxIter=100)
solution3 = solver3.solve(x0Example3)
solver3.printSummary()

print("\n--- Ejemplo 4 (reutilizando objeto con diferentes vectores iniciales) ---")
solver4 = GaussSeidel(exampleA, tol=1e-8, maxIter=50)

print("Con vector inicial [0, 0, 0, 0]:")
x0A = np.zeros(4)
solA = solver4.solve(x0A)
print(f"  Iteraciones: {solver4.getIterations()}")
print(f"  Solución: {solA}")

print("\nCon vector inicial [10, 10, 10, 10]:")
x0B = np.ones(4) * 10
solB = solver4.solve(x0B)
print(f"  Iteraciones: {solver4.getIterations()}")
print(f"  Solución: {solB}")

print(f"\nDiferencia entre soluciones: {np.linalg.norm(solA - solB)}")