def leer_archivo_bin_a_array(
    nombre_archivo="numeros_aleatorios.bin",
    max_numeros_por_linea=10
):
    """
    Lee un archivo .bin generado por la función anterior y lo guarda en
    un array bidimensional de strings.

    Args:
        nombre_archivo (str): El nombre del archivo .bin a leer.
        max_numeros_por_linea (int): El número máximo de elementos que puede tener una línea.
                                     Se usará para rellenar con "null" si hay menos.

    Returns:
        list[list[str]]: Un array bidimensional (lista de listas) donde cada sublista
                         representa una línea del archivo, con cada número formateado
                         como un string. Las posiciones vacías se rellenan con "null".
                         Retorna una lista vacía si el archivo no se encuentra o está vacío.
    """
    datos_leidos = []

    try:
        with open(nombre_archivo, "rb") as f:
            for linea_bytes in f:
                # Decodificar la línea de bytes a string (usando utf-8 como se codificó)
                linea_str = linea_bytes.decode('utf-8').strip() # .strip() para quitar el '\n'

                if not linea_str: # Ignorar líneas vacías si las hubiera
                    continue

                # Dividir la línea por el separador de números '#'
                numeros_en_linea = linea_str.split('#')

                # La longitud esperada de cada número es 3 componentes: decimal, binario, hexadecimal
                # Entonces, cada "bloque" de número tiene 3 partes.
                # Dividimos por 3 para obtener la cantidad real de "números" completos.
                cantidad_bloques_reales = len(numeros_en_linea) // 3

                # Crear una nueva lista para la línea actual
                fila_actual = []

                # Iterar sobre los bloques de números reales
                for i in range(cantidad_bloques_reales):
                    # Unir los 3 componentes (decimal, binario, hexadecimal) de nuevo con '#'
                    # para mantener el formato original NNNNNNNN#NNNNNNN#NNNNNN
                    bloque_numero = "#".join(numeros_en_linea[i*3 : (i*3)+3])
                    fila_actual.append(bloque_numero)

                # Rellenar con "null" si la línea tiene menos números de lo esperado
                while len(fila_actual) < max_numeros_por_linea:
                    fila_actual.append("null")

                datos_leidos.append(fila_actual)

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []

    return datos_leidos

