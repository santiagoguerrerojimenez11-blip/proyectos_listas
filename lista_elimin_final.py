class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class lista_enlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def eliminar_final(self):
        if self.cabeza is None:
            return None
        if self.cabeza.siguiente is None:
            eliminado = self.cabeza.dato
            self.cabeza = None
            return eliminado
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
        eliminado = actual.siguiente.dato
        actual.siguiente = None
        return eliminado

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end="-->")
            actual = actual.siguiente
        print("None")

lista = lista_enlazada()
lista.insertar_inicio("c")
lista.insertar_inicio("b")
lista.insertar_inicio("a")
print("lista original")
lista.mostrar()
print("mostrar lista eliminando al final ")
lista.eliminar_final()
lista.mostrar()

    
    