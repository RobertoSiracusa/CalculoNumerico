import numpy as np
import os
import archiveUtil as ArchiveUtil
import regCount as regCount


def bin_to_numpy_array(file_path, file_name):

    archivo= ArchiveUtil.ArchiveUtil(file_path)
    # Obtener el archivo binario
    file_path = os.path.join(file_path, file_name)
    
    # Leer el archivo binario
    with open(file_path, 'rb') as file:
        binary_content = archivo.get_archive(file_name).read()
    
    # Decodificar el contenido binario
    decoded_content = binary_content.decode('utf-8')
    
    # Calcular dimensiones del array
    lineas = decoded_content.splitlines()
    filas = len(lineas)
    max_columnas = 0
    
    for linea in lineas:
        # Contar elementos incluso si están vacíos
        elementos = linea.split('#')
        num_elementos = len(elementos)
        if num_elementos > max_columnas:
            max_columnas = num_elementos
    
    # Crear array numpy bidimensional inicializado con "%z"
    data_array = np.full((filas, max_columnas), "%z", dtype='U256')
    
    # Llenar el array con los datos
    for i, linea in enumerate(lineas):
        elementos = linea.split('#')
        for j, elemento in enumerate(elementos):
            # Si el elemento no está vacío, reemplazar el placeholder "%z"
            if elemento:
                data_array[i, j] = elemento
    
    return data_array


# Ejemplo de uso:
if __name__ == "__main__":
    try:
        # Obtener ruta al archivo binario
        file_path = os.path.join('src', 'Storage')
        file_name = 'random_representation_numbers.bin'
        
        # Procesar archivo
        result_array = bin_to_numpy_array(file_path, file_name)
        
        # Configurar NumPy para mostrar todo sin truncar
        np.set_printoptions(threshold=np.inf, linewidth=200)
        
        # Mostrar resultados
        print("Array bidimensional resultante:")
        print(result_array)
        print(f"\nDimensiones: {result_array.shape}")
        print(f"Número total de elementos: {result_array.size}")
        
        # Mostrar contenido de forma estructurada
        print("\nContenido detallado:")
        for i in range(result_array.shape[0]):
            print(f"Fila {i}:")
            for j in range(result_array.shape[1]):
                elemento = result_array[i, j]
                print(f"  Columna {j}: {elemento}")
        print("\nAcceso a un elemento específico:")
        elemento = result_array[0, 4]  # Acceder al primer elemento de la quinta columna
        print(f"\nElemento específico (Fila 1, Columna 5): {elemento}")
    except Exception as e:
        print(f"Error: {e}")


