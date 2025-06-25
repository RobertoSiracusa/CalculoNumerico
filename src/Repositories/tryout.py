from Helpers.utils import logWriter
from Repositories import numericSystem

class elementalOperation1:
    def __init__(self, numericSystemObject:numericSystem.numericSystem):
        self.numericSystem=numericSystemObject
        self.elementalOperationResult=None
        self._determineAvailableOperations()

    def _determineAvailableOperations(self):
        if self.numericSystem.binSystem:
            self.checkBinaryOperations()
        if self.numericSystem.decSystem:
            self.checkDecimalOperations()
        if self.numericSystem.hexSystem:
            self.checkHexadecimalOperations()
        if not (self.numericSystem.binSystem or self.numericSystem.decSystem or self.numericSystem.hexSystem):
            logWriter("ERROR:No hay operaciones disponibles para el sistema numérico proporcionado.",True)

    def checkDecimalOperations(self):
        decNumber= self.numericSystem.number
        if decNumber == '0' or decNumber == '0.0':
            logWriter("ERROR:No hay operaciones disponibles para el número 0.",True)
            return
        output= f"Operaciones disponibles para el número en base decimal {decNumber}:"
        
        if self.decSum():
            output += "- Suma"
        if self.decSubtraction():
            output += "- Resta"
        if self.decMultiplication():
            output += "- Multiplicación"
        if self.decDivision():
            output += "- División"
        output += "\t"
        self.elementalOperationResult += output


    def decSum(self):
        decNumber=int(self.numericSystem.number)
        try:
            result = 0
            for i in range(0,decNumber):
                result = result+ 1
            return True
        except Exception as e:
            
            return False
    def decSubtraction(self):
        decNumber=int(self.numericSystem.number)
        try:
            result = decNumber
            for i in range(0,decNumber):
                result = decNumber - 1
            return True
        except Exception as e:
            
            return False
        
    def decMultiplication(self):
        decNumber=int(self.numericSystem.number)
        try:
            result = 1
            for i in range(0,decNumber-1):
                result = result+decNumber
            return True
        except Exception as e:
            
            return False
    def decDivision(self):
        decNumber=int(self.numericSystem.number)
        try:
            result = decNumber
            for i in range(0,decNumber-1):
                result = result / 2
            return True
        except Exception as e:
            
            return False

    def _sumOneBit(bit1, bit2, carryIn):
 
        totalSum = int(bit1) + int(bit2) + int(carryIn)
        if totalSum == 0:
            return '0', '0'
        elif totalSum == 1:
            return '1', '0'
        elif totalSum == 2: 
            return '0', '1'
        elif totalSum == 3: 
            return '1', '1'

    def _subtractOneBit(bit1, bit2, borrowIn):
        
        
        valBit1 = int(bit1)
        valBit2 = int(bit2)
        valBorrowIn = int(borrowIn)

        tempValBit1 = valBit1 - valBorrowIn

        if tempValBit1 >= valBit2:
            
            return str(tempValBit1 - valBit2), '0'
        else:
            
            return str(tempValBit1 + 2 - valBit2), '1'

    def binAdd(self):
       
        binaryNum = self.numericSystem.number
        
        try:
            resultBinary = ""
            carry = '1' 
            
            for i in range(len(binaryNum) - 1, -1, -1):
                currentDigit = binaryNum[i]
                
                if carry == '1': 
                    if currentDigit == '0':
                        resultBinary = '1' + resultBinary
                        carry = '0' 
                    else: 
                        resultBinary = '0' + resultBinary
                        
                else: 
                    resultBinary = currentDigit + resultBinary

            
            if carry == '1':
                resultBinary = '1' + resultBinary
                
            
            return True 
        except Exception as e:
            logWriter(f"Error en Suma Binaria: {e}", True)
            return False

    def binSubtract(self):
       
        binaryNum = self.numericSystem.number
        
        try:
            if binaryNum == '0':
                logWriter("Error en la Resta Binaria: No se puede restar 1 de 0.", True)
                return False

            resultBinary = ""
            foundOne = False 
            
            for i in range(len(binaryNum) - 1, -1, -1):
                currentDigit = binaryNum[i]
                
                if not foundOne:
                    if currentDigit == '1':
                        resultBinary = '0' + resultBinary
                        foundOne = True 
                    else: 
                        resultBinary = '1' + resultBinary 
                else: 
                    resultBinary = currentDigit + resultBinary
            
            if resultBinary and resultBinary != '0':
                resultBinary = resultBinary.lstrip('0')
                if not resultBinary: 
                    resultBinary = '0'
            elif not resultBinary: 
                resultBinary = '0'
            return True 
        except Exception as e:
            logWriter(f"Error en la Resta Binaria: {e}", True)
            return False

    def binMultiply(self):
        
        binaryNum = self.numericSystem.number
        
        try:
            
            if binaryNum == '0':
                resultBinary = '0'
            else:
                resultBinary = binaryNum + '0'
                
            return True
        except Exception as e:
            logWriter(f"Error en la Multiplicación Binaria (por 2): {e}", True)
            return False

    def binDivide(self):
        
        binaryNum = self.numericSystem.number
        
        try:
            
            if binaryNum == '0':
                resultBinary = '0' 
            elif len(binaryNum) == 1:
                resultBinary = '0' 
            else:
                resultBinary = binaryNum[:-1] 

            if not resultBinary:
                resultBinary = '0'
                
            return True
        except Exception as e:
            logWriter(f"Error en la División Binaria (por 2): {e}", True)
            return False
    def hexAdd(self):
        hexNum = self.numericSystem.number
        
        try:
            resultHex = ""
            carry = 0
            
            hexDigits = "0123456789ABCDEF"
            hexDict = {hexDigits[i]: i for i in range(len(hexDigits))}
            
            for i in range(len(hexNum) - 1, -1, -1):
                currentDigit = hexNum[i]
                currentValue = hexDict[currentDigit]
                
                totalSum = currentValue + carry + 1
                
                if totalSum >= 16:
                    carry = 1
                    totalSum -= 16
                else:
                    carry = 0
                
                resultHex = hexDigits[totalSum] + resultHex
            
            if carry > 0:
                resultHex = hexDigits[carry] + resultHex
                
            return True
        except Exception as e:
            logWriter(f"Error en Suma Hexadecimal: {e}", True)
            return False
    def hexSub(self):
        hexNum = self.numericSystem.number
        
        try:
            if hexNum == '0':
                logWriter("Error en la Resta Hexadecimal: No se puede restar 1 de 0.", True)
                return False

            resultHex = ""
            foundOne = False 
            
            hexDigits = "0123456789ABCDEF"
            hexDict = {hexDigits[i]: i for i in range(len(hexDigits))}
            
            for i in range(len(hexNum) - 1, -1, -1):
                currentDigit = hexNum[i]
                currentValue = hexDict[currentDigit]
                
                if not foundOne:
                    if currentValue > 0:
                        resultHex = hexDigits[currentValue - 1] + resultHex
                        foundOne = True 
                    else: 
                        resultHex = 'F' + resultHex 
                else: 
                    resultHex = currentDigit + resultHex
            
            if resultHex and resultHex != '0':
                resultHex = resultHex.lstrip('0')
                if not resultHex: 
                    resultHex = '0'
            elif not resultHex: 
                resultHex = '0'
                
            return True
        except Exception as e:
            logWriter(f"Error en la Resta Hexadecimal: {e}", True)
            return False
    def hexMultiply(self):
        hexNum = self.numericSystem.number
        
        try:
            if hexNum == '0':
                resultHex = '0'
            else:
                resultHex = hexNum + '0'
                
            return True
        except Exception as e:
            logWriter(f"Error en la Multiplicación Hexadecimal (por 2): {e}", True)
            return False
    def hexDivide(self):
        hexNum = self.numericSystem.number
        
        try:
            if hexNum == '0':
                resultHex = '0' 
            elif len(hexNum) == 1:
                resultHex = '0' 
            else:
                resultHex = hexNum[:-1] 

            if not resultHex:
                resultHex = '0'
                
            return True
        except Exception as e:
            logWriter(f"Error en la División Hexadecimal (por 2): {e}", True)
            return False
    
    def getPrintFormat(self):
        if self.elementalOperationResult is None:
            logWriter("ERROR: No se han realizado operaciones elementales en el sistema numérico.", True)

        return self.elementalOperationResult.strip() if self.elementalOperationResult else "No hay operaciones disponibles."