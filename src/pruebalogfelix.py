#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para demostrar el sistema de logging de errores
Creado por: Felix
Propósito: Mostrar cómo se capturan y guardan errores en archivos .log
"""

from Repositories.archiveUtil import ArchiveUtil

def probar_errores_con_logging():
    """
    Función que prueba diferentes tipos de errores y demuestra 
    cómo se registran en el archivo .log
    """
    print("🔍 INICIANDO PRUEBAS DE SISTEMA DE ERRORES CON LOGGING")
    print("=" * 60)
    
    try:
        # Crear instancia con directorio válido
        archive_util = ArchiveUtil("./Storage")
        print("✅ ArchiveUtil creado correctamente")
        
        # PRUEBA 1: Error por archivo inexistente
        print("\n📁 PRUEBA 1: Intentar abrir archivo inexistente")
        try:
            archivo = archive_util.getArchive("archivo_que_no_existe.txt")
        except FileNotFoundError as e:
            print(f"❌ Error capturado: {e}")
            print("💾 Error registrado en PruebaErrorSystem.log")
        
        # PRUEBA 2: Error por nombre de archivo vacío
        print("\n📝 PRUEBA 2: Intentar abrir archivo con nombre vacío")
        try:
            archivo = archive_util.getArchive("")
        except ValueError as e:
            print(f"❌ Error capturado: {e}")
            print("💾 Error registrado en PruebaErrorSystem.log")
        
        # PRUEBA 3: Error por contenido vacío
        print("\n📄 PRUEBA 3: Intentar crear archivo con contenido vacío")
        try:
            archive_util.setCreateArchive("", "test_file")
        except ValueError as e:
            print(f"❌ Error capturado: {e}")
            print("💾 Error registrado en PruebaErrorSystem.log")
        
        # PRUEBA 4: Crear archivo exitoso (sin error)
        print("\n✨ PRUEBA 4: Crear archivo exitosamente")
        archive_util.setCreateArchive(
            "Contenido de prueba exitoso", 
            "archivo_exitoso", 
            append_newline=True
        )
        print("✅ Archivo creado exitosamente: archivo_exitoso.txt")
        
        # PRUEBA 5: Generar nombre de archivo único
        print("\n🎲 PRUEBA 5: Generar nombre de archivo único")
        nombre_unico = archive_util.utilitaryNameArchive()
        print(f"📋 Nombre generado: {nombre_unico}")
        
        print("\n🎉 TODAS LAS PRUEBAS COMPLETADAS")
        print("📋 Revisa el archivo: src/Storage/PruebaErrorSystem.log")
        print("   para ver todos los errores registrados")
        
    except Exception as e:
        print(f"💥 Error inesperado: {e}")

def mostrar_archivo_log():
    """
    Función para mostrar el contenido del archivo de log
    """
    print("\n" + "=" * 60)
    print("📖 CONTENIDO DEL ARCHIVO DE LOG:")
    print("=" * 60)
    
    try:
        log_path = "Storage/PruebaErrorSystem.log"
        with open(log_path, 'r', encoding='utf-8') as file:
            contenido = file.read()
            if contenido:
                print(contenido)
            else:
                print("📝 El archivo de log está vacío")
    except FileNotFoundError:
        print("❌ No se encontró el archivo de log")
    except Exception as e:
        print(f"❌ Error al leer el archivo de log: {e}")

if __name__ == "__main__":
    # Ejecutar las pruebas
    probar_errores_con_logging()
    
    # Mostrar el archivo de log generado
    mostrar_archivo_log()
