class Matriz:
    def __init__(self, datos):
        self.datos = datos
        self.dimension = len(datos)
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, fila)) for fila in self.datos])
    
    def __add__(self, otra):
        if isinstance(otra, Matriz):
            if self.dimension != otra.dimension:
                raise ValueError("Dimensiones incompatibles")
            resultado = []
            for i in range(self.dimension):
                fila = [self.datos[i][j] + otra.datos[i][j] for j in range(self.dimension)]
                resultado.append(fila)
            return Matriz(resultado)
        elif isinstance(otra, int):
            resultado = [[self.datos[i][j] + otra for j in range(self.dimension)] for i in range(self.dimension)]
            return Matriz(resultado)
        raise TypeError("Tipo no soportado")
    
    def __sub__(self, otra):
        if isinstance(otra, Matriz):
            if self.dimension != otra.dimension:
                raise ValueError("Dimensiones incompatibles")
            resultado = []
            for i in range(self.dimension):
                fila = [self.datos[i][j] - otra.datos[i][j] for j in range(self.dimension)]
                resultado.append(fila)
            return Matriz(resultado)
        elif isinstance(otra, int):
            resultado = [[self.datos[i][j] - otra for j in range(self.dimension)] for i in range(self.dimension)]
            return Matriz(resultado)
        raise TypeError("Tipo no soportado")
    
    def __mul__(self, otra):
        if isinstance(otra, Matriz):
            if self.dimension != otra.dimension:
                raise ValueError("Dimensiones incompatibles")
            resultado = [[0]*self.dimension for _ in range(self.dimension)]
            for i in range(self.dimension):
                for j in range(self.dimension):
                    for k in range(self.dimension):
                        resultado[i][j] += self.datos[i][k] * otra.datos[k][j]
            return Matriz(resultado)
        elif isinstance(otra, int):
            resultado = [[self.datos[i][j] * otra for j in range(self.dimension)] for i in range(self.dimension)]
            return Matriz(resultado)
        raise TypeError("Tipo no soportado")
    
    def __rmul__(self, escalar):
        return self * escalar
    
    def __rsub__(self, escalar):
        resultado = [[escalar - self.datos[i][j] for j in range(self.dimension)] for i in range(self.dimension)]
        return Matriz(resultado)
    
    def __radd__(self, escalar):
        return self + escalar

class Ecuacion:
    def __init__(self, expresion):
        self.expresion = expresion
    
    def evaluar(self, matrizA, matrizB):
        try:
            expr = self.expresion.replace('[', '').replace(']', '')
            return eval(expr, {'A': matrizA, 'B': matrizB})
        except Exception:
            return None

def leerMatriz(nombreArchivo):
    try:
        with open(nombreArchivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        datos = []
        for linea in lineas:
            linea = linea.strip()
            if linea:
                numeros = [int(x) for x in linea.split('#')]
                datos.append(numeros)
        return Matriz(datos)
    except Exception:
        return None

def main():
    matrizA = leerMatriz('matrizA.bin')
    matrizB = leerMatriz('matrizB.bin')
    
    if matrizA is None or matrizB is None:
        print("Error: Archivos de matriz inválidos")
        return
    
    try:
        with open('ecuaciones.bin', 'r', encoding='utf-8') as f:
            ecuaciones = [linea.strip() for linea in f.readlines()]
    except Exception:
        print("Error: Archivo de ecuaciones inválido")
        return
    
    for i, expr in enumerate(ecuaciones[:5], 1):
        ecuacion = Ecuacion(expr)
        resultado = ecuacion.evaluar(matrizA, matrizB)
        
        print(f"\nEcuación {i}: {expr}")
        if resultado is None:
            print("No se puede realizar")
        elif isinstance(resultado, Matriz):
            print("Resultado:\n" + str(resultado))
        else:
            print("Resultado:", resultado)

if __name__ == "__main__":
    main()