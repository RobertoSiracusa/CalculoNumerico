import os

class ArchiveUtil:
    def __init__(self, router=""):
        if not router or not router.strip():
            raise ValueError("La ruta asignada no es válida.")
        self.__router = None  
        self.__utilDirectory(router)  
    
    def getRouter(self):
        return self.__router
    
    def setRouter(self, newRouter):
        self.__utilDirectory(newRouter)
    
    def __utilDirectory(self, router):
        if not os.path.exists(router):
            raise FileNotFoundError("El directorio a guardar no existe.")
        self.__router = router
    
    def getArchive(self, nameArchive):
        if not nameArchive or not nameArchive.strip():
            raise ValueError("El nombre del archivo es requerido.")
        
        fullPath = os.path.join(self.__router, nameArchive)
        if not os.path.isfile(fullPath):
            raise FileNotFoundError("El archivo no se encontró en el directorio especificado.")
        
        try:
            return open(fullPath, 'rb')
        except PermissionError:
            raise PermissionError("No se tienen permisos para leer al archivo.") 
    
    def setCreateArchive(self, content, nameArchive, addNewLine =False):
        if not content or not content.strip(): 
            raise ValueError("El contenido es requerido.")
        if not nameArchive:
            raise ValueError("El nombre del archivo es requerido.")
        
        fullPath = os.path.join(self.__router, f"{nameArchive}.txt")
        mode = 'a' if os.path.exists(fullPath) else 'w'

        with open(fullPath, mode) as file:
            file.write(content) 
            if addNewLine:
                file.write('\n')
    
    def getDirectories(self):
        if not os.path.exists(self.__router):
            raise FileNotFoundError("El directorio no existe.")
        
        files = os.listdir(self.__router)
        if not files:
            raise FileNotFoundError("No se encontraron archivos.")
        return files
    
    def directoriesExist(self):
        if not os.path.exists(self.__router):
            return False  
        return bool(os.listdir(self.__router))