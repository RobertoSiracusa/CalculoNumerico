from .Error import Error
class ErrorAbsoluto(Error):
    
    
    def __init__(self, _realValue, _estimatedValue):
        super().__init__( _realValue, _estimatedValue)

    def calcular(self):
        errorAb = abs(self._realValue - self._estimatedValue)
        return errorAb
    
