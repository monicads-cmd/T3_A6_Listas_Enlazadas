class Nodo:
    """Clase base para un nodo"""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaSimples:
    """Lista simplemente enlazada"""
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamanio += 1
    
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamanio += 1
    
    def insertar_posicion(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            print("Posición inválida")
            return
        
        if posicion == 0:
            self.insertar_inicio(dato)
        else:
            nuevo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            self.tamanio += 1
    
    def eliminar_valor(self, dato):
        if self.esta_vacia():
            print("Lista vacía")
            return False
        
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            self.tamanio -= 1
            return True
        
        print("Elemento no encontrado")
        return False
    
    def eliminar_posicion(self, posicion):
        if self.esta_vacia() or posicion < 0 or posicion >= self.tamanio:
            print("Posición inválida o lista vacía")
            return None
        
        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
            return dato
        
        actual = self.cabeza
        for _ in range(posicion - 1):
            actual = actual.siguiente
        
        dato = actual.siguiente.dato
        actual.siguiente = actual.siguiente.siguiente
        self.tamanio -= 1
        return dato
    
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1
    
    def mostrar(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" → ".join(elementos) + " → None")


class ListaDoble:
    """Lista doblemente enlazada"""
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1
    
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1
    
    def insertar_posicion(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            print("Posición inválida")
            return
        
        if posicion == 0:
            self.insertar_inicio(dato)
        elif posicion == self.tamanio:
            self.insertar_final(dato)
        else:
            nuevo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            
            nuevo.anterior = actual.anterior
            nuevo.siguiente = actual
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio += 1
    
    def eliminar_valor(self, dato):
        if self.esta_vacia():
            print("Lista vacía")
            return False
        
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                
                self.tamanio -= 1
                return True
            actual = actual.siguiente
        
        print("Elemento no encontrado")
        return False
    
    def eliminar_posicion(self, posicion):
        if self.esta_vacia() or posicion < 0 or posicion >= self.tamanio:
            print("Posición inválida o lista vacía")
            return None
        
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        
        dato = actual.dato
        
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        else:
            self.cola = actual.anterior
        
        self.tamanio -= 1
        return dato
    
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1
    
    def mostrar(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        
        print("Recorrido hacia adelante:")
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("None ↔ " + " ↔ ".join(elementos) + " ↔ None")
        
        print("Recorrido hacia atrás:")
        actual = self.cola
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.anterior
        print("None ↔ " + " ↔ ".join(elementos) + " ↔ None")


class ListaCircular:
    """Lista circular simplemente enlazada"""
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            nuevo.siguiente = self.cabeza
            actual.siguiente = nuevo
            self.cabeza = nuevo
        self.tamanio += 1
    
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            nuevo.siguiente = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza
        self.tamanio += 1
    
    def insertar_posicion(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            print("Posición inválida")
            return
        
        if posicion == 0:
            self.insertar_inicio(dato)
        else:
            nuevo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            self.tamanio += 1
    
    def eliminar_valor(self, dato):
        if self.esta_vacia():
            print("Lista vacía")
            return False
        
        if self.cabeza.dato == dato:
            if self.cabeza.siguiente == self.cabeza:
                self.cabeza = None
            else:
                actual = self.cabeza
                while actual.siguiente != self.cabeza:
                    actual = actual.siguiente
                actual.siguiente = self.cabeza.siguiente
                self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente != self.cabeza and actual.siguiente.dato != dato:
            actual = actual.siguiente
        
        if actual.siguiente.dato == dato:
            actual.siguiente = actual.siguiente.siguiente
            self.tamanio -= 1
            return True
        
        print("Elemento no encontrado")
        return False
    
    def eliminar_posicion(self, posicion):
        if self.esta_vacia() or posicion < 0 or posicion >= self.tamanio:
            print("Posición inválida o lista vacía")
            return None
        
        if posicion == 0:
            dato = self.cabeza.dato
            if self.tamanio == 1:
                self.cabeza = None
            else:
                actual = self.cabeza
                while actual.siguiente != self.cabeza:
                    actual = actual.siguiente
                actual.siguiente = self.cabeza.siguiente
                self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
            return dato
        
        actual = self.cabeza
        for _ in range(posicion - 1):
            actual = actual.siguiente
        
        dato = actual.siguiente.dato
        actual.siguiente = actual.siguiente.siguiente
        self.tamanio -= 1
        return dato
    
    def buscar(self, dato):
        if self.esta_vacia():
            return -1
        
        actual = self.cabeza
        posicion = 0
        while True:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
            if actual == self.cabeza:
                break
        return -1
    
    def mostrar(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        
        actual = self.cabeza
        elementos = []
        while True:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print(" → ".join(elementos) + " → (vuelve al inicio)")


def menu_lista_simples():
    lista = ListaSimples()
    while True:
        print("\n" + "="*50)
        print("LISTA SIMPLEMENTE ENLAZADA")
        print("="*50)
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Insertar en posición")
        print("4. Eliminar por valor")
        print("5. Eliminar por posición")
        print("6. Buscar elemento")
        print("7. Mostrar lista")
        print("8. Tamaño de la lista")
        print("9. Volver al menú principal")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            dato = input("Ingrese el dato: ")
            lista.insertar_inicio(dato)
            print("Elemento insertado al inicio")
        elif opcion == '2':
            dato = input("Ingrese el dato: ")
            lista.insertar_final(dato)
            print("Elemento insertado al final")
        elif opcion == '3':
            dato = input("Ingrese el dato: ")
            try:
                pos = int(input("Ingrese la posición: "))
                lista.insertar_posicion(dato, pos)
            except ValueError:
                print("Posición inválida")
        elif opcion == '4':
            dato = input("Ingrese el dato a eliminar: ")
            if lista.eliminar_valor(dato):
                print("Elemento eliminado")
        elif opcion == '5':
            try:
                pos = int(input("Ingrese la posición a eliminar: "))
                dato = lista.eliminar_posicion(pos)
                if dato:
                    print(f"Elemento eliminado: {dato}")
            except ValueError:
                print("Posición inválida")
        elif opcion == '6':
            dato = input("Ingrese el dato a buscar: ")
            pos = lista.buscar(dato)
            if pos != -1:
                print(f"Elemento encontrado en la posición {pos}")
            else:
                print("Elemento no encontrado")
        elif opcion == '7':
            lista.mostrar()
        elif opcion == '8':
            print(f"Tamaño de la lista: {lista.tamanio}")
        elif opcion == '9':
            break
        else:
            print("Opción inválida")


def menu_lista_doble():
    lista = ListaDoble()
    while True:
        print("\n" + "="*50)
        print("LISTA DOBLEMENTE ENLAZADA")
        print("="*50)
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Insertar en posición")
        print("4. Eliminar por valor")
        print("5. Eliminar por posición")
        print("6. Buscar elemento")
        print("7. Mostrar lista")
        print("8. Tamaño de la lista")
        print("9. Volver al menú principal")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            dato = input("Ingrese el dato: ")
            lista.insertar_inicio(dato)
            print("Elemento insertado al inicio")
        elif opcion == '2':
            dato = input("Ingrese el dato: ")
            lista.insertar_final(dato)
            print("Elemento insertado al final")
        elif opcion == '3':
            dato = input("Ingrese el dato: ")
            try:
                pos = int(input("Ingrese la posición: "))
                lista.insertar_posicion(dato, pos)
            except ValueError:
                print("Posición inválida")
        elif opcion == '4':
            dato = input("Ingrese el dato a eliminar: ")
            if lista.eliminar_valor(dato):
                print("Elemento eliminado")
        elif opcion == '5':
            try:
                pos = int(input("Ingrese la posición a eliminar: "))
                dato = lista.eliminar_posicion(pos)
                if dato:
                    print(f"Elemento eliminado: {dato}")
            except ValueError:
                print("Posición inválida")
        elif opcion == '6':
            dato = input("Ingrese el dato a buscar: ")
            pos = lista.buscar(dato)
            if pos != -1:
                print(f"Elemento encontrado en la posición {pos}")
            else:
                print("Elemento no encontrado")
        elif opcion == '7':
            lista.mostrar()
        elif opcion == '8':
            print(f"Tamaño de la lista: {lista.tamanio}")
        elif opcion == '9':
            break
        else:
            print("Opción inválida")


def menu_lista_circular():
    lista = ListaCircular()
    while True:
        print("\n" + "="*50)
        print("LISTA CIRCULAR")
        print("="*50)
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Insertar en posición")
        print("4. Eliminar por valor")
        print("5. Eliminar por posición")
        print("6. Buscar elemento")
        print("7. Mostrar lista")
        print("8. Tamaño de la lista")
        print("9. Volver al menú principal")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            dato = input("Ingrese el dato: ")
            lista.insertar_inicio(dato)
            print("Elemento insertado al inicio")
        elif opcion == '2':
            dato = input("Ingrese el dato: ")
            lista.insertar_final(dato)
            print("Elemento insertado al final")
        elif opcion == '3':
            dato = input("Ingrese el dato: ")
            try:
                pos = int(input("Ingrese la posición: "))
                lista.insertar_posicion(dato, pos)
            except ValueError:
                print("Posición inválida")
        elif opcion == '4':
            dato = input("Ingrese el dato a eliminar: ")
            if lista.eliminar_valor(dato):
                print("Elemento eliminado")
        elif opcion == '5':
            try:
                pos = int(input("Ingrese la posición a eliminar: "))
                dato = lista.eliminar_posicion(pos)
                if dato:
                    print(f"Elemento eliminado: {dato}")
            except ValueError:
                print("Posición inválida")
        elif opcion == '6':
            dato = input("Ingrese el dato a buscar: ")
            pos = lista.buscar(dato)
            if pos != -1:
                print(f"Elemento encontrado en la posición {pos}")
            else:
                print("Elemento no encontrado")
        elif opcion == '7':
            lista.mostrar()
        elif opcion == '8':
            print(f"Tamaño de la lista: {lista.tamanio}")
        elif opcion == '9':
            break
        else:
            print("Opción inválida")


def menu_principal():
    while True:
        print("\n" + "="*50)
        print("PROGRAMA DE LISTAS ENLAZADAS")
        print("="*50)
        print("1. Lista Simplemente Enlazada")
        print("2. Lista Doblemente Enlazada")
        print("3. Lista Circular")
        print("4. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_lista_simples()
        elif opcion == '2':
            menu_lista_doble()
        elif opcion == '3':
            menu_lista_circular()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu_principal()