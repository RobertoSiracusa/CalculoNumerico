import numpy as np
from archiveUtil import ArchiveUtil

class GaussJordan:
    def __init__(self, augmentedMatrix: np.ndarray):  
        if not isinstance(augmentedMatrix, np.ndarray):
            errorMsg = "El parámetro 'augmentedMatrix' debe ser un array de NumPy (np.ndarray)."
            ArchiveUtil.logError("TypeError", errorMsg, "")
            raise TypeError(errorMsg)
        
        if augmentedMatrix.ndim != 2:
            errorMsg = "La matriz aumentada debe ser bidimensional (Ejemplo: forma (filas, columnas))."
            ArchiveUtil.logError("ValueError", errorMsg, "")
            raise ValueError(errorMsg)
        
        if augmentedMatrix.size == 0 or augmentedMatrix.shape[0] == 0:
            errorMsg = "La matriz aumentada no debe estar vacía (debe tener al menos una fila)."
            ArchiveUtil.logError("ValueError", errorMsg, "")
            raise ValueError(errorMsg)
        
        if augmentedMatrix.shape[1] < 2:
            errorMsg = "La matriz aumentada debe tener al menos 2 columnas (matriz de coeficientes A y vector de términos independientes b)."
            ArchiveUtil.logError("ValueError", errorMsg, "")
            raise ValueError(errorMsg)


        self.augmentedMatrix = augmentedMatrix.astype(float)
        self.nRows, self.nCols = self.augmentedMatrix.shape
        self.x = None
        self.y = None
        self.z = None
        self.solution_strings_dict = {} 
        self.raw_solution_values = None 
        self.resolveMatrix()

        # Advertencias sobre el tamaño del sistema
        if self.nRows > self.nCols - 1:
            errorMsg = "El sistema puede estar sobredeterminado o no tener solución única."
            ArchiveUtil.logError("Tamaño del Sistema", errorMsg, "")
            print(errorMsg)
        if self.nRows < self.nCols - 1:
            errorMsg = "El sistema puede tener infinitas soluciones o ser indeterminado."
            ArchiveUtil.logError("Infinitas Soluciones", errorMsg, "")
            print(errorMsg)

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

        if pivotCol != k:
            self.swapColumns(matrix, k, pivotCol)
            swappedColumns.append((k, pivotCol))
        return matrix, swappedColumns

    def scaledPivoting(self, augmentedMatrix: np.ndarray, k: int) -> np.ndarray:
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
        return augmentedMatrix

    def resolveMatrix(self, pivotingType: str = "parcial") -> np.ndarray | None:
        """
        Implementa el método de Gauss-Jordan para resolver un sistema de ecuaciones lineales.

        Args:
            pivotingType (str): Tipo de pivoteo a aplicar:
                                - "parcial": Pivoteo parcial (por defecto).
                                - "completo": Pivoteo completo.
                                - "escalonado": Pivoteo escalonado.
                                - "none": No se aplica ningún pivoteo.

        Returns:
            np.array: La matriz en forma escalonada reducida por filas (si es posible),
                      o None si se encuentra un pivote cero inmanejable.
        """
        pathToFile = "src/Storage"
        archive = ArchiveUtil(pathToFile)
        outputFileName = "GaussJordan"

        currentMatrix = self.augmentedMatrix
        
        # Reiniciar los atributos de solución para una nueva ejecución
        self.x_solution = "No resuelto"
        self.y_solution = "No resuelto"
        self.z_solution = "No resuelto"
        self.solution_strings_dict = {} 
        self.raw_solution_values = None

        # Usamos np.arange en lugar de list(range())
        originalColumnOrder = np.arange(self.nCols - 1) if pivotingType == "full" else None

        text = (f"\n--- Comenzando Gauss-Jordan con Pivoeteo {pivotingType.capitalize()} ---")
        archive.setCreateArchive(text, outputFileName, append_newline=True)

        # Asegúrate de que ArchiveUtil.setCreateArchive pueda manejar directamente un numpy array convertido a string
        text_matrix = (f"Matriz Inicial:\n{currentMatrix}") 
        archive.setCreateArchive(text_matrix, outputFileName, append_newline=True)

        for k in range(self.nRows):
            if pivotingType == "parcial":
                currentMatrix = self.partialPivoting(currentMatrix, k)
            elif pivotingType == "completo": 
                currentMatrix, swaps = self.completePivoting(currentMatrix, k)
                if originalColumnOrder is not None: 
                    for col1Idx, col2Idx in swaps:
                        originalColumnOrder[[col1Idx, col2Idx]] = originalColumnOrder[[col2Idx, col1Idx]]
            elif pivotingType == "escalonado":
                currentMatrix = self.scaledPivoting(currentMatrix, k)
            elif pivotingType != "none":
                errorMsg = "Tipo de pivoteo '{pivotingType}' no reconocido. No se aplicara el pivoteo"
                ArchiveUtil.logError("ValueError", errorMsg, "")
                raise ValueError(errorMsg)
                
            pivot = currentMatrix[k, k]

            if abs(pivot) < 1e-9: 
                errorMsg = "Error: Pivote igual a cero o casi cero en la fila {k} después del pivoteo. El sistema podría no tener una solución única o ser inconsistente."
                ArchiveUtil.logError("ValueError", errorMsg, "")
                raise ValueError(errorMsg)
            
            currentMatrix[k, :] = currentMatrix[k, :] / pivot

            for i in range(self.nRows):
                if i != k:
                    factor = currentMatrix[i, k]
                    currentMatrix[i, :] = currentMatrix[i, :] - factor * currentMatrix[k, :]

        text = ("\n--- Proceso de Gauss-Jordan finalizado ---")
        archive.setCreateArchive(text, outputFileName, append_newline=True)

        text_matrix_final = (f"Matrix in Reduced Row Echelon Form (result):\n{currentMatrix}")
        archive.setCreateArchive(text_matrix_final, outputFileName, append_newline=True)

        solution_values = None 

        if pivotingType == "completo" and originalColumnOrder is not None: 
            unorderedSolution = currentMatrix[:, -1]
            solution_values = np.zeros_like(unorderedSolution)
            for i, originalIdx in enumerate(originalColumnOrder):
                solution_values[originalIdx] = unorderedSolution[i]
        else:
            solution_values = currentMatrix[:, -1]
        
        self.raw_solution_values = solution_values

        if len(solution_values) >= 3:
            self.x = f"x = {solution_values[0]:.6f}"
            self.y = f"y = {solution_values[1]:.6f}"
            self.z = f"z = {solution_values[2]:.6f}"
            
            self.solution_strings_dict['x'] = self.x
            self.solution_strings_dict['y'] = self.y
            self.solution_strings_dict['z'] = self.z

            final_solution_for_txt = (
                f"\Solucion:\n"
                f"{self.x}, "
                f"{self.y}, "
                f"{self.z}"
            )
        else:
            self.x = "No aplicable (menos de 3 vars)"
            self.y = "No aplicable (menos de 3 vars)"
            self.z = "No aplicable (menos de 3 vars)"
            self.solution_strings_dict.clear()
            final_solution_for_txt = "\nSolución: No hay suficientes variables (se esperaban 3 para x, y, z)"

        archive.setCreateArchive(final_solution_for_txt, outputFileName, append_newline=True)
        
        return currentMatrix
#---------------- EJEMPLO DE USO ----------------

def main():
    print("\n========== EXAMPLE 1: Partial Pivoting (Standard Case) ==========")
    A1 = np.array([
        [55.8, 20.4, 17.1,2.0,3.0],
        [7.8, 52.1, 12.3,1.0,2.0],
        [16.4, 11.5, 46.1,0.0,10.0],
        [26.4, 12.5, 6.1,2.0,0.0]
    ], dtype=float)
    
    solver1 = GaussJordan(A1.copy()) 
    solver1.resolveMatrix(pivotingType="parcial") 

    print("\n========== EXAMPLE 2: Partial Pivoting (Avoiding Zero on Diagonal) ==========")
    solver2 = GaussJordan(A1.copy())
    solver2.resolveMatrix(pivotingType="parcial")

    print("\n========== EXAMPLE 3: Full Pivoting ==========")
    solver3 = GaussJordan(A1.copy())
    solver3.resolveMatrix(pivotingType="completo") 

    print("\n========== EXAMPLE 4: Scaled Pivoting ==========")
    solver4 = GaussJordan(A1.copy())
    solver4.resolveMatrix(pivotingType="escalonado")

    print("\n========== EXAMPLE 5: No Pivoting (Can Fail) ==========")
    solver5 = GaussJordan(A1.copy())
    solver5.resolveMatrix(pivotingType="none") 

    print("\n========== EXAMPLE 6: Error Handling Demo ==========")
    try:
        # This will raise a TypeError
        GaussJordan([[1,2,3],[4,5,6]]).resolveMatrix() 
    except TypeError as e:
        print(f"Caught expected error: {e}")
    
    try:
    
        GaussJordan(np.array([1,2,3])).resolveMatrix()
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:

        A_singular_problem = np.array([
            [1., 1., 2.],
            [2., 2., 4.], 
            [3., 4., 5.]
        ], dtype=float)
        solver_singular = GaussJordan(A_singular_problem)
        solver_singular.resolveMatrix(pivotingType="none")
    except Exception as e: 
        print(f"Caught unexpected error during singular matrix solve: {e}")

if __name__ == "__main__":
    main()