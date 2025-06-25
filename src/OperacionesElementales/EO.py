import numpy as np
from datetime import datetime
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Repositories'))

from Repositories.archiveUtil import ArchiveUtil
from OperacionesMatrices import MatrixOperations
from ValidadorFormulas import FormulaValidator

class ElementaryMatrixOperations:
    def __init__(self):
        self.name = "Operaciones Elementales de Matrices"
        self.operations = MatrixOperations()
        self.validator = FormulaValidator()
        self.availableMatrices = self.validator.availableMatrices
    
    def registerMatrix(self, name, matrix):
        return self.validator.registerMatrix(name, matrix)
    
    def addMatrices(self, matrixA, matrixB):
        return self.operations.addMatrices(matrixA, matrixB)
    
    def subtractMatrices(self, matrixA, matrixB):
        return self.operations.subtractMatrices(matrixA, matrixB)
    
    def scalarMultiplication(self, matrix, scalar):
        return self.operations.scalarMultiplication(matrix, scalar)
    
    def matrixMultiplication(self, matrixA, matrixB):
        return self.operations.matrixMultiplication(matrixA, matrixB)
    
    def transpose(self, matrix):
        return self.operations.transpose(matrix)
    
    def matrixInverse(self, matrix):
        return self.operations.matrixInverse(matrix)
    
    def isDigit(self, character):
        return self.validator.isDigit(character)
    
    def isUpperCaseLetter(self, character):
        return self.validator.isUpperCaseLetter(character)
    
    def extractDecimalNumber(self, text, start):
        return self.validator.extractDecimalNumber(text, start)
    
    def extractFormulaTermsManual(self, formula):
        return self.validator.extractFormulaTerms(formula)
    
    def validateFormulaStructureManual(self, formula):
        return self.validator.validateFormulaStructure(formula)
    
    def validateAvailableMatrices(self, formula):
        return self.validator.validateAvailableMatrices(formula)
    
    def validateCompatibleDimensions(self, formula):
        return self.validator.validateCompatibleDimensions(formula)
    
    def evaluateInternalFormula(self, formula):
        return self.validator.evaluateInternalFormula(formula)
    
    def validateFormula(self, formula):
        return self.validator.validateFormula(formula)

    def extractFormulaTerms(self, formula):
        return self.extractFormulaTermsManual(formula)
    
    def validateFormulaStructure(self, formula):
        return self.validateFormulaStructureManual(formula)
    
    def getSystemInfo(self):
        return self.validator.getSystemInfo()
    
    def clearMatrices(self):
        return self.validator.clearMatrices()
    
    def saveResultsTxt(self, formulasFile):
        try:
            archiveUtil = ArchiveUtil(".")
            formulas = []
            
            with archiveUtil.getArchive(formulasFile) as file:
                for line in file:
                    formula = line.decode('utf-8').strip()
                    if formula:
                        formulas.append(formula)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            content = f"REPORTE VALIDACIÓN - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            content += "=" * 50 + "\n\n"
            
            for formula in formulas:
                result = self.validateFormula(formula)
                validity = "VÁLIDA" if result else "NO VÁLIDA"
                
                content += f"Fórmula: {formula}\n"
                content += f"Resultado: {validity}\n"
                content += "-" * 30 + "\n"
            
            fileName = f"resultados_validacion_{timestamp}"
            archiveUtil.setCreateArchive(content, fileName, append_newline=False, booleano=True)
            
            return f"{fileName}.txt"
            
        except Exception as e:
            return None 