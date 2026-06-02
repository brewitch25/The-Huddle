import socket
import threading

# Configuraciones del host y puerto
HOST = '127.0.0.1'
PORT = 50001

# Para almacenar sockets de clientes activos
clientes = []

def crear_broadcast(mensaje, cliente_origen):
    """
    Envia mensaje a todos los clientes, excepto al que lo envio
    """
    for cliente in cliente:
        if cliente != cliente_origen:
            try:
                cliente.send(mensaje)
            except:
                remover_cliente(cliente)    # Si falla al enviar

def manipular_cliente(cliente_socket):
    """
    Funcion que se encarga de escuchar los mensajes del cliente
    """
    while True:
        try:
            mensaje = cliente_socket.recv(1024)
            if not mensaje:
                break
            crear_broadcast(mensaje, cliente_socket)
        except:
            break
    remover_cliente(cliente_socket) 

def remover_cliente(cliente_socket):
    """
    Elimina al cliente de la lista y cierra el socket del mismo
    """
    if cliente_socket in clientes:
        clientes.remove(cliente_socket)
        try:
            cliente_socket.close()
        except:
            pass
        print(f"Un cliente se retiro, quedan {len(clientes)}")

        