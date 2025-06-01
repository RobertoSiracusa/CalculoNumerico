class MyList:
    """
    Una implementación simple de una lista unidimensional.
    """
    def __init__(self):
        self._data = [] # La lista interna donde se almacenan los elementos

    def append(self, item):
        """Añade un elemento al final de la lista."""
        self._data.append(item)

    def get(self, index):
        """Obtiene el elemento en un índice específico."""
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError("Índice fuera de rango")

    def remove(self, item):
        """Elimina la primera ocurrencia de un elemento de la lista."""
        if item in self._data:
            self._data.remove(item)
        else:
            raise ValueError(f"El elemento '{item}' no está en la lista")

    def __len__(self):
        """Devuelve el número de elementos en la lista."""
        return len(self._data)

    def __str__(self):
        """Representación en cadena de la lista para impresión."""
        return str(self._data)

    def __getitem__(self, index):
        """Permite el acceso a los elementos usando corchetes (ej: my_list[0])."""
        return self.get(index)

    def __iter__(self):
        """Permite iterar sobre los elementos de la lista."""
        return iter(self._data)

    def to_list(self):
        """Devuelve la lista interna como una lista de Python estándar."""
        return self._data