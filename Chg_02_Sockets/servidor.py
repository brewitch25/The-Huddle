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