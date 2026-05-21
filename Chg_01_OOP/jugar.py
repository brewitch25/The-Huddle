# Aca se manejan los turnos y las condiciones de victoria
import random
from personajes import Gato, Raton, Queso
from main import UIConsole

class Game:
    def __init__(self):
        """
        Constructor del terreno de juego
        """
        # Solicitud del tamaño de la matriz de juego
        self.tamaño_tablero =  UIConsole.solicitar_tamano_tablero()
        
        # Ubicamos al raton en la esquina inferior derecha
        limite_maximo = self.tamaño_tablero - 1
        self.raton = Raton(limite_maximo, limite_maximo)

        # Ubicamos al gato de forma aleatoria en el tablero
        self.gato = self.inicializar_gato_aleatorio()

        # Ubicamos al queso de forma aleatoria en el tablero(evitando al gato y al raton)
        self.queso = self.inicializar_queso_aleatorio()

        # Estado inicial del juego
        self.jugando = True

    def es_posicion_valida(self, x, y):
        """
        Verifica si las coordenadas estan dentro del tablero - Encapsulamiento
        """
        return 0 <= x < self.tamaño_tablero and 0 <= y < self.tamaño_tablero
    
    def ubicar_gato_aleatorio(self):
        """
        Posiciona de manera aleatoria al gato en el tablero, evitando que aparezca en la misma
        posicion que el raton al iniciar el juego
        """
        while True:
            aleatorio_x = random.randint(0, self.tamaño_tablero - 1)
            aleatorio_y = random.randint(0, self.tamaño_tablero - 1)
            posicion_posible = (aleatorio_x, aleatorio_y)

            # Si el gaton no coincide con la posicion del raton, se crea el personaje
            if posicion_posible != self.raton.posicion:
                return self.Gato(aleatorio_x, aleatorio_y)

