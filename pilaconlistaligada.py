class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def desapilar(self):
        if self.cima is None:
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

    def esta_vacia(self):
        return self.cima is None

# Uso
p = Pila()
p.apilar("A")
p.apilar("B")
p.apilar("C")
print(p.desapilar())  # C
print(p.desapilar())  # B


# Definición del nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definición de la pila
class Pila:
    def __init__(self):
        self.cima = None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        if self.cima is None:
            print("La pila está vacía.")
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

    def peek(self):
        if self.cima is None:
            print("La pila está vacía.")
            return None
        return self.cima.dato

    def is_empty(self):
        return self.cima is None

# Uso de la pila
pila = Pila()
pila.push("A")
pila.push("B")
pila.push("C")

print("Elemento en la cima:", pila.peek())  # C

print("Desapilando:", pila.pop())  # C
print("Desapilando:", pila.pop())  # B

print("Elemento en la cima ahora:", pila.peek())  # A

print("¿Está vacía la pila?", pila.is_empty())  # False

pila.pop()  # A
print("¿Y ahora está vacía?", pila.is_empty())  # True


class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, dato):
        self.elementos.append(dato)  # Añadir al final de la lista

    def pop(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        return self.elementos.pop()  # Quita el último elemento

    def peek(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        return self.elementos[-1]  # Mira el último elemento

    def esta_vacia(self):
        return len(self.elementos) == 0

# Uso de la pila
pila = Pila()
pila.push("A")
pila.push("B")
pila.push("C")

print("Elemento en la cima:", pila.peek())  # C

print("Desapilando:", pila.pop())  # C
print("Desapilando:", pila.pop())  # B

print("Elemento en la cima ahora:", pila.peek())  # A

print("¿Está vacía la pila?", pila.esta_vacia())  # False

pila.pop()  # A
print("¿Y ahora está vacía?", pila.esta_vacia())  # True
