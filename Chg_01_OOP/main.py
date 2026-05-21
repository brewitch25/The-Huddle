# Aca se manejan los turnos y las condiciones de victoria
import random
from personajes import  Raton, Gato, Queso
from render import UIConsole

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
        self.gato = self.ubicar_gato_aleatorio()

        # Ubicamos al queso de forma aleatoria en el tablero(evitando al gato y al raton)
        self.queso = self.ubicar_queso_aleatorio()

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
                return Gato(aleatorio_x, aleatorio_y)

    def ubicar_queso_aleatorio(self):
        """
        Posiciona de manera aleatoria el queso en el tablero, verificar que el queso no aparezca en 
        la misma posicion que el gato y el raton
        """
        while True:
            aleatorio_x = random.randint(0, self.tamaño_tablero - 1)
            aleatorio_y = random.randint(0, self.tamaño_tablero - 1)
            posicion_posible = (aleatorio_x, aleatorio_y)

            # Verificar que el queso no este en la misma posicion del gato o del raton 
            if posicion_posible != self.gato.posicion and posicion_posible != self.raton.posicion:
                return Queso(aleatorio_x, aleatorio_y)
            
    def verificar_fin_juego(self):
        """
        Verifica las condiciones de victoria o derrota
        """
        # En caso de derrota(gato atrapo al raton)
        if self.gato.posicion == self.raton.posicion:
            UIConsole.mostrar_tablero(self.gato, self.raton, self.queso, self.tamaño_tablero)
            UIConsole.mostrar_mensaje("Haz sido atrapado! Termino el juego :(")
            self.jugando = False
        
        # En caso de vistoria(raton llego el queso)
        if self.raton.posicion == self.queso.posicion:
            UIConsole.mostrar_tablero(self.gato, self.raton, self.queso)
            UIConsole.mostrar_mensaje("Llegaste al queso! Haz ganado el juego!")
            self.jugando = False

    def loop_central(self):
        """
        El motor del juego, manejo de turnos
        """
        while self.jugando:
            # Mostrar el estado del juego(matriz)
            UIConsole.mostrar_tablero(self.gato, self.raton, self.queso, self.tamaño_tablero)

            # Turno del raton
            movimiento = UIConsole.pedir_movimiento_raton()
            proximo_x_raton, proximo_y_raton = self.raton.calcular_movimiento(movimiento)

            # Verificar que el raton se pueda mover, sin chocar
            if self.es_posicion_valida(proximo_x_raton, proximo_y_raton):
                self.raton.mover(proximo_x_raton, proximo_y_raton)

            # Verificar que el raton gano antes de que se mueva el gato
            self.verificar_fin_juego()
            if not self.jugando:
                break

            # Turno del gato
            proximo_x_gato, proximo_y_gato = self.gato.calcular_movimiento(self.raton.posicion)

            #Verificar que el gato se mueva sin chocar por los bordes de la matriz
            if self.es_posicion_valida(proximo_x_gato, proximo_y_gato):
                self.gato.mover(proximo_x_gato, proximo_y_gato)
            
            # Verificar que el gato atrapo al raton
            self.verificar_fin_juego()

"""
Ejecucion del juego
"""
if __name__ == "__main__":
    juego = Game()
    juego.loop_central()