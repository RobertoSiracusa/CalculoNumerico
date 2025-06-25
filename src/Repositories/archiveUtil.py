import os

class ArchiveUtil:
    def __init__(self, router=""):
        if not router or not router.strip():
            raise ValueError("La ruta asignada no es válida.")
        self._router = None
        self.utilDirectory(router)
    
    @property
    def router(self):
        return self._router
    
    @router.setter
    def router(self, newRouter):
        self.utilDirectory(newRouter)
    
    def utilDirectory(self, router):
        if not os.path.exists(router):
            raise FileNotFoundError("El directorio a guardar no existe.")
        self._router = router
    
    def getArchive(self, fileName):
        if not fileName or not fileName.strip():
            raise ValueError("El nombre del archivo es requerido.")
        
        fullFilePath = os.path.join(self._router, fileName)
        if not os.path.isfile(fullFilePath):
            raise FileNotFoundError("El archivo no se encontro en el directorio especificado.")
        
        return open(fullFilePath, 'rb')

    def setCreateArchiveLog(self, content, logFileName, outputLogFileName, append_newline=False):

        fullFilePath = os.path.join(self._router, f"{logFileName}.log")
        mode = 'a' if os.path.exists(fullFilePath) else 'w'

        with open(fullFilePath, mode) as file:
            file.write(outputLogFileName+content) 
            if append_newline:
                file.write('\n')
    def setCreateArchiveTxt(self, content, fileName, append_newline=False):
        
        if not content or not content.strip(): 
            raise ValueError("El contenido es requerido.")
        if not fileName:
            raise ValueError("El nombre del archivo es requerido.")
        
        fullFilePath = os.path.join(self._router, f"{fileName}.txt")
        mode = 'a' if os.path.exists(fullFilePath) else 'w'

        with open(fullFilePath, mode) as file:
            file.write(content) 
            if append_newline:
                file.write('\n')
    
    def getDirectories(self):
        if not os.path.exists(self._router):
            raise FileNotFoundError("El directorio no existe.")
        
        files = os.listdir(self._router)
        if not files:
            raise FileNotFoundError("No se encontraron archivos.")
        return files
    
    def directoriesExist(self):
        
        if not os.path.exists(self._router):
            return False  
        return bool(os.listdir(self._router))