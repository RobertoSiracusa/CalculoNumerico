from error import Error 
from errorAbsoluto import ErrorAbsoluto
from errorRedondeo import ErrorRedondeo
from errorTruncamiento import ErrorTruncamiento
from errorPropagacion import ErrorPropagacion
from errorRelativo import ErrorRelativo

obj = Error(123.456789,123.446789)
objAE = ErrorAbsoluto(obj.getRealValue(), obj.getEstimatedValue())
objRE = ErrorRelativo(obj.getRealValue(), obj.getEstimatedValue())
objRndE = ErrorRedondeo(obj.getRealValue())
objTE  = ErrorTruncamiento(0.5,3)
objPropE = ErrorPropagacion(1.0)

print("Error Absoluto: ", objAE.calculateAE())
print("Error Relativo: ", objRE.calculateRE())
print("Error Redondeo: ", objRndE.calculatRndE())
print("Error Truncamiento: ", objTE.calculateTE())
print("Error Propagacion: ", objPropE.calculatePE())