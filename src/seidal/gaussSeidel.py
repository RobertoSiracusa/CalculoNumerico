import numpy as np

class GaussSeidel:
    def __init__(self, A, tol=1e-10, maxIter=1000):
        self.A = np.array(A, dtype=np.float64)
        self.tol = tol
        self.maxIter = maxIter
        self.n = self.A.shape[0]
        
        self.solution = None
        self.iterations = 0
        self.converged = False
        self.history = []
        
        self._validateMatrix()
    
    def _validateMatrix(self):
        if self.A.shape[0] != self.A.shape[1]:
            raise ValueError("La matriz A debe ser cuadrada.")
        
        for i in range(self.n):
            if self.A[i, i] == 0:
                raise ValueError(f"El elemento diagonal A[{i},{i}] es cero. La iteración podría no converger.")
    
    def solve(self, x0, saveHistory=False):
        self.history = []
        self.iterations = 0
        self.converged = False
        
        x = np.array(x0, dtype=np.float64)
        
        if x.shape[0] != self.n:
            raise ValueError(f"El vector inicial debe tener tamaño {self.n}")
        
        print("Vector inicial:", x)
        
        if saveHistory:
            self.history.append(x.copy())
        
        for iterationCount in range(1, self.maxIter + 1):
            xNew = np.copy(x)
            
            for i in range(self.n):
                sum1 = np.dot(self.A[i, :i], xNew[:i])
                sum2 = np.dot(self.A[i, i + 1:], x[i + 1:])
                xNew[i] = (-sum1 - sum2) / self.A[i, i]
            
            if saveHistory:
                self.history.append(xNew.copy())
            
            if np.allclose(x, xNew, rtol=self.tol):
                print(f"Convergido en {iterationCount} iteraciones.")
                self.iterations = iterationCount
                self.converged = True
                self.solution = xNew
                return self.solution
            
            x = np.copy(xNew)
        
        print(f"No convergió dentro de {self.maxIter} iteraciones.")
        self.iterations = self.maxIter
        self.converged = False
        self.solution = x
        return self.solution
    
    def getSolution(self):
        if self.solution is None:
            raise RuntimeError("Debe ejecutar solve() primero.")
        return self.solution
    
    def getIterations(self):
        return self.iterations
    
    def isConverged(self):
        return self.converged
    
    def getHistory(self):
        return self.history
    
    def printSummary(self):
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

def gaussSeidel(A, x0, tol=1e-10, maxIter=1000):
    solver = GaussSeidel(A, tol, maxIter)
    solution = solver.solve(x0)
    return solution, solver.getIterations()

def gauss_Seidel(A, x0, tol=1e-10, maxIter=1000):
    return gaussSeidel(A, x0, tol, maxIter)