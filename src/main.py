

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
            
        dataArrayN1 = pf.initArray(binary_content)
       
         
        dataArrayN1 = pf.binNumpyArray(binary_content, dataArrayN1)
        storeNumbers.storeSignificantFigures(dataArrayN1)

        dataArrayN1 = pf.processArray(dataArrayN1)
        
        storeNumbers.storeGaussJordan(dataArrayN1)

        
        
        
        archive=None
        dataArray1=None
    except Exception as e:
        logWriter("Error al procesar archivo: " + str(e), True)
        
main()
