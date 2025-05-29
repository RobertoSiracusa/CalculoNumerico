import struct

def generate_binary_file(filename="numbers.bin"):
    """
    Generates a binary file named 'numbers.bin' with 10 lines,
    each containing 10 four-digit decimal numbers separated by '#'.
    """
    with open(filename, 'wb') as f:
        for _ in range(10):  # 10 lines
            line_bytes = b""
            for i in range(10):  # 10 numbers per line
                # Generate a 4-digit number (0000-9999)
                # You can modify this to generate random numbers or specific sequences
                number = i * 100 + _ * 10 + 1 # Example: 0001, 0011, 0021... up to 9991
                if number > 9999: # Ensure number stays within 4 digits
                    number = number % 10000

                # Format the number as a 4-digit string and encode it
                line_bytes += f"{number:04d}".encode('ascii')

                if i < 9: # Add '#' delimiter between numbers
                    line_bytes += b'#'
            
            line_bytes += b'\n' # Add newline character at the end of each line
            f.write(line_bytes)
    print(f"File '{filename}' created successfully.")

# Run the function to create the file
generate_binary_file()

def contar_cifras_significativas(numero_str):
    """
    Cuenta el número de cifras significativas en una cadena de número.
    Asume que la cadena es un número entero con posibles ceros a la izquierda.
    Los ceros a la izquierda no se consideran significativos.
    """
    numero_limpio = numero_str.lstrip('0') # Elimina los ceros a la izquierda
    
    if not numero_limpio: # Si el número_limpio está vacío (ej. "0000"), significa que el número original era 0
        return 1 # El número 0 tiene una cifra significativa (el mismo cero)
    else:
        return len(numero_limpio) # La longitud de la cadena sin ceros a la izquierda es el número de cifras significativas

def leer_y_analizar_bin(nombre_archivo="numeros.bin"):
    """
    Lee el archivo binario generado, extrae los números y cuenta sus cifras significativas.
    """
    try:
        with open(nombre_archivo, 'rb') as f:
            contenido_bytes = f.read()
            contenido_str = contenido_bytes.decode('utf-8') # Decodifica los bytes a una cadena UTF-8

            lineas = contenido_str.strip().split('\n') # Divide el contenido en líneas

            resultados = []
            for i, linea in enumerate(lineas):
                numeros_en_linea = linea.split('#') # Divide la línea en números usando '#' como delimitador
                # El último split puede generar una cadena vacía si la línea termina en '#',
                # así que la filtramos. Si tu generador no deja el último '#' en la línea,
                # puedes quitar el filtro `filter(None, ...)`
                numeros_en_linea = list(filter(None, numeros_en_linea)) 

                for j, num_str in enumerate(numeros_en_linea):
                    cifras = contar_cifras_significativas(num_str)
                    resultados.append({
                        'linea': i + 1,
                        'posicion_en_linea': j + 1,
                        'numero_original': num_str,
                        'cifras_significativas': cifras
                    })
        return resultados

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al leer o procesar el archivo: {e}")
        return []

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Asegúrate de que el archivo 'numeros.bin' exista en el mismo directorio
    # donde ejecutas este script, o proporciona la ruta completa al archivo.
    
    # Primero, puedes usar el código del ejemplo anterior para crear el archivo:
    # from generador_bin import generar_archivo_bin
    # generar_archivo_bin() # Esto generará numeros.bin si aún no lo tienes

    analisis = leer_y_analizar_bin("numeros.bin")

    if analisis:
        print("\nAnálisis de cifras significativas:")
        for resultado in analisis:
            print(f"Línea {resultado['linea']}, Posición {resultado['posicion_en_linea']}: "
                  f"Número '{resultado['numero_original']}' tiene {resultado['cifras_significativas']} cifras significativas.")