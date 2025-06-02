from .Error import Error
from .ErrorAbsoluto import ErrorAbsoluto

class ErrorRedondeo(ErrorAbsoluto):
    def __init__(self, _realValue,decimals = 3):
        _realValue = self.validateDigitBeforeUse(_realValue)
        self.decimals = decimals
        self._roundedValue = self.calculateRndValue(_realValue)
        super().__init__(_realValue, self._roundedValue)

    def calculateRndValue(self,_realValue):
        _roundedValue = round(_realValue, self.decimals)
        return _roundedValue
    
    def calculateRndE(self):
        return super().calculateAE()
    
    def validateDigitBeforeUse(self, _realValue):
        beforeDigitUse = Error(_realValue, 0)
        validRealValue = beforeDigitUse.getRealValue()
        return validRealValue
    
    def showCase(self):
        print("--------------------------------------------")
        print("\n\tCaso de Redondeo:\n")
        print("Valor real: ", self._realValue)
        print("Valor redondeado: ", self._roundedValue)
        print("\nError de redondeo: ", self.calculateRndE())
        print("--------------------------------------------")