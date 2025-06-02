
import Composables.storageArray as sA
import Process.ProcessFunctions as pf
import Repositories.archiveUtil as ArchiveUtil

def main():
    path_to_compressed_file = "src/Storage"
    file_name = 'random_representation_numbers.bin'

    try:
        archive = ArchiveUtil.ArchiveUtil(path_to_compressed_file)
        
        # MODIFICACIÓN: Usar contexto with para gestión automática
        with archive.getArchive(file_name) as file:
            binary_content = file.read()  # Leer contenido una vez
            
        # Pasar contenido binario a las funciones
        dataArray = pf.initArray(binary_content)
        dataArray = pf.binNumpyArray(binary_content, dataArray)
        
        pf.printArray(dataArray)
        
        sA.saveArrayToTxt(dataArray, path_to_compressed_file)
        
        dataArray=None
    except Exception as e:
        print(f"Error: {e}")
        
main()
