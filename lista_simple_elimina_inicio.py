
class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class lista_enlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self,dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def eliminar_inicio(self):
        if self.cabeza is None:  #si la lista esta vacia
            print("no hay nada que eliminar")
            return
        self.cabeza = self.cabeza.siguiente #la cabeza salta al siguiente nodo

    def mostrar(self):
        actual = self.cabeza
        while actual :
            print(actual.dato,end="-->")
            actual = actual.siguiente
        print("None")             

lista = lista_enlazada()
lista.insertar_inicio("c")
lista.insertar_inicio("b")
lista.insertar_inicio("a")
print("lista original")
lista.mostrar()

lista.eliminar_inicio()
print("lista eliminando el inicio")
lista.mostrar()