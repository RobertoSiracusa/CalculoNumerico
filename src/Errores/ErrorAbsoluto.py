from Error import Error

class ErrorAbsoluto(Error):
    """Calcula la diferencia absoluta entre valores"""
    def calcular(self):
        return abs(self.valor_real - self.valor_aproximado)