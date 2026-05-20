# Aca se dibuja el tablero y se piden los mivimientos al usuario, interfaz de la consola
import os

class UIConsole:
    @staticmethod
    def solicitarTamanoTablero():
        """
        Pide al usuario que ingrese tamaño del tablero, no debe ser menor a 5x5
        Uso de try, except para asegurar que ingrese solo numeros enteros
        """
        while True:
            try: 
                tablero = int(input("Introduce el tamaño del tablero(minimo 5): "))
                if tablero >= 5:
                    return tablero
                else:
                    print("Tablero muy pequeño, ingrese otro numero")
            except ValueError:
                print("Ingrese un numero entero valido")