import datetime
import random
import Repositories.archiveUtil as ArchiveUtil
from Helpers.utils import txtWriter
def saveArrayToTxt(dataArray, basePath):
    
    contentText = ""
    numRows = dataArray.shape[0]
    for i in range(numRows):
        row = dataArray[i]
        lineContent = ""
        num_cols = row.shape[0]
        for j in range(num_cols):
            lineContent += str(row[j])
            if j < num_cols - 1:
                lineContent += "#"
        contentText += lineContent
        if i < numRows - 1:
            contentText += "\n"

    
    currentDateTime = datetime.datetime.now()
    formattedDateTime = currentDateTime.strftime("%Y-%m-%d_%H-%M-%S")
    randNum = random.randint(1, 100)
    outputFileName = f"Numeros_en_Txt_{formattedDateTime}_serial{randNum}"

    
    archiveUtilInstance = ArchiveUtil.ArchiveUtil(basePath)
    archiveUtilInstance.set_create_archive(contentText, outputFileName, append_newline=False)