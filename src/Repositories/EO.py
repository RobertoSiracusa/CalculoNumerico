# import numpy as np  # Solo se importaría si fuera necesario

class NumericCalculator:
    def __init__(self, numberString):
        """
        Constructor que recibe un string representando un número
        Args:
            numberString (str): El número en formato string
        """
        self.numberString = numberString
        self.elementalOperation = ""
        self._determineAvailableOperations()
    
    def _determineAvailableOperations(self):
        """
        Método que determina todas las bases posibles del número y sus operaciones
        """
        # Variables string para almacenar las operaciones disponibles
        decimalOperations = ""
        binaryOperations = ""
        hexadecimalOperations = ""
        
        # Verificar si es válido para decimal
        if self._isValidDecimal():
            decimalOperations = "decimal : suma resta multiplicacion y division"
        
        # Verificar si es válido para binario
        if self._isValidBinary():
            binaryOperations = "Binario : Suma Binaria Resta Binaria Multiplicación Binaria Division Binaria"
        
        # Verificar si es válido para hexadecimal
        if self._isValidHexadecimal():
            hexadecimalOperations = "Hexadecimal : Suma Hexadecimal Resta Hexadecimal Multiplicación División Hexadecimal"
        
        # Construir el string final
        self._buildOperationString(decimalOperations, binaryOperations, hexadecimalOperations)
    
    def _isValidDecimal(self):
        """
        Verifica si el número es válido en base decimal
        Returns:
            bool: True si es válido, False en caso contrario
        """
        try:
            # Remover signos negativos para validación
            cleanNumber = self.numberString.replace('-', '')
            
            # Verificar si contiene solo dígitos decimales y punto decimal
            validChars = "0123456789."
            for char in cleanNumber:
                if char not in validChars:
                    return False
            
            # Verificar que no haya más de un punto decimal
            if cleanNumber.count('.') > 1:
                return False
            
            # Intentar convertir a float para validar formato
            float(self.numberString)
            return True
        except ValueError:
            return False
    
    def _isValidBinary(self):
        """
        Verifica si el número es válido en base binaria
        Returns:
            bool: True si es válido, False en caso contrario
        """
        try:
            # Remover signos negativos para validación
            cleanNumber = self.numberString.replace('-', '')
            
            # Verificar si contiene solo dígitos binarios y punto decimal
            validChars = "01."
            for char in cleanNumber:
                if char not in validChars:
                    return False
            
            # Verificar que no haya más de un punto decimal
            if cleanNumber.count('.') > 1:
                return False
            
            # Si tiene punto decimal, validar ambas partes
            if '.' in cleanNumber:
                # Separar manualmente sin usar split()
                dotIndex = self._findCharacterIndex(cleanNumber, '.')
                integerPart = cleanNumber[:dotIndex]
                decimalPart = cleanNumber[dotIndex + 1:]
                
                # Verificar parte entera
                if integerPart and not self._isValidBinaryInteger(integerPart):
                    return False
                # Verificar parte decimal
                if decimalPart and not self._isValidBinaryInteger(decimalPart):
                    return False
            else:
                # Verificar número entero binario
                if not self._isValidBinaryInteger(cleanNumber):
                    return False
            
            return True
        except:
            return False
    
    def _isValidBinaryInteger(self, binaryStr):
        """
        Verifica si una cadena representa un entero binario válido
        Args:
            binaryStr (str): Cadena a verificar
        Returns:
            bool: True si es válido, False en caso contrario
        """
        if not binaryStr:
            return False
        for char in binaryStr:
            if char not in "01":
                return False
        return True
    
    def _findCharacterIndex(self, text, character):
        """
        Encuentra el primer índice de un carácter en un string
        Args:
            text (str): String donde buscar
            character (str): Carácter a buscar
        Returns:
            int: Índice del carácter o -1 si no se encuentra
        """
        for i in range(len(text)):
            if text[i] == character:
                return i
        return -1
    
    def _isValidHexadecimal(self):
        """
        Verifica si el número es válido en base hexadecimal
        Returns:
            bool: True si es válido, False en caso contrario
        """
        try:
            # Remover signos negativos para validación
            cleanNumber = self.numberString.replace('-', '')
            
            # Verificar si contiene solo dígitos hexadecimales y punto decimal
            validChars = "0123456789ABCDEFabcdef."
            for char in cleanNumber:
                if char not in validChars:
                    return False
            
            # Verificar que no haya más de un punto decimal
            if cleanNumber.count('.') > 1:
                return False
            
            # Si tiene punto decimal, validar ambas partes
            if '.' in cleanNumber:
                # Separar manualmente sin usar split()
                dotIndex = self._findCharacterIndex(cleanNumber, '.')
                integerPart = cleanNumber[:dotIndex]
                decimalPart = cleanNumber[dotIndex + 1:]
                
                # Verificar parte entera
                if integerPart and not self._isValidHexInteger(integerPart):
                    return False
                # Verificar parte decimal
                if decimalPart and not self._isValidHexInteger(decimalPart):
                    return False
            else:
                # Verificar número entero hexadecimal
                if not self._isValidHexInteger(cleanNumber):
                    return False
            
            return True
        except:
            return False
    
    def _isValidHexInteger(self, hexStr):
        """
        Verifica si una cadena representa un entero hexadecimal válido
        Args:
            hexStr (str): Cadena a verificar
        Returns:
            bool: True si es válido, False en caso contrario
        """
        if not hexStr:
            return False
        validChars = "0123456789ABCDEFabcdef"
        for char in hexStr:
            if char not in validChars:
                return False
        return True
    
    def _buildOperationString(self, decimalOperations, binaryOperations, hexadecimalOperations):
        """
        Construye el string final con las operaciones disponibles
        Args:
            decimalOperations (str): String con las operaciones disponibles para decimal
            binaryOperations (str): String con las operaciones disponibles para binario
            hexadecimalOperations (str): String con las operaciones disponibles para hexadecimal
        """
        # Construir string directamente sin usar listas
        finalString = ""
        
        # Agregar operaciones en orden específico si están disponibles
        if decimalOperations:
            finalString = decimalOperations
        
        if binaryOperations:
            if finalString:
                finalString = finalString + ", " + binaryOperations
            else:
                finalString = binaryOperations
        
        if hexadecimalOperations:
            if finalString:
                finalString = finalString + ", " + hexadecimalOperations
            else:
                finalString = hexadecimalOperations
        
        # Asignar resultado final
        if finalString:
            self.elementalOperation = finalString
        else:
            self.elementalOperation = "No hay operaciones válidas disponibles para este número"
    
    def binaryAddition(self, other):
        """
        Realiza suma binaria entre dos números
        Args:
            other: Otro objeto NumericCalculator
        Returns:
            str: Resultado de la suma en binario
        """
        # Convertir ambos números a decimal primero
        decimal1 = self._binaryToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._binaryToDecimal(other.numberString.replace('-', ''))
        
        # Aplicar signos
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        # Realizar suma
        result = decimal1 + decimal2
        
        # Convertir resultado a binario
        return self._decimalToBinary(result)
    
    def binarySubtraction(self, other):
        """
        Realiza resta binaria entre dos números
        Args:
            other: Otro objeto NumericCalculator
        Returns:
            str: Resultado de la resta en binario
        """
        # Convertir ambos números a decimal primero
        decimal1 = self._binaryToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._binaryToDecimal(other.numberString.replace('-', ''))
        
        # Aplicar signos
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        # Realizar resta
        result = decimal1 - decimal2
        
        # Convertir resultado a binario
        return self._decimalToBinary(result)
    
    def binaryMultiplication(self, other):
        """
        Realiza multiplicación binaria entre dos números
        Args:
            other: Otro objeto NumericCalculator
        Returns:
            str: Resultado de la multiplicación en binario
        """
        # Convertir ambos números a decimal primero
        decimal1 = self._binaryToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._binaryToDecimal(other.numberString.replace('-', ''))
        
        # Aplicar signos
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        # Realizar multiplicación
        result = decimal1 * decimal2
        
        # Convertir resultado a binario
        return self._decimalToBinary(result)
    
    def binaryDivision(self, other):
        """
        Realiza división binaria entre dos números
        Args:
            other: Otro objeto NumericCalculator
        Returns:
            str: Resultado de la división en binario
        """
        # Convertir ambos números a decimal primero
        decimal1 = self._binaryToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._binaryToDecimal(other.numberString.replace('-', ''))
        
        # Aplicar signos
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        # Verificar división por cero
        if decimal2 == 0:
            return "Error: División por cero"
        
        # Realizar división
        result = decimal1 / decimal2
        
        # Convertir resultado a binario
        return self._decimalToBinary(result)
    
    def hexAddition(self, other):
        """
        Realiza suma hexadecimal entre dos números
        Args:
            other: Otro objeto NumericCalculator
        Returns:
            str: Resultado de la suma en hexadecimal
        """
        # Convertir ambos números a decimal primero
        decimal1 = self._hexToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._hexToDecimal(other.numberString.replace('-', ''))
        
        # Aplicar signos
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        # Realizar suma
        result = decimal1 + decimal2
        
        # Convertir resultado a hexadecimal
        return self._decimalToHex(result)
    
    def hexSubtraction(self, other):
        """
        Realiza resta hexadecimal entre dos números
        Args:
            other: Otro objeto NumericCalculator
        Returns:
            str: Resultado de la resta en hexadecimal
        """
        # Convertir ambos números a decimal primero
        decimal1 = self._hexToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._hexToDecimal(other.numberString.replace('-', ''))
        
        # Aplicar signos
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        # Realizar resta
        result = decimal1 - decimal2
        
        # Convertir resultado a hexadecimal
        return self._decimalToHex(result)
    
    def hexMultiplication(self, other):
        """
        Realiza multiplicación hexadecimal entre dos números
        Args:
            other: Otro objeto NumericCalculator
        Returns:
            str: Resultado de la multiplicación en hexadecimal
        """
        # Convertir ambos números a decimal primero
        decimal1 = self._hexToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._hexToDecimal(other.numberString.replace('-', ''))
        
        # Aplicar signos
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        # Realizar multiplicación
        result = decimal1 * decimal2
        
        # Convertir resultado a hexadecimal
        return self._decimalToHex(result)
    
    def hexDivision(self, other):
        """
        Realiza división hexadecimal entre dos números
        Args:
            other: Otro objeto NumericCalculator
        Returns:
            str: Resultado de la división en hexadecimal
        """
        # Convertir ambos números a decimal primero
        decimal1 = self._hexToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._hexToDecimal(other.numberString.replace('-', ''))
        
        # Aplicar signos
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        # Verificar división por cero
        if decimal2 == 0:
            return "Error: División por cero"
        
        # Realizar división
        result = decimal1 / decimal2
        
        # Convertir resultado a hexadecimal
        return self._decimalToHex(result)
    
    def _reverseString(self, text):
        """
        Invierte un string sin usar reversed()
        Args:
            text (str): String a invertir
        Returns:
            str: String invertido
        """
        reversedText = ""
        for i in range(len(text) - 1, -1, -1):
            reversedText += text[i]
        return reversedText
    
    def _binaryToDecimal(self, binaryStr):
        """
        Convierte un número binario a decimal
        Args:
            binaryStr (str): Número binario como string
        Returns:
            float: Número decimal
        """
        if '.' in binaryStr:
            # Manejar números con parte decimal - separar manualmente
            dotIndex = self._findCharacterIndex(binaryStr, '.')
            integerPart = binaryStr[:dotIndex]
            decimalPart = binaryStr[dotIndex + 1:]
            
            # Convertir parte entera - iterar manualmente al revés
            integerValue = 0
            reversedInteger = self._reverseString(integerPart)
            for i in range(len(reversedInteger)):
                digit = reversedInteger[i]
                integerValue += int(digit) * (2 ** i)
            
            # Convertir parte decimal - iterar normalmente
            decimalValue = 0
            for i in range(len(decimalPart)):
                digit = decimalPart[i]
                decimalValue += int(digit) * (2 ** -(i + 1))
            
            return integerValue + decimalValue
        else:
            # Número entero binario - iterar manualmente al revés
            result = 0
            reversedBinary = self._reverseString(binaryStr)
            for i in range(len(reversedBinary)):
                digit = reversedBinary[i]
                result += int(digit) * (2 ** i)
            return result
    
    def _decimalToBinary(self, decimalNum):
        """
        Convierte un número decimal a binario
        Args:
            decimalNum (float): Número decimal
        Returns:
            str: Número binario como string
        """
        if decimalNum == 0:
            return "0"
        
        # Manejar números negativos
        isNegative = decimalNum < 0
        decimalNum = abs(decimalNum)
        
        # Separar parte entera y decimal
        integerPart = int(decimalNum)
        decimalPart = decimalNum - integerPart
        
        # Convertir parte entera
        if integerPart == 0:
            integerBinary = "0"
        else:
            integerBinary = ""
            while integerPart > 0:
                integerBinary = str(integerPart % 2) + integerBinary
                integerPart //= 2
        
        # Convertir parte decimal (limitado a 10 dígitos)
        decimalBinary = ""
        if decimalPart > 0:
            decimalBinary = "."
            precision = 10
            while decimalPart > 0 and precision > 0:
                decimalPart *= 2
                bit = int(decimalPart)
                decimalBinary += str(bit)
                decimalPart -= bit
                precision -= 1
        
        result = integerBinary + decimalBinary
        return ("-" + result) if isNegative else result
    
    def _hexToDecimal(self, hexStr):
        """
        Convierte un número hexadecimal a decimal
        Args:
            hexStr (str): Número hexadecimal como string
        Returns:
            float: Número decimal
        """
        hexStr = hexStr.upper()  # Convertir a mayúsculas
        
        if '.' in hexStr:
            # Manejar números con parte decimal - separar manualmente
            dotIndex = self._findCharacterIndex(hexStr, '.')
            integerPart = hexStr[:dotIndex]
            decimalPart = hexStr[dotIndex + 1:]
            
            # Convertir parte entera - iterar manualmente al revés
            integerValue = 0
            reversedInteger = self._reverseString(integerPart)
            for i in range(len(reversedInteger)):
                digit = reversedInteger[i]
                digitValue = int(digit) if digit.isdigit() else ord(digit) - ord('A') + 10
                integerValue += digitValue * (16 ** i)
            
            # Convertir parte decimal - iterar normalmente
            decimalValue = 0
            for i in range(len(decimalPart)):
                digit = decimalPart[i]
                digitValue = int(digit) if digit.isdigit() else ord(digit) - ord('A') + 10
                decimalValue += digitValue * (16 ** -(i + 1))
            
            return integerValue + decimalValue
        else:
            # Número entero hexadecimal - iterar manualmente al revés
            result = 0
            reversedHex = self._reverseString(hexStr)
            for i in range(len(reversedHex)):
                digit = reversedHex[i]
                digitValue = int(digit) if digit.isdigit() else ord(digit) - ord('A') + 10
                result += digitValue * (16 ** i)
            return result
    
    def _getHexDigit(self, value):
        """
        Convierte un valor numérico (0-15) a su dígito hexadecimal correspondiente
        Args:
            value (int): Valor numérico entre 0 y 15
        Returns:
            str: Dígito hexadecimal correspondiente
        """
        # Para valores 0-9, convertir a carácter numérico
        if value >= 0 and value <= 9:
            return chr(ord('0') + value)
        # Para valores 10-15, convertir a letras A-F
        elif value >= 10 and value <= 15:
            return chr(ord('A') + (value - 10))
        else:
            return "0"  # Valor por defecto para casos fuera de rango
    
    def _decimalToHex(self, decimalNum):
        """
        Convierte un número decimal a hexadecimal
        Args:
            decimalNum (float): Número decimal
        Returns:
            str: Número hexadecimal como string
        """
        if decimalNum == 0:
            return "0"
        
        # Manejar números negativos
        isNegative = decimalNum < 0
        decimalNum = abs(decimalNum)
        
        # Separar parte entera y decimal
        integerPart = int(decimalNum)
        decimalPart = decimalNum - integerPart
        
        # Convertir parte entera
        if integerPart == 0:
            integerHex = "0"
        else:
            integerHex = ""
            while integerPart > 0:
                remainder = integerPart % 16
                integerHex = self._getHexDigit(remainder) + integerHex
                integerPart //= 16
        
        # Convertir parte decimal (limitado a 10 dígitos)
        decimalHex = ""
        if decimalPart > 0:
            decimalHex = "."
            precision = 10
            while decimalPart > 0 and precision > 0:
                decimalPart *= 16
                digit = int(decimalPart)
                decimalHex += self._getHexDigit(digit)
                decimalPart -= digit
                precision -= 1
        
        result = integerHex + decimalHex
        return ("-" + result) if isNegative else result
    
    def getElementalOperation(self):
        """
        Retorna el string con las operaciones elementales disponibles
        Returns:
            str: String con las operaciones disponibles
        """
        return self.elementalOperation
    
    def getPrintFormat(self):
        """
        Retorna el formato de impresión completo sin salto de línea
        que indica todas las bases posibles del número y sus operaciones disponibles
        Returns:
            str: String con formato de impresión completo
        """
        return f"Número: {self.numberString} - Operaciones disponibles: {self.elementalOperation}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear objeto con número que funciona en múltiples bases
    calc1 = NumericCalculator("111")
    print(f"Número: {calc1.numberString}")
    print(f"Operaciones disponibles: {calc1.getElementalOperation()}")
    
    print("\n" + "="*50 + "\n")
    
    # Crear objeto con número binario
    calc2 = NumericCalculator("101.01")
    print(f"Número: {calc2.numberString}")
    print(f"Operaciones disponibles: {calc2.getElementalOperation()}")
    
    print("\n" + "="*50 + "\n")
    
    # Crear objeto con número hexadecimal
    calc3 = NumericCalculator("A1F.2C")
    print(f"Número: {calc3.numberString}")
    print(f"Operaciones disponibles: {calc3.getElementalOperation()}")
    
    print("\n" + "="*50 + "\n")
    
    # Ejemplo de operaciones binarias
    binCalc1 = NumericCalculator("1010")
    binCalc2 = NumericCalculator("0110")
    
    if binCalc1._isValidBinary() and binCalc2._isValidBinary():
        print("Operaciones binarias:")
        print(f"{binCalc1.numberString} + {binCalc2.numberString} = {binCalc1.binaryAddition(binCalc2)}")
        print(f"{binCalc1.numberString} - {binCalc2.numberString} = {binCalc1.binarySubtraction(binCalc2)}")
        print(f"{binCalc1.numberString} * {binCalc2.numberString} = {binCalc1.binaryMultiplication(binCalc2)}")
        print(f"{binCalc1.numberString} / {binCalc2.numberString} = {binCalc1.binaryDivision(binCalc2)}")
    
    print("\n" + "="*50 + "\n")
    
    # Ejemplo de operaciones hexadecimales
    hexCalc1 = NumericCalculator("A")
    hexCalc2 = NumericCalculator("5")
    
    if hexCalc1._isValidHexadecimal() and hexCalc2._isValidHexadecimal():
        print("Operaciones hexadecimales:")
        print(f"{hexCalc1.numberString} + {hexCalc2.numberString} = {hexCalc1.hexAddition(hexCalc2)}")
        print(f"{hexCalc1.numberString} - {hexCalc2.numberString} = {hexCalc1.hexSubtraction(hexCalc2)}")
        print(f"{hexCalc1.numberString} * {hexCalc2.numberString} = {hexCalc1.hexMultiplication(hexCalc2)}")
        print(f"{hexCalc1.numberString} / {hexCalc2.numberString} = {hexCalc1.hexDivision(hexCalc2)}")
    
    print("\n" + "="*50 + "\n")
    
    # Ejemplo del nuevo método getPrintFormat()
    print("Ejemplos usando el método getPrintFormat():")
    testCalc1 = NumericCalculator("111")
    testCalc2 = NumericCalculator("1001.11")
    testCalc3 = NumericCalculator("ABC.5F")
    
    print(testCalc1.getPrintFormat())
    print(testCalc2.getPrintFormat())
    print(testCalc3.getPrintFormat())