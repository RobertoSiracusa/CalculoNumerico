import numpy as np

class GaussJordan:
    def __init__(self, augmentedMatrix: np.ndarray):
        if not isinstance(augmentedMatrix, np.ndarray):
            raise TypeError("El parámetro 'augmentedMatrix' debe ser un array de NumPy (np.ndarray).")
        
        if augmentedMatrix.ndim != 2:
            raise ValueError("La matriz aumentada debe ser bidimensional (e.g., forma (filas, columnas)).")
        
        if augmentedMatrix.size == 0 or augmentedMatrix.shape[0] == 0:
            raise ValueError("La matriz aumentada no debe estar vacía (debe tener al menos una fila).")
        
        if augmentedMatrix.shape[1] < 2:
            raise ValueError("La matriz aumentada debe tener al menos 2 columnas (matriz de coeficientes A y vector de términos independientes b).")

        # 5. Asignar la matriz y asegurar que los elementos sean flotantes
        self.augmentedMatrix = augmentedMatrix.astype(float)
        self.nRows, self.nCols = self.augmentedMatrix.shape

        # Advertencias sobre el tamaño del sistema
        if self.nRows > self.nCols - 1:
            print("Advertencia: El sistema puede estar sobredeterminado o no tener solución única.")
        elif self.nRows < self.nCols - 1:
            print("Advertencia: El sistema puede tener infinitas soluciones o ser indeterminado.")

        np.set_printoptions(precision=4, suppress=False)

    def swapRows(self, matrix: np.ndarray, row1: int, row2: int):
        matrix[[row1, row2]] = matrix[[row2, row1]]

    def swapColumns(self, matrix: np.ndarray, col1: int, col2: int):
        matrix[:, [col1, col2]] = matrix[:, [col2, col1]]

    def partialPivoting(self, matrix: np.ndarray, k: int) -> np.ndarray:
        n = matrix.shape[0]
        maxIndex = k + np.argmax(np.abs(matrix[k:, k]))

        if maxIndex != k:
            self.swapRows(matrix, k, maxIndex)
            print(f"   > Partial Pivoting: Swapped rows {k} and {maxIndex}")
        return matrix

    def completePivoting(self, matrix: np.ndarray, k: int) -> tuple[np.ndarray, list]:
        n, m = matrix.shape
        submatrix = np.abs(matrix[k:n, k:m-1])

        if submatrix.size == 0: 
            return matrix, []
        
        maxFlatIndex = np.argmax(submatrix)
        rowIndexOffset, colIndexOffset = np.unravel_index(maxFlatIndex, submatrix.shape)

        pivotRow = k + rowIndexOffset
        pivotCol = k + colIndexOffset

        swappedColumns = []

        if pivotRow != k:
            self.swapRows(matrix, k, pivotRow)
            print(f"   > Full Pivoting: Swapped rows {k} and {pivotRow}")

        if pivotCol != k:
            self.swapColumns(matrix, k, pivotCol)
            swappedColumns.append((k, pivotCol))
            print(f"   > Full Pivoting: Swapped columns {k} and {pivotCol}")

        return matrix, swappedColumns

    def scaledPivoting(self, augmentedMatrix: np.ndarray, k: int) -> np.ndarray:
        """
        Realiza el pivoteo escalonado para la columna k.
        Encuentra la fila con el cociente más grande (elemento en columna k / factor de escala de la fila).
        """
        n, m = augmentedMatrix.shape
        scaleFactors = np.zeros(n)

        for i in range(n):
            if augmentedMatrix[i, :m-1].size > 0:
                scaleFactors[i] = np.max(np.abs(augmentedMatrix[i, :m-1]))
            else:
                scaleFactors[i] = 0.0 

        maxRatio = -1.0
        rowWithMaxRatio = k

        for i in range(k, n):
            if scaleFactors[i] == 0:
                ratio = 0.0
            else:
                ratio = np.abs(augmentedMatrix[i, k]) / scaleFactors[i]

            if ratio > maxRatio:
                maxRatio = ratio
                rowWithMaxRatio = i
        if rowWithMaxRatio != k:
            self.swapRows(augmentedMatrix, k, rowWithMaxRatio)
            print(f"   > Scaled Pivoting: Swapped rows {k} and {rowWithMaxRatio}")
        return augmentedMatrix

    def solve(self, pivotingType: str = "partial") -> np.ndarray | None:
        """
        Implementa el método de Gauss-Jordan para resolver un sistema de ecuaciones lineales.

        Args:
            pivotingType (str): Tipo de pivoteo a aplicar:
                                - "partial": Pivoteo parcial (por defecto).
                                - "full": Pivoteo completo.
                                - "scaled": Pivoteo escalonado.
                                - "none": No se aplica ningún pivoteo.

        Returns:
            np.array: La matriz en forma escalonada reducida por filas (si es posible),
                      o None si se encuentra un pivote cero inmanejable.
        """
        currentMatrix = self.augmentedMatrix.copy() 
        originalColumnOrder = list(range(self.nCols - 1)) if pivotingType == "full" else None

        print(f"\n--- Starting Gauss-Jordan with {pivotingType.capitalize()} Pivoting ---")
        print("Initial Matrix:\n", currentMatrix)

        for k in range(self.nRows):
            print(f"\n--- Iteration {k+1} (Pivot at [{k},{k}]) ---")

            if pivotingType == "partial":
                currentMatrix = self.partialPivoting(currentMatrix, k)
            elif pivotingType == "full": 
                currentMatrix, swaps = self.completePivoting(currentMatrix, k)
                if originalColumnOrder is not None: 
                    for col1Idx, col2Idx in swaps:
                        originalColumnOrder[col1Idx], originalColumnOrder[col2Idx] = \
                            originalColumnOrder[col2Idx], originalColumnOrder[col1Idx]
            elif pivotingType == "scaled":
                currentMatrix = self.scaledPivoting(currentMatrix, k)
            elif pivotingType != "none":
                print(f"Warning: Pivoting type '{pivotingType}' not recognized. No pivoting will be applied.")

            pivot = currentMatrix[k, k]

            if abs(pivot) < 1e-9: 
                print(f"Error! Zero or near-zero pivot at row {k} after pivoting. The system might not have a unique solution or be inconsistent.")
                return None

            currentMatrix[k, :] = currentMatrix[k, :] / pivot
            print(f"   > Row {k} divided by pivot ({pivot:.4f}):\n", currentMatrix)

            for i in range(self.nRows):
                if i != k: # For all other rows
                    factor = currentMatrix[i, k]
                    currentMatrix[i, :] = currentMatrix[i, :] - factor * currentMatrix[k, :]
                    print(f"   > Row {i} - {factor:.4f} * Row {k}:\n", currentMatrix)

        print("\n--- Gauss-Jordan Process Finished ---")
        print("Matrix in Reduced Row Echelon Form (result):\n", currentMatrix)

        if pivotingType == "full" and originalColumnOrder is not None: 
            unorderedSolution = currentMatrix[:, -1]
            solution = np.zeros_like(unorderedSolution)
            for i, originalIdx in enumerate(originalColumnOrder):
                solution[originalIdx] = unorderedSolution[i]
            print("\nSolution (adjusted for column swaps):\n", solution)
        else:
            solution = currentMatrix[:, -1]
            print("\nSolution (final independent term vector):\n", solution)

        return currentMatrix 

#---------------- EJEMPLO DE USO ----------------

def main():
    print("\n========== EXAMPLE 1: Partial Pivoting (Standard Case) ==========")
    A1 = np.array([
        [55.8, 20.4, 17.1, 18.5, 19.2, 2500],
        [7.8, 52.1, 12.3, 13.9, 18.5, 2000],
        [16.4, 11.5, 46.1, 11.5, 21.3, 2500],
        [11.7, 9.2, 14.1, 47.0, 10.4, 2000],
        [8.3, 6.8, 10.4, 9.1, 30.6, 1000]
    ], dtype=float)
    
    solver1 = GaussJordan(A1.copy()) 
    solver1.solve(pivotingType="partial") 

    print("\n========== EXAMPLE 2: Partial Pivoting (Avoiding Zero on Diagonal) ==========")
    solver2 = GaussJordan(A1.copy())
    solver2.solve(pivotingType="partial")

    print("\n========== EXAMPLE 3: Full Pivoting ==========")
    solver3 = GaussJordan(A1.copy())
    solver3.solve(pivotingType="full") 

    print("\n========== EXAMPLE 4: Scaled Pivoting ==========")
    solver4 = GaussJordan(A1.copy())
    solver4.solve(pivotingType="scaled")

    print("\n========== EXAMPLE 5: No Pivoting (Can Fail) ==========")
    solver5 = GaussJordan(A1.copy())
    solver5.solve(pivotingType="none") 

    print("\n========== EXAMPLE 6: Error Handling Demo ==========")
    try:
        # This will raise a TypeError
        GaussJordan([[1,2,3],[4,5,6]]).solve() 
    except TypeError as e:
        print(f"Caught expected error: {e}")
    
    try:
    
        GaussJordan(np.array([1,2,3])).solve()
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:

        A_singular_problem = np.array([
            [1., 1., 2.],
            [2., 2., 4.], 
            [3., 4., 5.]
        ], dtype=float)
        solver_singular = GaussJordan(A_singular_problem)
        solver_singular.solve(pivotingType="none")
    except Exception as e: 
        print(f"Caught unexpected error during singular matrix solve: {e}")

if __name__ == "__main__":
    main()