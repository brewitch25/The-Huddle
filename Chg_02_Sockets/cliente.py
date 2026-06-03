import socket
import threading
import sys
import time

HOST = '127.0.0.1'
PORT = 50001

# para verificar que el servidor sigue activo
servidor_activo = True

def recibir_mensaje(cliente_socket):
    """
    Se encarga de escuchar lo que llega del servidor
    """
    global servidor_activo
    while True:
        try:
            mensaje = cliente_socket.recv(1024)
            if not mensaje:
                print("Conexion cerrada por el servidor")
                break
            print(f"{mensaje.decode('utf-8')}")
        except:
            break       # Caso: caida repentina del servidor
    
    #Verificar que salimos del while, servidor fuera
    print("Se perdio conexion con el servidor")     
    servidor_activo = False

    # Cierre de socket para liberar espacio
    try:
        cliente_socket.close()
    except:
        pass

def intentos_conectar(cliente):
    """
    Intentamos conectar con el servidor con intentos
    """
    intentos = 3

    for i in range(intentos):
        try:
            cliente.connect((HOST, PORT))
            print("Conexion exitosa con el cliente")
            return cliente
        except Exception as e:
            print(f"Intentos {i+1} fallidos, Reintentando en 5 seg")
            time.sleep(5)

    return None

def iniciar_cliente():
    """
    Funcion para conectar y enviar mensajes
    """
    global servidor_activo
    nombre_cliente = input("Por favor, ingrese su nombre: ")
    
    # Creamos hilos para recibir mensajes en 2do plano
    hilo_recibir = threading.Thread(target=recibir_mensaje, args=(cliente,))
    hilo_recibir.start()

    # Hilo principal
    while True:
        try:
            texto = input("Si deseas salir, escribi 'salir' \nPodes escribir aca: ")
            if texto.lower() == 'salir':
                break
            cliente.send(texto.encode('utf-8'))
        except:
            print("Error al enviar mensaje")
            intentos_conectar(cliente)
    cliente.close()
    print("Te has desconectado del chat")
    

if __name__ == "__main__":
    iniciar_cliente()