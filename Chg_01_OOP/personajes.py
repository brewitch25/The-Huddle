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
    
    @property
    def simbolo(self):
        return self._simbolo
    
    @abstractmethod
    def calcular_movimiento(self, *args):
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
    
    def calcular_movimiento(self, direccion_teclado):
        """
        Calcula el movimiento del raton de acuerdo al input del usuario, que son los siguientes:
        W= arriba, S= abajo, A= izquierda, D= derecha
        """
        nx, ny = self._x, self._y
        if direccion_teclado == "W": ny -= 1        
        if direccion_teclado == "S": ny += 1        
        if direccion_teclado == "A": nx -= 1        
        if direccion_teclado == "D": nx += 1        
        return nx, ny
    
class Gato(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, "🐱")

    def calcular_movimiento(self, pos_raton):
        """
        Calcula los movimientos del gato, se mueve sin necesidad de inputs del usuario, 
        usa las coordenadas del raton para intentar atrapara al raton
        """
        rx, ry = pos_raton
        gx, gy = self._x, self._y       # Posicion gato (gx, posicion actual en el eje X, gy lo mismo pero en posicion Y)

        if gx < rx: gx += 1
        elif gx > rx: gx -= 1
        elif gy < ry: gy += 1
        elif gy > ry : gy -= 1
        return gx, gy

class Queso(Entidad):
    def __init__(self, x, y):
        super().__init__(x, y, "🧀")

    def calcular_movimiento(self, *args):
        """
        No calcula movimientos, es una entidad estatica, se mantiene en la misma posicion
        durante la ejecucion del juego
        """
        return self._x, self._y             