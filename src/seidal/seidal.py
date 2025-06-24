import numpy as np

class GaussSeidel:
    """
    Clase para realizar iteraciones de tipo Gauss-Seidel sobre un sistema de ecuaciones lineales.
    """
    
    def __init__(self, A, tol=1e-10, max_iter=1000):
        """
        Inicializa el objeto GaussSeidel.
        
        Args:
            A (np.ndarray): La matriz de coeficientes (n x n).
            tol (float): La tolerancia absoluta para la convergencia.
            max_iter (int): El número máximo de iteraciones.
        """
        self.A = np.array(A, dtype=np.float64)
        self.tol = tol
        self.max_iter = max_iter
        self.n = self.A.shape[0]
        
        # Resultados
        self.solution = None
        self.iterations = 0
        self.converged = False
        self.history = []
        
        # Validar matriz
        self._validate_matrix()
    
    def _validate_matrix(self):
        """Valida que la matriz sea cuadrada y no tenga ceros en la diagonal."""
        if self.A.shape[0] != self.A.shape[1]:
            raise ValueError("La matriz A debe ser cuadrada.")
        
        for i in range(self.n):
            if self.A[i, i] == 0:
                raise ValueError(f"El elemento diagonal A[{i},{i}] es cero. La iteración podría no converger.")
    
    def solve(self, x0, save_history=False):
        """
        Ejecuta el método de Gauss-Seidel.
        
        Args:
            x0 (np.ndarray): El vector inicial para las iteraciones (n,).
            save_history (bool): Si True, guarda el historial de iteraciones.
            
        Returns:
            np.ndarray: El vector solución.
        """
        # Reiniciar resultados
        self.history = []
        self.iterations = 0
        self.converged = False
        
        # Copiar y asegurar tipo de datos
        x = np.array(x0, dtype=np.float64)
        
        if x.shape[0] != self.n:
            raise ValueError(f"El vector inicial debe tener tamaño {self.n}")
        
        print("Vector inicial:", x)
        
        if save_history:
            self.history.append(x.copy())
        
        for it_count in range(1, self.max_iter + 1):
            x_new = np.copy(x)
            
            for i in range(self.n):
                # Suma los términos que involucran los valores de x_new ya actualizados (j < i)
                s1 = np.dot(self.A[i, :i], x_new[:i])
                # Suma los términos que involucran los valores de x de la iteración previa (j > i)
                s2 = np.dot(self.A[i, i + 1:], x[i + 1:])
                
                # Actualiza el elemento actual
                x_new[i] = (-s1 - s2) / self.A[i, i]
            
            if save_history:
                self.history.append(x_new.copy())
            
            # Comprueba la convergencia
            if np.allclose(x, x_new, rtol=self.tol):
                print(f"Convergido en {it_count} iteraciones.")
                self.iterations = it_count
                self.converged = True
                self.solution = x_new
                return self.solution
            
            # Actualiza x para la siguiente iteración
            x = np.copy(x_new)
        
        print(f"No convergió dentro de {self.max_iter} iteraciones.")
        self.iterations = self.max_iter
        self.converged = False
        self.solution = x
        return self.solution
    
    def get_solution(self):
        """Retorna la solución calculada."""
        if self.solution is None:
            raise RuntimeError("Debe ejecutar solve() primero.")
        return self.solution
    
    def get_iterations(self):
        """Retorna el número de iteraciones realizadas."""
        return self.iterations
    
    def is_converged(self):
        """Retorna True si el método convergió."""
        return self.converged
    
    def get_history(self):
        """Retorna el historial de iteraciones si fue guardado."""
        return self.history
    
    def print_summary(self):
        """Imprime un resumen de los resultados."""
        if self.solution is None:
            print("No se ha ejecutado el método aún.")
            return
        
        print("\n=== Resumen de Gauss-Seidel ===")
        print(f"Convergió: {'Sí' if self.converged else 'No'}")
        print(f"Iteraciones: {self.iterations}")
        print(f"Tolerancia: {self.tol}")
        print(f"Vector solución: {self.solution}")
        if self.history:
            print(f"Historial guardado: {len(self.history)} vectores")


# Función de compatibilidad con el código anterior
def gauss_seidel(A, x0, tol=1e-10, max_iter=1000):
    """
    Función de compatibilidad que usa la clase GaussSeidel internamente.
    
    Args:
        A (np.ndarray): La matriz de coeficientes (n x n).
        x0 (np.ndarray): El vector inicial para las iteraciones (n,).
        tol (float): La tolerancia absoluta para la convergencia.
        max_iter (int): El número máximo de iteraciones.
        
    Returns:
        np.ndarray: El vector resultado después de las iteraciones.
        int: El número de iteraciones realizadas.
    """
    solver = GaussSeidel(A, tol, max_iter)
    solution = solver.solve(x0)
    return solution, solver.get_iterations()