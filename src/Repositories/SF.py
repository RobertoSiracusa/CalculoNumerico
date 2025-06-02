class SignificantFigures:

    def __init__(self, number):
        self.number = str(number)  # Convertir a string
        self.significantFigures = None
        # Ejecutar el método 1 al crear el objeto
        self.checkDecimalSystem()
    
    # Método 1: Verifica si el número es decimal
    def checkDecimalSystem(self):
        # Limpiamos el número de espacios
        cleanNumber = self.number.strip()
        if cleanNumber.startswith('-') or cleanNumber.startswith('+'):
            cleanNumber = cleanNumber[1:]
        
        # Verificamos que solo contenga dígitos decimales y máximo un punto
        dotFound = False
        for char in cleanNumber:
            if char== ',':
                # Si se encuentra una coma, la convertimos a punto
                char = '.'
            if char == '.':
                if dotFound:  # Más de un punto
                    self.setSignificantFigures("Sistema Numérico Inválido")
                    return
                dotFound = True
            elif not char.isdigit():
                # Contiene caracteres no válidos para decimal
                self.setSignificantFigures("Sistema Numérico Inválido")
                return
        
        # Si llegamos aquí, es un número decimal válido
        self.calculateSignificantFigures()
    
    # Método 2: Calcula las cifras significativas para números decimales
    def calculateSignificantFigures(self):
        # Quitamos el signo negativo si existe (no afecta las cifras significativas)
        cleanNumber = self.number.strip()
        if cleanNumber.startswith('-') or cleanNumber.startswith('+'):
            cleanNumber = cleanNumber[1:]
        
        # Caso especial: solo cero
        if cleanNumber == '0' or cleanNumber == '0.0':
            self.setSignificantFigures(0)
            return
        
        # Separamos parte entera y decimal
        parts = cleanNumber.split('.')
        
        if len(parts) == 1:  # Solo parte entera
            # Eliminamos ceros a la izquierda
            numWithoutLeadingZeros = cleanNumber.lstrip('0')
            if not numWithoutLeadingZeros:  # El número es solo ceros
                self.setSignificantFigures(0)
            else:
                # Para números enteros sin punto decimal, los ceros finales no son significativos
                # Contamos solo hasta el último dígito no cero
                lastNonZero = len(numWithoutLeadingZeros)
                for i in range(len(numWithoutLeadingZeros) - 1, -1, -1):
                    if numWithoutLeadingZeros[i] != '0':
                        lastNonZero = i + 1
                        break
                self.setSignificantFigures(lastNonZero)
        else:
            integerPart, decimalPart = parts
            
            # Si es 0.000... (solo ceros en la parte decimal)
            if all(c == '0' for c in cleanNumber.replace('.', '')):
                # Para números como 0.000, las cifras significativas son todos los ceros después del punto
                self.setSignificantFigures(len(decimalPart) if decimalPart else 1)
                return
            
            # Si la parte entera es solo ceros o vacía
            if not integerPart or integerPart == '0' or all(c == '0' for c in integerPart):
                # Buscamos el primer dígito significativo en la parte decimal
                firstSignificant = 0
                for i, digit in enumerate(decimalPart):
                    if digit != '0':
                        firstSignificant = i
                        break
                
                # Contamos desde el primer dígito significativo hasta el final
                significantDigits = decimalPart[firstSignificant:]
                self.setSignificantFigures(len(significantDigits))
            else:
                # La parte entera tiene dígitos significativos
                integerPartWithoutZeros = integerPart.lstrip('0')
                # Todos los dígitos de la parte entera (sin ceros a la izquierda) 
                # más todos los dígitos de la parte decimal son significativos
                # Cuando hay punto decimal, todos los ceros finales en la parte decimal son significativos
                self.setSignificantFigures(len(integerPartWithoutZeros) + len(decimalPart))
    
    # Método 3: Retorna un string 
    def toString(self):
        return f"Número: {self.number} Cifras Significativas: {self.significantFigures}"
    
    # Getters
    def getNumber(self):
        return self.number
    
    def getSignificantFigures(self):
        return self.significantFigures
    
    # Setters
    def setNumber(self, number):
        self.number = str(number)
        # Recalcular cifras significativas cuando se cambia el número
        self.checkDecimalSystem()
    
    def setSignificantFigures(self, figures):
        self.significantFigures = figures