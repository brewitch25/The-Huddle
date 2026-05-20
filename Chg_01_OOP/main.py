# Aca se dibuja el tablero y se piden los mivimientos al usuario, interfaz de la consola
import os

class UIConsole:
    @staticmethod
    def solicitar_tamano_tablero():
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
    
    @staticmethod
    def mostrar_tablero(gato, raton, queso, tamaño_tablero):
        """
        Dibuja el tablero en la consola, fila por fila
        Se utiliza emojis para rellenar los espacios vacios
        """
        #limpia la terminal para que aparezaca un solo tablero "animado" en el mismo lugar
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Tu objetivo! Llegar al queso antes de que te atrape el gato!")

        # Obtenemos las posiciones actuales, desde el encapsulamiento de cada personaje(Entidad)
        posicion_gato = gato.posicion
        posicion_raton = raton.posicion
        posicion_queso = queso.posicion

        # Recorremos la matriz por fila (eje Y) y por columna (Eje X)
        for fila in range(tamaño_tablero):
            linea_tablero = ""
            for columna in range(tamaño_tablero):
                posicion_actual = (columna, fila)
                
                # Verificamos si hay algun personaje en la coordenada
                if posicion_actual == posicion_raton:
                    linea_tablero += raton.simbolo
                elif posicion_actual == posicion_gato:
                    linea_tablero += gato.simbolo
                elif posicion_actual == posicion_queso:
                    linea_tablero += queso.simbolo
                else:
                    linea_tablero += "🟩"
            
            print(linea_tablero)
        print("\n" + "-" * (tamaño_tablero * 2))

    @staticmethod
    def pedir_movimiento_raton():
        """
        Toma la direccion que el usuario ingresa para mover el raton
        """
        print("Mover al raton: W = Arriba - S = Abajo - A = Izquierda - D = derecha")
        return input("Introduce los movimientos: ").upper()

    @staticmethod
    def mostrar_mensaje(mensaje):
        """
        Funcion para imprimir los mensajes en general
        """
        print(f"{mensaje}")
