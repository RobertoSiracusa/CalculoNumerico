from .ErrorAbsoluto import ErrorAbsoluto


class ErrorPropagacion(ErrorAbsoluto):
    def __init__(self, initialValue = 1.0):
        self.initialValue = initialValue
        __realResult = (self.initialValue * 3)
        __errorResult = self.resultWhitError()
        super().__init__(__realResult, __errorResult)

    def resultWhitError(self):
        return ((self.initialValue * 0.1)*3 - 0.3 )
    
    def calculatePropE(self):
        return super().calculateAE()

    def showCase(self):
        print("--------------------------------------------")
        print("\n\tCaso de Propagación de Error:\n")
        print("Valor inicial: ", self.initialValue)
        print("Resultado Real: ", self._realValue)
        print("Resultado con Error: ", self._estimatedValue)
        print("\nError de propagación: ", self.calculatePropE())
        print("--------------------------------------------")