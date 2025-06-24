import numpy as np
from seidal import gauss_seidel, GaussSeidel  # Importa la función y la clase

# ===== Ejemplo usando la función de compatibilidad =====
print("===== USO DE LA FUNCIÓN DE COMPATIBILIDAD =====\n")

# Ejemplo de Uso [1]:
A_ejemplo = np.array(
        [[10.0, -1.0, 2.0, 0.0],
        [-1.0, 11.0, -1.0, 3.0],
        [2.0, -1.0, 10.0, -1.0],
        [0.0, 3.0, -1.0, 8.0]]
)
x0_ejemplo = np.array([1.0, 1.0, 1.0, 1.0], dtype=np.float64)

print("--- Ejemplo 1 (función) ---")
resultado, iteraciones = gauss_seidel(A_ejemplo, x0_ejemplo)
print(f"Vector resultado: {resultado}")
print(f"Iteraciones realizadas: {iteraciones}")

# ===== Ejemplo usando la clase GaussSeidel =====
print("\n\n===== USO DE LA CLASE GAUSSSEIDEL =====\n")

# Crear objeto GaussSeidel
print("--- Ejemplo 1 (clase) ---")
solver1 = GaussSeidel(A_ejemplo, tol=1e-10, max_iter=1000)
solucion1 = solver1.solve(x0_ejemplo)
solver1.print_summary()

# Ejemplo 2 con historial
print("\n--- Ejemplo 2 (clase con historial) ---")
A_ejemplo2 = np.array(
        [[4.0, 1.0, 2.0],
         [3.0, 5.0, 1.0],
         [1.0, 1.0, 3.0]]
)
x0_ejemplo2 = np.array([0.5, 0.5, 0.5], dtype=np.float64)

solver2 = GaussSeidel(A_ejemplo2, tol=1e-10, max_iter=25)
solucion2 = solver2.solve(x0_ejemplo2, save_history=True)

# Acceder a los resultados usando los métodos
print(f"\nSolución: {solver2.get_solution()}")
print(f"Convergió: {solver2.is_converged()}")
print(f"Iteraciones: {solver2.get_iterations()}")
print(f"Tamaño del historial: {len(solver2.get_history())}")

# Mostrar algunas iteraciones del historial
if solver2.get_history():
    print("\nPrimeras 3 iteraciones del historial:")
    for i, vec in enumerate(solver2.get_history()[:3]):
        print(f"  Iteración {i}: {vec}")

# Ejemplo 3: Sistema que podría no converger bien
print("\n--- Ejemplo 3 (tolerancia más estricta) ---")
A_ejemplo3 = np.array(
        [[2.0, -1.0, 0.0],
         [-1.0, 2.0, -1.0],
         [0.0, -1.0, 2.0]]
)
x0_ejemplo3 = np.array([0.0, 0.0, 0.0], dtype=np.float64)

solver3 = GaussSeidel(A_ejemplo3, tol=1e-12, max_iter=100)
solucion3 = solver3.solve(x0_ejemplo3)
solver3.print_summary()

# Ejemplo 4: Usando diferentes configuraciones en el mismo objeto
print("\n--- Ejemplo 4 (reutilizando objeto con diferentes vectores iniciales) ---")
solver4 = GaussSeidel(A_ejemplo, tol=1e-8, max_iter=50)

# Primera solución con un vector inicial
print("Con vector inicial [0, 0, 0, 0]:")
x0_a = np.zeros(4)
sol_a = solver4.solve(x0_a)
print(f"  Iteraciones: {solver4.get_iterations()}")
print(f"  Solución: {sol_a}")

# Segunda solución con otro vector inicial
print("\nCon vector inicial [10, 10, 10, 10]:")
x0_b = np.ones(4) * 10
sol_b = solver4.solve(x0_b)
print(f"  Iteraciones: {solver4.get_iterations()}")
print(f"  Solución: {sol_b}")

# Verificar que ambas soluciones son similares
print(f"\nDiferencia entre soluciones: {np.linalg.norm(sol_a - sol_b)}")