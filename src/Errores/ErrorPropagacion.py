from ErrorAbsoluto import ErrorAbsoluto



#-----------------------------------
"""Revisar formula de acropolis"""
#-----------------------------------



class ErrorPropagacion(ErrorAbsoluto):
    """Calcula error por propagación en operaciones"""
    def calcular(self, operacion=lambda x, y: x + y):
        resultado_real = operacion(self.valor_real, self.valor_real)
        resultado_aprox = operacion(self.valor_aproximado, self.valor_aproximado)
        return abs(resultado_real - resultado_aprox)