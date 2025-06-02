from .Error import Error

class ErrorAbsoluto(Error):
    
    def __init__(self, _realValue, _estimatedValue):
        super().__init__( _realValue, _estimatedValue)

    def calculateAE(self):
        absoluteError = abs(self._realValue - self._estimatedValue)
        return absoluteError
    
    def showCase(self):
        print("\n--------------------------------------------")
        print("\n\tCaso de Error Absoluto:\n")
        print("Valor real: ", self._realValue)
        print("Valor estimado: ", self._estimatedValue)
        print("\nError absoluto: ", self.calculateAE())
        print("--------------------------------------------")