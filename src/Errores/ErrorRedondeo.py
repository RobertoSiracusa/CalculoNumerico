from error import Error
from errorAbsoluto import ErrorAbsoluto

class ErrorRedondeo(ErrorAbsoluto):
    def __init__(self, _realValue):
        _realValue = self.__validateDigitBeforeUse(_realValue)
        self._roundedValue = self.__calculateRndValue(_realValue)
        super().__init__(_realValue, self._roundedValue)

    def __calculateRndValue(self,_realValue):
        _roundedValue = round(_realValue, 3)
        return _roundedValue
    
    def calculateRndE(self):
        return super().calculateAE()
    
    def __validateDigitBeforeUse(self, _realValue):
        beforeDigitUse = Error(_realValue, 0)
        validRealValue = beforeDigitUse.getRealValue()
        return validRealValue