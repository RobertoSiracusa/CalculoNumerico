import os

class ArchiveUtil:
    def __init__(self, router=""):
        if not router or not router.strip():
            raise ValueError("La ruta asignada no es válida.")
        self._router = None
        self._util_directory(router)
    
    @property
    def router(self):
        return self._router
    
    @router.setter
    def router(self, new_router):
        self._util_directory(new_router)
    
    def _util_directory(self, router):
        if not os.path.exists(router):
            raise FileNotFoundError("El directorio a guardar no existe.")
        self._router = router
    
    def get_archive(self, name_archive):
        if not name_archive or not name_archive.strip():
            raise ValueError("EL nombre del archivo es requerido.")
        
        full_path = os.path.join(self._router, name_archive)
        if not os.path.isfile(full_path):
            raise FileNotFoundError("El archivo no se encontró en el directorio especificado.")
        
        return open(full_path, 'rb')
    
    def set_create_archive(self, content, name_archive, append_newline=False):
        
        if not content or not content.strip(): 
            raise ValueError("El contenido es requerido.")
        if not name_archive:
            raise ValueError("El nombre del archivo es requerido.")
        
        full_path = os.path.join(self._router, f"{name_archive}.txt")
        mode = 'a' if os.path.exists(full_path) else 'w'

        with open(full_path, mode) as file:
            file.write(content) 
            if append_newline:
                file.write('\n')
    
    def get_directories(self):
        if not os.path.exists(self._router):
            raise FileNotFoundError("El directorio no existe.")
        
        files = os.listdir(self._router)
        if not files:
            raise FileNotFoundError("No se encontraron archivos.")
        return files
    
    def directories_exist(self):
        
        if not os.path.exists(self._router):
            return False  
        return bool(os.listdir(self._router))