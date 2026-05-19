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

