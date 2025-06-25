import numpy as np
from OperacionesMatrices import MatrixOperations

class FormulaValidator:
    def __init__(self):
        self.availableMatrices = {}
        self.operations = MatrixOperations()
    
    def registerMatrix(self, name, matrix):
        try:
            if not isinstance(matrix, np.ndarray):
                matrix = np.array(matrix, dtype=float)
            self.availableMatrices[name] = matrix
            return True
        except Exception:
            return False
    
    def isDigit(self, character):
        return character in '0123456789'
    
    def isUpperCaseLetter(self, character):
        return character in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def extractDecimalNumber(self, text, start):
        pos = start
        numberStr = ""
        pointFound = False
        
        while pos < len(text):
            char = text[pos]
            if self.isDigit(char):
                numberStr += char
                pos += 1
            elif char == '.' and not pointFound:
                numberStr += char
                pointFound = True
                pos += 1
            else:
                break
        
        return numberStr, pos
    
    def extractFormulaTerms(self, formula):
        try:
            cleanFormula = formula.replace(" ", "")
            terms = []
            pos = 0
            
            while pos < len(cleanFormula):
                sign = "+"
                scalarStr = ""
                matrixName = ""
                transpose = False
                inverse = False
                
                if pos < len(cleanFormula) and cleanFormula[pos] in "+-":
                    sign = cleanFormula[pos]
                    pos += 1
                elif len(terms) == 0:
                    sign = "+"
                
                scalarStr, pos = self.extractDecimalNumber(cleanFormula, pos)
                
                if pos < len(cleanFormula) and self.isUpperCaseLetter(cleanFormula[pos]):
                    matrixName = cleanFormula[pos]
                    pos += 1
                else:
                    return [] 
                
                if pos < len(cleanFormula) and cleanFormula[pos] == '^':
                    pos += 1
                    if pos < len(cleanFormula):
                        if cleanFormula[pos] == 'T':
                            transpose = True
                            pos += 1
                        elif cleanFormula[pos] == '-' and pos + 1 < len(cleanFormula) and cleanFormula[pos + 1] == '1':
                            inverse = True
                            pos += 2
                        else:
                            return [] 
                
                if scalarStr == "":
                    scalarValue = 1.0
                else:
                    try:
                        scalarValue = float(scalarStr)
                    except ValueError:
                        return [] 

                if sign == "-":
                    scalarValue = -scalarValue
                
                terms.append({
                    'escalar': scalarValue,
                    'matriz': matrixName,
                    'transpuesta': transpose,
                    'inversa': inverse,
                    'tieneEscalarExplicito': scalarStr != ""
                })
            
            return terms
        except Exception:
            return []
    
    def validateFormulaStructure(self, formula):
        try:
            cleanFormula = formula.replace(" ", "")
            
            if not cleanFormula:
                return False

            terms = self.extractFormulaTerms(formula)
            if not terms:
                return False
            
            return True
        except Exception:
            return False
    
    def validateAvailableMatrices(self, formula):
        try:
            terms = self.extractFormulaTerms(formula)
            if not terms:
                return False
            
            for term in terms:
                if term['matriz'] not in self.availableMatrices:
                    return False
            
            return True
        except Exception:
            return False
    
    def validateCompatibleDimensions(self, formula):
        try:
            terms = self.extractFormulaTerms(formula)
            if not terms:
                return False

            for term in terms:
                if term.get('inversa', False):
                    matrix = self.availableMatrices[term['matriz']]
                    if matrix.shape[0] != matrix.shape[1]:
                        return False  
            
            firstTerm = terms[0]
            baseMatrix = self.availableMatrices[firstTerm['matriz']]
            
            if firstTerm.get('inversa', False):
                expectedDimension = baseMatrix.shape  
            elif firstTerm['transpuesta']:
                expectedDimension = (baseMatrix.shape[1], baseMatrix.shape[0])
            else:
                expectedDimension = baseMatrix.shape
            
            for term in terms[1:]:
                matrix = self.availableMatrices[term['matriz']]
                
                if term.get('inversa', False):
                    currentDimension = matrix.shape 
                elif term['transpuesta']:
                    currentDimension = (matrix.shape[1], matrix.shape[0])
                else:
                    currentDimension = matrix.shape
                
                if currentDimension != expectedDimension:
                    return False
            
            return True
        except Exception:
            return False
    
    def evaluateInternalFormula(self, formula):
        try:
            terms = self.extractFormulaTerms(formula)
            if not terms:
                return False
            
            result = None
            
            for term in terms:
                originalMatrix = self.availableMatrices[term['matriz']]
                
                if term.get('inversa', False):
                    if not self.operations.matrixInverse(originalMatrix):
                        return False
 
                    processedMatrix = self.operations.calculateInverse(originalMatrix)
                    if processedMatrix is None:
                        return False
                        
                elif term['transpuesta']:
                    processedMatrix = self.operations.calculateTranspose(originalMatrix)
                else:
                    processedMatrix = originalMatrix.copy()
                
                if term['tieneEscalarExplicito'] or term['escalar'] != 1.0:
                    processedMatrix = self.operations.applyScalar(
                        processedMatrix, term['escalar']
                    )
                
                if result is None:
                    result = processedMatrix.copy()
                else:
                    newSum = self.operations.addMatricesResult(result, processedMatrix)
                    if newSum is None:
                        return False
                    result = newSum
            
            return True
        except Exception:
            return False
    
    def validateFormula(self, formula):
        try:
            if not self.validateFormulaStructure(formula):
                return False
            
            if not self.validateAvailableMatrices(formula):
                return False
            
            if not self.validateCompatibleDimensions(formula):
                return False
            
            if not self.evaluateInternalFormula(formula):
                return False
            
            return True
        except Exception:
            return False
    
    def getSystemInfo(self):
        return {
            'matricesRegistradas': len(self.availableMatrices),
            'nombresMatrices': list(self.availableMatrices.keys())
        }
    
    def clearMatrices(self):
        self.availableMatrices.clear()
        return True 