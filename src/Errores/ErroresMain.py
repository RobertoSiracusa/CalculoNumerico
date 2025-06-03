from Errores.Error import Error 
from Errores.ErrorAbsoluto import ErrorAbsoluto
from Errores.ErrorRedondeo import ErrorRedondeo
from Errores.ErrorTruncamiento import ErrorTruncamiento
from Errores.ErrorPropagacion import ErrorPropagacion
from Errores.ErrorRelativo import ErrorRelativo

obj = Error(123.456789,123.446789)
objAE = ErrorAbsoluto(obj.getRealValue(), obj.getEstimatedValue())
objRE = ErrorRelativo(obj.getRealValue(), obj.getEstimatedValue())
objRndE = ErrorRedondeo(obj.getRealValue(), 3)
objTE  = ErrorTruncamiento(0.5,3)
objPropE = ErrorPropagacion(1.0)

objAE.showCase()
objRE.showCase()
objRndE.showCase()
objTE.showCase()
objPropE.showCase()