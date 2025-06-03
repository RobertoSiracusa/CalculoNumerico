
import Composables.storageArray as sA
import Process.ProcessFunctions as pf
import Repositories.archiveUtil as ArchiveUtil
import Composables.storeNumbers as storeNumbers

def main():
    pathToFile = "src/Storage"
    fileName = 'random_representation_numbers.bin'
    
    try:
        archive = ArchiveUtil.ArchiveUtil(pathToFile)
        
        with archive.getArchive(fileName) as file:
            binary_content = file.read()  
            
        dataArray = pf.initArray(binary_content)
        dataArray = pf.binNumpyArray(binary_content, dataArray)
        
        storeNumbers.storeSignificantFigures(dataArray, pathToFile)
        print("Datos almacenados correctamente.")
        
        archive=None
        dataArray=None
    except Exception as e:
        print(f"Error: {e}")
        
main()
