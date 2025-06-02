import datetime
import random
import archiveUtil as ArchiveUtil

def saveArrayToTxt(dataArray, basePath):
    # Convertir el array numpy a formato de texto
    contentLines = []
    for row in dataArray:
        # Convertir cada fila a string separado por '#'
        lineContent = '#'.join(str(element) for element in row)
        contentLines.append(lineContent)
    
    # Unir todas las líneas con saltos de línea
    contentText = '\n'.join(contentLines)
    
    # Generar el nombre del archivo con formato requerido
    currentDateTime = datetime.datetime.now()
    formattedDateTime = currentDateTime.strftime("%Y-%m-%d_%H-%M-%S")
    randNum = random.randint(1, 100)
    outputFileName = f"extracted_numbers{formattedDateTime}_serial{randNum}"
    
    # Usar ArchiveUtil para guardar el archivo
    archiveUtilInstance = ArchiveUtil.ArchiveUtil(basePath)
    archiveUtilInstance.set_create_archive(contentText, outputFileName, append_newline=False)