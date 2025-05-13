# Nodo individual
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Lista ligada
class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")


a = ListaLigada()
a.agregar_al_final(4)
a.agregar_al_final(5)
a.agregar_al_final(8)
a.imprimir()

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaLigada()
lista.insertar(8)
lista.insertar(6)
lista.insertar(9)
lista.recorrer()  # A -> B -> C -> None
