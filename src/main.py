import NumSF


def read_bin_file_to_2d_array(file_name=""):

    all_lines_numbers = []
    try:
        with open(file_name, "rb") as f:
            for line_bytes in f:

                line_str = line_bytes.decode('utf-8').strip()
                

                numbers_in_line = line_str.split('#')
                
                all_lines_numbers.append(numbers_in_line)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

    return all_lines_numbers

def operarArray(array_2d):
    if array_2d !=None and len(array_2d) > 0:
        for i, line in enumerate(array_2d):
            for j, number_str in enumerate(line):
                object = NumSF.NumSF(number_str)
                try:
                    print(f"Línea {i+1}, Número {j+1}: {number_str} - Cifras Significativas: {object.cifras_significativas()}, Sistema: {object.numSistem}, Operaciones: {object.numOperaciones}")
                except ValueError as ve:
                    print(f"Línea {i+1}, Número {j+1}: Error - {ve}")

    else:
        print("El array de datos está vacío. No hay números para procesar.")

def main():
    file_name = "random_representation_numbers.bin"
    array_2d = read_bin_file_to_2d_array(file_name)
    
    if array_2d:
        print(f"Archivo '{file_name}' leído correctamente. Procesando números...")
        operarArray(array_2d)
    else:
        print("No se encontraron números para procesar.")

main()