import os
from datetime import datetime
import random

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
            error_msg = "El directorio a guardar no existe."
            # Solo hacer log si _router ya está inicializado (evitar recursión en constructor)
            if hasattr(self, '_router') and self._router:
                self._logError("FileNotFoundError", error_msg, router)
            raise FileNotFoundError(error_msg)
        self._router = router
    
    def getArchive(self, fileName):
        if not fileName or not fileName.strip():
            error_msg = "El nombre del archivo es requerido."
            self._logError("ValueError", error_msg, fileName)
            raise ValueError(error_msg)
        
        fullFilePath = os.path.join(self._router, fileName)
        if not os.path.isfile(fullFilePath):
            error_msg = "El archivo no se encontro en el directorio especificado."
            self._logError("FileNotFoundError", error_msg, fileName, fullFilePath)
            raise FileNotFoundError(error_msg)
        
        return open(fullFilePath, 'rb')
    
    def setCreateArchive(self, content, fileName, append_newline=False, booleano=True):
        
        if not content or not content.strip(): 
            error_msg = "El contenido es requerido."
            # Solo hacer log si no estamos ya en proceso de logging (evitar recursión infinita)
            if booleano or not hasattr(self, '_logging_in_progress'):
                self._logging_in_progress = True
                self._logError("ValueError", error_msg, fileName)
                delattr(self, '_logging_in_progress')
            raise ValueError(error_msg)
        if not fileName:
            error_msg = "El nombre del archivo es requerido."
            if booleano or not hasattr(self, '_logging_in_progress'):
                self._logging_in_progress = True
                self._logError("ValueError", error_msg, fileName)
                delattr(self, '_logging_in_progress')
            raise ValueError(error_msg)

        if booleano == True:
            fullFilePath = os.path.join(self._router, f"{fileName}.txt")
        else:
            # Usar la carpeta Storage existente en lugar de crear src/Storage
            storage_dir = "Storage"
            if not os.path.exists(storage_dir):
                os.makedirs(storage_dir)
            fullFilePath = os.path.join(storage_dir, "PruebaErrorSystem.log")
        
        mode = 'a' if os.path.exists(fullFilePath) else 'w'

        with open(fullFilePath, mode) as file:
            file.write(content) 
            if append_newline:
                file.write('\n')
    
    def getDirectories(self):
        if not os.path.exists(self._router):
            error_msg = "El directorio no existe."
            self._logError("FileNotFoundError", error_msg, self._router)
            raise FileNotFoundError(error_msg)
        
        files = os.listdir(self._router)
        if not files:
            error_msg = "No se encontraron archivos."
            self._logError("FileNotFoundError", error_msg, self._router)
            raise FileNotFoundError(error_msg)
        return files
    
    def directoriesExist(self):
        
        if not os.path.exists(self._router):
            return False  
        return bool(os.listdir(self._router))
    
    def utilitaryNameArchive(self):
        currentDateTime = datetime.now()
        formattedDateTime = currentDateTime.strftime("%Y-%m-%d_%H-%M-%S")
        randNum = random.randint(1, 99)
        return f"ErrorSystemValues{formattedDateTime}_serial{randNum}"
    
    def _logError(self, error_type, error_message, fileName=None, fullPath=None):
        """
        Método privado para registrar errores en archivo .log
        """
        try:
            # Crear timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Formatear mensaje de error
            log_entry = f"[{timestamp}] ERROR - {error_type}\n"
            log_entry += f"  Mensaje: {error_message}\n"
            
            if fileName:
                log_entry += f"  Archivo solicitado: {fileName}\n"
            if fullPath:
                log_entry += f"  Ruta completa: {fullPath}\n"
            
            log_entry += f"  Directorio de trabajo: {self._router}\n"
            log_entry += "-" * 50 + "\n"
            
            # Guardar en archivo .log usando setCreateArchive con booleano=False
            self.setCreateArchive(log_entry, "unused_name", append_newline=True, booleano=False)
            
        except Exception as log_exception:
            # Si falla el logging, no queremos que rompa la funcionalidad principal
            print(f"Warning: No se pudo registrar el error en el log: {log_exception}")