import numpy as np
from EO import OperacionesElementalesMatrices

def test_sistema_limpio():
    """Test del sistema refactorizado - solo True/False"""
    
    # Inicializar sistema
    sistema = OperacionesElementalesMatrices()
    
    # Crear matrices de prueba
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.array([[2, 0], [1, 3]])
    
    print("=== PRUEBA DEL SISTEMA LIMPIO ===")
    print("Solo retorna True/False - SIN imprimir resultados\n")
    
    # Registrar matrices
    print("1. REGISTRANDO MATRICES:")
    print(f"   Matriz A: {sistema.registrar_matriz('A', A)}")
    print(f"   Matriz B: {sistema.registrar_matriz('B', B)}")
    print(f"   Matriz C: {sistema.registrar_matriz('C', C)}")
    
    # Probar operaciones individuales
    print("\n2. OPERACIONES INDIVIDUALES:")
    print(f"   A + B funciona: {sistema.suma_matrices(A, B)}")
    print(f"   A - B funciona: {sistema.resta_matrices(A, B)}")
    print(f"   2 * A funciona: {sistema.multiplicacion_escalar(A, 2)}")
    print(f"   A * B funciona: {sistema.multiplicacion_matrices(A, B)}")
    print(f"   A^T funciona: {sistema.transpuesta(A)}")
    
    # Probar fórmulas válidas
    print("\n3. FÓRMULAS VÁLIDAS:")
    formulas_validas = [
        "2A + B",
        "A + B - C", 
        "A^T",
        "3A + 2B",
        "-A + B"
    ]
    
    for formula in formulas_validas:
        resultado = sistema.validar_formula(formula)
        print(f"   '{formula}': {resultado}")
    
    # Probar fórmulas inválidas
    print("\n4. FÓRMULAS INVÁLIDAS:")
    formulas_invalidas = [
        "A + 2",     # Escalar suelto
        "2 + A",     # Escalar suelto
        "A + D",     # Matriz no registrada
        "A * Z",     # Matriz no registrada
        ""           # Fórmula vacía
    ]
    
    for formula in formulas_invalidas:
        resultado = sistema.validar_formula(formula)
        print(f"   '{formula}': {resultado}")
    
    # Info del sistema
    print(f"\n5. INFO DEL SISTEMA:")
    info = sistema.obtener_info_sistema()
    print(f"   Matrices registradas: {info['matrices_registradas']}")
    print(f"   Nombres: {info['nombres_matrices']}")
    
    print("\n=== TODAS LAS OPERACIONES SE EJECUTARON INTERNAMENTE ===")
    print("¡No se imprimió ningún resultado de las operaciones!")

if __name__ == "__main__":
    test_sistema_limpio() 