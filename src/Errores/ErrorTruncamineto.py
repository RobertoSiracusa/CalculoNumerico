from ErrorAbsoluto import ErrorAbsoluto


#-----------------------------------
"""Revisar formula de acropolis"""
#-----------------------------------



class ErrorTruncamiento(ErrorAbsoluto):
    """Calcula error por truncamiento de decimales"""
    def calcular(self):
        valor_truncado = int(self.valor_aproximado)
        return abs(self.valor_real - valor_truncado)