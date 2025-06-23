import numpy as np
from EO import OperacionesElementalesMatrices

def prueba_sistema():
    """Prueba simple del sistema de operaciones elementales"""
    
    # Crear instancia
    operaciones = OperacionesElementalesMatrices()
    
    # Crear matrices de prueba
    A = np.array([[1, 2],
                  [3, 4]], dtype=float)
    
    B = np.array([[5, 6],
                  [7, 8]], dtype=float)
    
    # Registrar matrices
    operaciones.registrar_matriz("A", A)
    operaciones.registrar_matriz("B", B)
    
    # Probar diferentes fórmulas
    formulas_test = [
        "A + B",        # Suma simple
        "2A + B",       # Escalar pegado + suma
        "A - B",        # Resta
        "3A",           # Solo escalar
        "A^T",          # Transpuesta
        "0.5A + 1.5B",  # Decimales
        "-A + B"        # Negativo
    ]
    
    print("Probando sistema de operaciones elementales...")
    print("=" * 50)
    
    resultados = {}
    
    for i, formula in enumerate(formulas_test, 1):
        print(f"Prueba {i}: {formula}")
        resultado = operaciones.evaluar_formula(formula)
        
        if resultado is not None:
            resultados[formula] = resultado
            print(f"✅ ÉXITO")
            print(f"Resultado:\n{resultado}")
        else:
            print(f"❌ ERROR")
        
        print("-" * 30)
    
    # Probar fórmula inválida
    print("Probando fórmula inválida:")
    print("Prueba: '2 + A' (escalar suelto)")
    resultado_invalido = operaciones.evaluar_formula("2 + A")
    if resultado_invalido is None:
        print("✅ CORRECTAMENTE RECHAZADA")
    else:
        print("❌ ERROR: Debería haber sido rechazada")
    
    # Guardar resultados
    mensaje = operaciones.guardar_resultados("prueba_resultados.txt")
    print(f"\n{mensaje}")
    
    print(f"\n🎯 RESUMEN:")
    print(f"- Fórmulas válidas probadas: {len(formulas_test)}")
    print(f"- Fórmulas exitosas: {len(resultados)}")
    print(f"- Fórmulas inválidas rechazadas: 1")
    print(f"- Sistema funcionando: {'✅ SÍ' if len(resultados) == len(formulas_test) else '❌ NO'}")

if __name__ == "__main__":
    prueba_sistema() 