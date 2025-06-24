"""
PROXY - Este archivo mantiene compatibilidad con código existente
La implementación real ahora está en src/OperacionesElementales/
"""
import sys
import os
import importlib.util

# Obtener la ruta al archivo EO.py en src/OperacionesElementales/
src_eo_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'OperacionesElementales', 'EO.py')
src_eo_path = os.path.abspath(src_eo_path)

# Cargar el módulo desde el path específico
spec = importlib.util.spec_from_file_location("src_eo", src_eo_path)
src_eo_module = importlib.util.module_from_spec(spec)

# Agregar rutas necesarias para las dependencias
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'OperacionesElementales'))

# Ejecutar el módulo para cargarlo
spec.loader.exec_module(src_eo_module)

# Importar la clase desde el módulo cargado
_OperacionesElementalesMatrices = src_eo_module.OperacionesElementalesMatrices

# Crear alias para mantener compatibilidad
class OperacionesElementalesMatrices(_OperacionesElementalesMatrices):
    """
    PROXY - Mantiene compatibilidad con código existente
    Todas las funcionalidades están implementadas en src/OperacionesElementales/
    """
    pass
