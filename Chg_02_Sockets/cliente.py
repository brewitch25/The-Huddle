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
