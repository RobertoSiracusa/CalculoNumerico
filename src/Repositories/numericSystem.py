class numericSystem:
    def __init__(self, number):
        self.number = str(number.strip())
        self.NumericSystem = self._processNumericSystem()

    def _processNumericSystem(self):

        num = self.getNumber()
        num = num.strip()
      
        if num == '' or num == '%z':
            return "Ninguna base válida"

      
        if len(num) == 0:
            return "Ninguna base válida"

        if num[0] == '-' or num[0] == '+':
            num_no_sign = num[1:]
        else:
            num_no_sign = num

        num_no_dot = ""
        for c in num_no_sign:
            if c != '.':
                num_no_dot += c

    
        if len(num_no_dot) == 0:
            return "Ninguna base válida"

      
        is_bin = True
        for c in num_no_dot:
            if c != '0' and c != '1':
                is_bin = False
                break

        is_dec = True
        for c in num_no_dot:
            if c < '0' or c > '9':
                is_dec = False
                break


        is_hex = True
        for c in num_no_dot:
            if not ((c >= '0' and c <= '9') or (c >= 'A' and c <= 'F') or (c >= 'a' and c <= 'f')):
                is_hex = False
                break

        result = ""
        if is_bin:
            result += "binaria"
        if is_dec:
            if result != "":
                result += ", "
            result += "decimal"
        if is_hex:
            if result != "":
                result += ", "
            result += "hexadecimal"
        if result == "":
            return "Ninguna base válida"
        return result
    
    def getNumericSystem(self):
        return self.NumericSystem
    
    def toString(self):
        return f"El numero {self.number} pertenece a los sistemas numericos: {self.NumericSystem}"
    
    def getNumber(self):
        return self.number