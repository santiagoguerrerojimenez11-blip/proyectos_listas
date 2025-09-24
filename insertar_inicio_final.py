class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class ListaEnlazada:
    def __init__(self):
        self.cab = None

    def insertar_varios_inicio(self, datos):
        for dato in datos:
            nuevo = Nodo(dato)
            nuevo.sig = self.cab
            self.cab = nuevo

    def insertar_varios_final(self, datos):
        for dato in datos:
            nuevo = Nodo(dato)
            if self.cab is None:
                self.cab = nuevo
            else:
                actual = self.cab
                while actual.sig:
                    actual = actual.sig
                actual.sig = nuevo

    def mostrar(self):
        actual = self.cab
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.sig
        print("None")

lista = ListaEnlazada()
lista.insertar_varios_inicio([1, 2, 3])
lista.mostrar()
lista.insertar_varios_final([4, 5, 6])
lista.mostrar()
