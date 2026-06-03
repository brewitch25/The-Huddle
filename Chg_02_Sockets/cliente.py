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

def intentar_conectar():
    """
    Intentamos conectar con el servidor con intentos
    """
    intentos = 3

    for i in range(intentos):
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            cliente.connect((HOST, PORT))
            print("Conexion exitosa con el cliente")
            return cliente
        except Exception as e:
            print(f"Intentos {i+1} fallidos, Reintentando en 3 seg")
            time.sleep(3)

    return None

def iniciar_cliente():
    """
    Funcion para conectar y enviar mensajes
    """
    global servidor_activo
    nombre_cliente = input("Por favor, ingrese su nombre: ")

    while True:
        servidor_activo = True

        cliente = intentar_conectar()

        # Creamos hilos para recibir mensajes en 2do plano
        hilo_recibir = threading.Thread(target=recibir_mensaje, args=(cliente,))
        hilo_recibir.start()

        # Hilo principal
        while servidor_activo:
            try:
                # Caso de servidor desconectado
                if not servidor_activo:
                    break

                texto = input("Si deseas salir, escribi 'salir' \nPodes escribir aca: ")

                # Caso: servidor inactivo no envia el mensaje
                if not servidor_activo:
                    break

                if texto.lower() == 'salir':
                    cliente.close()
                    sys.exit()

                mensaje_cliente = f"{nombre_cliente}, {texto}"
                cliente.send(mensaje_cliente.encode('utf-8'))
            except(KeyboardInterrupt, SystemExit):
                cliente.close()
                sys.exit()
            # Manejar problemas de conexion del servidor
            except:
                servidor_activo = False
                break

        print("Iniciando recuperacion automatica")
        

if __name__ == "__main__":
    iniciar_cliente()