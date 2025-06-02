from .ErrorAbsoluto import ErrorAbsoluto
from math import factorial, cos

class ErrorTruncamiento(ErrorAbsoluto):
   
    def __init__(self,valueToAprox=0.5,nTerms=3):
        _realValue = cos(valueToAprox)
        _truncatedValue = self.aproximateFunction(valueToAprox, nTerms)
        super().__init__(_realValue, _truncatedValue)

    def calculateTE(self):
        return super().calculateAE()

    def aproximateFunction(self,valueToAprox,nTerms):
        suma = 0
        for i in range(nTerms):
            suma +=(-1)**i * (valueToAprox**(2*i)) / factorial(2*i)
        return suma
    
    def showCase(self):
        print("\n--------------------------------------------")
        print("\n\tCaso de Truncamiento:\n")
        print("Valor real: ", self._realValue)
        print("Valor truncado: ", self._estimatedValue)
        print("\nError de truncamiento: ", self.calculateTE())
        print("--------------------------------------------")