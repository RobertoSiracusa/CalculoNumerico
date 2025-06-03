
class elementalOperation:
    def __init__(self, numberString):
        self.numberString = numberString
        self.elementalOperation = ""
        self._determineAvailableOperations()
    
    def _determineAvailableOperations(self):
        decimalOperations = ""
        binaryOperations = ""
        hexadecimalOperations = ""
        
        if self._isValidDecimal():
            decimalOperations = "decimal : Suma Resta Multiplicacion y Division"
        
        if self._isValidBinary():
            binaryOperations = "Binario : Suma Binaria Resta Binaria Multiplicacion Binaria Division Binaria"
        
        if self._isValidHexadecimal():
            hexadecimalOperations = "Hexadecimal : Suma Hexadecimal Resta Hexadecimal Multiplicacion Division Hexadecimal"
        
        self._buildOperationString(decimalOperations, binaryOperations, hexadecimalOperations)
    
    def _isValidDecimal(self):
        try:
            cleanNumber = self.numberString.replace('-', '')
            
            validChars = "0123456789."
            for char in cleanNumber:
                if char not in validChars:
                    return False
            
            if cleanNumber.count('.') > 1:
                return False
            
            float(self.numberString)
            return True
        except ValueError:
            return False
    
    def _isValidBinary(self):
    
        try:
            cleanNumber = self.numberString.replace('-', '')
            
            validChars = "01."
            for char in cleanNumber:
                if char not in validChars:
                    return False
            
            if cleanNumber.count('.') > 1:
                return False
            
            if '.' in cleanNumber:

                dotIndex = self._findCharacterIndex(cleanNumber, '.')
                integerPart = cleanNumber[:dotIndex]
                decimalPart = cleanNumber[dotIndex + 1:]
                
                if integerPart and not self._isValidBinaryInteger(integerPart):
                    return False
                
                if decimalPart and not self._isValidBinaryInteger(decimalPart):
                    return False
            else:
                
                if not self._isValidBinaryInteger(cleanNumber):
                    return False
            
            return True
        except:
            return False
    
    def _isValidBinaryInteger(self, binaryStr):
        
        if not binaryStr:
            return False
        for char in binaryStr:
            if char not in "01":
                return False
        return True
    
    def _findCharacterIndex(self, text, character):
        
        for i in range(len(text)):
            if text[i] == character:
                return i
        return -1
    
    def _isValidHexadecimal(self):
        
        try:
            
            cleanNumber = self.numberString.replace('-', '')
            
            validChars = "0123456789ABCDEFabcdef."
            for char in cleanNumber:
                if char not in validChars:
                    return False
            
            if cleanNumber.count('.') > 1:
                return False
            
            if '.' in cleanNumber:

                dotIndex = self._findCharacterIndex(cleanNumber, '.')
                integerPart = cleanNumber[:dotIndex]
                decimalPart = cleanNumber[dotIndex + 1:]
                
                if integerPart and not self._isValidHexInteger(integerPart):
                    return False
                
                if decimalPart and not self._isValidHexInteger(decimalPart):
                    return False
            else:
                
                if not self._isValidHexInteger(cleanNumber):
                    return False
            
            return True
        except:
            return False
    
    def _isValidHexInteger(self, hexStr):
        
        if not hexStr:
            return False
        validChars = "0123456789ABCDEFabcdef"
        for char in hexStr:
            if char not in validChars:
                return False
        return True
    
    def _buildOperationString(self, decimalOperations, binaryOperations, hexadecimalOperations):
        
        finalString = ""
        
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
        
        if finalString:
            self.elementalOperation = finalString
        else:
            self.elementalOperation = "No hay operaciones válidas disponibles para este número"
    
    def binaryAddition(self, other):
    
        decimal1 = self._binaryToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._binaryToDecimal(other.numberString.replace('-', ''))
        
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        result = decimal1 + decimal2
        
        return self._decimalToBinary(result)
    
    def binarySubtraction(self, other):

        decimal1 = self._binaryToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._binaryToDecimal(other.numberString.replace('-', ''))
        
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        result = decimal1 - decimal2
        
        return self._decimalToBinary(result)
    
    def binaryMultiplication(self, other):
        decimal1 = self._binaryToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._binaryToDecimal(other.numberString.replace('-', ''))
        
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        result = decimal1 * decimal2
        
        return self._decimalToBinary(result)
    
    def binaryDivision(self, other):
        decimal1 = self._binaryToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._binaryToDecimal(other.numberString.replace('-', ''))
        
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        if decimal2 == 0:
            return "Error: División por cero"
        
        result = decimal1 / decimal2
        
        return self._decimalToBinary(result)
    
    def hexAddition(self, other):
        decimal1 = self._hexToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._hexToDecimal(other.numberString.replace('-', ''))
        
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        result = decimal1 + decimal2
        
        return self._decimalToHex(result)
    
    def hexSubtraction(self, other):
        decimal1 = self._hexToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._hexToDecimal(other.numberString.replace('-', ''))
        
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        result = decimal1 - decimal2
        
        return self._decimalToHex(result)
    
    def hexMultiplication(self, other):
        decimal1 = self._hexToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._hexToDecimal(other.numberString.replace('-', ''))
        
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        result = decimal1 * decimal2
        
        return self._decimalToHex(result)
    
    def hexDivision(self, other):
        decimal1 = self._hexToDecimal(self.numberString.replace('-', ''))
        decimal2 = self._hexToDecimal(other.numberString.replace('-', ''))
        
        if self.numberString.startswith('-'):
            decimal1 = -decimal1
        if other.numberString.startswith('-'):
            decimal2 = -decimal2
        
        if decimal2 == 0:
            return "Error: División por cero"
        
        result = decimal1 / decimal2
        
        return self._decimalToHex(result)
    
    def _reverseString(self, text):
        reversedText = ""
        for i in range(len(text) - 1, -1, -1):
            reversedText += text[i]
        return reversedText
    
    def _binaryToDecimal(self, binaryStr):
        if '.' in binaryStr:
            dotIndex = self._findCharacterIndex(binaryStr, '.')
            integerPart = binaryStr[:dotIndex]
            decimalPart = binaryStr[dotIndex + 1:]
            
            integerValue = 0
            reversedInteger = self._reverseString(integerPart)
            for i in range(len(reversedInteger)):
                digit = reversedInteger[i]
                integerValue += int(digit) * (2 ** i)
            
            decimalValue = 0
            for i in range(len(decimalPart)):
                digit = decimalPart[i]
                decimalValue += int(digit) * (2 ** -(i + 1))
            
            return integerValue + decimalValue
        else:
            result = 0
            reversedBinary = self._reverseString(binaryStr)
            for i in range(len(reversedBinary)):
                digit = reversedBinary[i]
                result += int(digit) * (2 ** i)
            return result
    
    def _decimalToBinary(self, decimalNum):
        if decimalNum == 0:
            return "0"
        
        isNegative = decimalNum < 0
        decimalNum = abs(decimalNum)
        
        integerPart = int(decimalNum)
        decimalPart = decimalNum - integerPart
        
        if integerPart == 0:
            integerBinary = "0"
        else:
            integerBinary = ""
            while integerPart > 0:
                integerBinary = str(integerPart % 2) + integerBinary
                integerPart //= 2
        
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
        hexStr = hexStr.upper()
        
        if '.' in hexStr:
            dotIndex = self._findCharacterIndex(hexStr, '.')
            integerPart = hexStr[:dotIndex]
            decimalPart = hexStr[dotIndex + 1:]
            
            integerValue = 0
            reversedInteger = self._reverseString(integerPart)
            for i in range(len(reversedInteger)):
                digit = reversedInteger[i]
                digitValue = int(digit) if digit.isdigit() else ord(digit) - ord('A') + 10
                integerValue += digitValue * (16 ** i)
            
            decimalValue = 0
            for i in range(len(decimalPart)):
                digit = decimalPart[i]
                digitValue = int(digit) if digit.isdigit() else ord(digit) - ord('A') + 10
                decimalValue += digitValue * (16 ** -(i + 1))
            
            return integerValue + decimalValue
        else:
            result = 0
            reversedHex = self._reverseString(hexStr)
            for i in range(len(reversedHex)):
                digit = reversedHex[i]
                digitValue = int(digit) if digit.isdigit() else ord(digit) - ord('A') + 10
                result += digitValue * (16 ** i)
            return result
    
    def _getHexDigit(self, value):
        if value >= 0 and value <= 9:
            return chr(ord('0') + value)
        elif value >= 10 and value <= 15:
            return chr(ord('A') + (value - 10))
        else:
            return "0"
    
    def _decimalToHex(self, decimalNum):
        if decimalNum == 0:
            return "0"
        
        isNegative = decimalNum < 0
        decimalNum = abs(decimalNum)
        
        integerPart = int(decimalNum)
        decimalPart = decimalNum - integerPart
        
        if integerPart == 0:
            integerHex = "0"
        else:
            integerHex = ""
            while integerPart > 0:
                remainder = integerPart % 16
                integerHex = self._getHexDigit(remainder) + integerHex
                integerPart //= 16
        
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
        return self.elementalOperation
    
    def getPrintFormat(self):
        return f"Numero: {self.numberString} | Operaciones: {self.elementalOperation}"
    
    def __str__(self):
        return f"Numero: {self.numberString} - Operaciones disponibles: {self.elementalOperation}"