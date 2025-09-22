#lista simple - Santiago Guerrero Jimenez

class Nodo:
    def __init__(self,dato):
        self.dato = dato  
        self.siguiente = None

class Lista_enlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self,dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato,end="-->")
            actual = actual.siguiente
        print("None")            

lista = Lista_enlazada()
lista.insertar_inicio("c")
lista.insertar_inicio("b")
lista.insertar_inicio("a")
print("lista enlazada simple ")
lista.mostrar()