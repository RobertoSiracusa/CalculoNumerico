import random

def generar_archivo_bin_aleatorio(nombre_archivo="numeros_aleatorios.bin"):
    """
    Genera un archivo .bin con números aleatorios en base decimal, binaria y hexadecimal.

    El archivo tendrá exactamente 10 líneas.
    Cada línea contendrá una cantidad aleatoria de números (entre 1 y 10),
    y cada número será distinto dentro de su línea.
    El formato para separar cada número es NNNNNNNN#NNNNNNN#NNNNNN, donde N son las cifras.
    """
    num_lineas_fijas = 1000
    max_numeros_por_linea = 1000

    with open(nombre_archivo, "wb") as f:
        for _ in range(num_lineas_fijas):  # Se generan exactamente 10 líneas
            linea_numeros = []
            numeros_generados_en_linea = set()  # Para asegurar números distintos por línea

            # La cantidad de números por línea es aleatoria (entre 1 y max_numeros_por_linea)
            cantidad_numeros_actual = random.randint(1, max_numeros_por_linea)

            while len(linea_numeros) < cantidad_numeros_actual:
                # Generar número aleatorio (ejemplo: entre 0 y 255 para simplicidad)
                # Puedes ajustar el rango si necesitas números más grandes
                num_decimal = random.randint(0, 255)

                if num_decimal not in numeros_generados_en_linea:
                    numeros_generados_en_linea.add(num_decimal)

                    # Formatear a binario (8 bits) y hexadecimal (2 dígitos)
                    num_binario = format(num_decimal, '08b')
                    num_hexadecimal = format(num_decimal, '02X')

                    # Unir los formatos con el separador '#'
                    numero_formateado = f"{num_decimal}#{num_binario}#{num_hexadecimal}"
                    linea_numeros.append(numero_formateado)

            # Unir todos los números formateados en la línea con '#' y añadir un salto de línea
            linea_str = "#".join(linea_numeros) + "\n"
            # Escribir la línea codificada en bytes al archivo
            f.write(linea_str.encode('utf-8'))

    print(f"Archivo '{nombre_archivo}' generado exitosamente con {num_lineas_fijas} líneas.")



### Ejemplo de Uso



if __name__ == "__main__":
    generar_archivo_bin_aleatorio("mis_numeros_variados.bin")