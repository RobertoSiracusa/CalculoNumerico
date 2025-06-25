
import Composables.storageArray as sA
from Helpers.utils import logWriter
import Process.ProcessFunctions as pf
import Repositories.archiveUtil as ArchiveUtil
import Composables.storeNumbers as storeNumbers

def main():
    pathToFile = "src/Storage"
    arrayFile1 = 'random_representation_numbers.bin'
    arrayFile2 = 'random_representation_numbers_2.bin'

    try:
        archive = ArchiveUtil.ArchiveUtil(pathToFile)
        
        with archive.getArchive(arrayFile1) as file:
            binary_content = file.read()  
            
        dataArray = pf.initArray(binary_content)
        dataArray = pf.binNumpyArray(binary_content, dataArray)
        
        storeNumbers.storeSignificantFigures(dataArray, pathToFile)
        print("Datos almacenados correctamente.")
        
        archive=None
        dataArray=None
    except Exception as e:
        logWriter("Error al procesar el archivo: " + str(e), True)
        
main()
