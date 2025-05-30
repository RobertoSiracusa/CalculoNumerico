class NumSF:
    def __init__(self, num_str):
        self.num_str = num_str
        self._numCalc = None
        self.numSistem = None
        self.numOperaciones = self._elemental_operation()
        self._detectar_y_convertir(num_str)

    def _detectar_y_convertir(self, num_str):

        if self._hex(num_str):
            self.numSistem = "hexadecimal"
            self._numCalc = int(num_str, 16)
            return

        if self._binary(num_str):
            self.numSistem = "binario"
            self._numCalc = int(num_str, 2)
            return
        
        if self._decimal(num_str):
            self.numSistem = "decimal"
            self._numCalc = int(num_str)
            return

        raise ValueError("El número proporcionado no es un número decimal (mayor a cero), binario o hexadecimal válido.")

    def _decimal(self, s):
 
        return s.isdigit() and int(s) > 0

    def _binary(self, s):
        """
        Verifica si el string contiene solo '0' y '1'.
        """
        return all(c in '01' for c in s)

    def _hex(self, s):
   #VERIFICAR REDUNDANCIA!!!!
        hasMayus = any(c.isupper() for c in s)
        hexValid = all(c.isdigit() or c in 'ABCDEFabcdef' for c in s.upper())
        return hasMayus and hexValid
 
    def cifras_significativas(self):
        """
        Cuenta las cifras significativas del número.
        Asume que el número es un entero positivo.
        """
        if self._numCalc is None:
            raise ValueError("El número no ha sido calculado correctamente.")
        
        num_str = str(self._numCalc).lstrip('0')
        if not num_str:
            return 1
        return len(num_str)
    
    def _elemental_operation(self):
        if self.numSistem == "decimal":
            return "4 Operaciones: Suma, Resta, Multiplicación, División"
        elif self.numSistem == "binario":
            return "2 Operaciones: AND, OR"
        elif self.numSistem == "hexadecimal":
            return "4 Operaciones: Suma, Resta, Multiplicación, División"
        
    def __str__(self):
        return f"Número:{self.num_str} Sistema Numérico:{self.numSistem} Cifras Significativas:{self.cifras_significativas()} Operaciones:{self.numOperaciones}"