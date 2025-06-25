import datetime
import random
import Repositories.archiveUtil as ArchiveUtil
from Repositories.significantFigures import significantFigures
from Repositories.numericSystem import numericSystem
from Helpers.utils import logWriter, txtWriter
from Repositories.elementalOperation import elementalOperation
def storeSignificantFigures(dataArray,basePath):

    currentDateTime = datetime.datetime.now()
    formattedDateTime = currentDateTime.strftime("%Y-%m-%d_%H-%M-%S")
    randNum = random.randint(1, 100)
    outputFileName = f"InformaciónNumérica_{formattedDateTime}_serial{randNum}"
    

    

    for i in range(dataArray.shape[0]):
        for j in range(dataArray.shape[1]):
            value = dataArray[i, j]
            if value == "%z":  
                continue
            try:
                
                sf = significantFigures(value)
                nS = numericSystem(value)
                eO = elementalOperation(value, nS.binSystem, nS.decSystem, nS.hexSystem)

                text= sf.toString()+"\n"+nS.toString()+"\n"+eO.toString()+"\n"
                txtWriter(outputFileName,text,True)
            except ValueError as e:
                print(f"Error procesando '{value}': {e}")
                continue