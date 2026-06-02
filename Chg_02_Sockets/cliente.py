import socket
import threading
import sys
import time

HOST = '127.0.0.1'
PORT = 50001

def recibir_mensaje(cliente_socket):
    """
    Se encarga de escuchar lo que llega del servidor
    """
    while True:
        try:
            mensaje = cliente_socket.recv(1024)
            if not mensaje:
                print("Conexion cerrada por el servidor")
                break
            #print(f"{mensaje.decode('utf-8')}")     #Mostrar en la pantalla(decodificado de byte a txt)
        except:
            print("Error al recibir los datos")
            break

        print("Saliendo del modo escucha")
        sys.exit()

def intentos_conectar():
    """
    Intentamos conectar con el servidor con intentos
    """
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    intentos = 3

    for i in range(intentos):
        try:
            cliente.connect((HOST, PORT))
            print("Conexion exitosa con el cliente")
            return cliente
        except:
            print(f"Intentos {i+1} fallidos, Reintentando en 3 seg")
            time.sleep(3)

    return None

def iniciar_cliente():

    cliente = intentos_conectar()
    if not cliente:
        print("No se pudo establecer conexion")
        return
    
    # Creamos hilos para recibir mensajes en 2do plano
    hilo_recibir = threading.Thread(target=recibir_mensaje, args=(cliente,))
    hilo_recibir.daemon = True
    hilo_recibir.start()

    # Hilo principal
    print("Podes escribir. Para terminar escribi 'salir' ")
    while True:
        try:
            texto = input()
            if texto.lower() == 'salir':
                break
        
        except KeyboardInterrupt:
            break
        except:
            print("Error al enviar mensaje")

    cliente.close()
    print("Te has desconectado del chat")

if __name__ == "__main__":
    iniciar_cliente()