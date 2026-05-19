# Aca estan los personajes y las reglas del juego
from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, x, y, simbolo):
        # Encapsulamiento
        self._x = x
        self._y = y
        self._simbolo = simbolo
    
    # Getter: Se utiliza para recuperar el valor de un atributo privado
    @property 
    def posicion(self):
        return(self._x, self._y)
    
    def simbolo(self):
        return self._simbolo
    
    @abstractmethod
    def calcularMovimiento(self, *args):
        """Cada entidad calcula su movimiento a su manera"""
        pass

    def mover(self, nueva_x, nueva_y):
        """Logica comun de movimiento para la entidad que si cambia de posicion"""
        self._x = nueva_x
        self._y = nueva_y

# Aca se aplica herencia
class Raton(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, "🐭")
    
    def calcularMovimiento(self, direccion_teclado):
        nx, ny = self._x, self._y
        if direccion_teclado == "W": ny -= 1        # Arriba
        if direccion_teclado == "S": ny += 1        # Abajo
        if direccion_teclado == "A": nx -= 1        # Izquierda
        if direccion_teclado == "D": nx += 1        # Derecha
        return nx, ny
    
class Gato(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, "🐱")

    def calcularMovimiento(self, pos_raton):
        rx, ry = pos_raton
        nx, ny = self._x, self._y       # Posicion gato (nx, posicion actual en el eje X, ny lo mismo pero en posicion Y)

        if nx < rx: nx += 1
        elif nx > rx: nx -= 1
        elif ny < ry: ny += 1
        elif ny > ry : ny -= 1
        return nx, ny


