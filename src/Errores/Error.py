class Error:
    """Clase base abstracta para todos los tipos de error"""
    def __init__(self, valor_real, valor_aproximado):
        self._validar_datos(valor_real, valor_aproximado)
        self.valor_real = valor_real
        self.valor_aproximado = valor_aproximado
    
    def _validar_datos(self, real, aproximado):
        """Validaciones base que aplican a todos los errores"""
        if not isinstance(real, (int, float)) or not isinstance(aproximado, (int, float)):
            raise TypeError("Ambos valores deben ser numéricos")
        if real == 0 and hasattr(self, '_requiere_division'):
            raise ValueError("El valor real no puede ser cero para este tipo de error")
    
    def calcular(self):
        """Método abstracto que debe implementarse en clases hijas"""
        raise NotImplementedError("Debe implementarse en subclases")
    
    def es_valido(self):
        """Verifica si los datos son válidos"""
        try:
            self._validar_datos(self.valor_real, self.valor_aproximado)
            return True
        except (TypeError, ValueError):
            return False