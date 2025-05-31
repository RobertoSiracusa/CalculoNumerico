from ErrorAbsoluto import ErrorAbsoluto

class ErrorRelativo(ErrorAbsoluto):
    """Calcula el error relativo porcentual"""
    def __init__(self, valor_real, valor_aproximado):
        self._requiere_division = True  # Activa validación de división
        super().__init__(valor_real, valor_aproximado)
    
    def calcular(self):
        error_absoluto = super().calcular()
        return (error_absoluto / self.valor_real) * 100