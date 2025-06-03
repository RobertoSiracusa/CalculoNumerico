from CalculoNumerico.Error import Error
from CalculoNumerico.ErrorAbsoluto import ErrorAbsoluto

obj = Error(0.5,1)
objeto = ErrorAbsoluto(obj.getRealValue(), obj.getEstimatedValue())

print(objeto.calcular())