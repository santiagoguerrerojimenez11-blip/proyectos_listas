class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_final(self, dato):
        if self.cabeza is None:
            nuevo = Nodo(dato)
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        nuevo = Nodo(dato)
        actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end="-->")
            actual = actual.siguiente
        print("None")


lista = ListaEnlazada()
lista.insertar_inicio("a")
lista.insertar_inicio("b")
lista.insertar_final("c")
lista.insertar_final("d")
lista.mostrar()
