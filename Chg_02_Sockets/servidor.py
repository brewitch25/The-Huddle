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

def iniciar_servidor():
    """
    Funcion que crea e inicia el servidor
    """
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_servidor.bind((HOST, PORT))
        socket_servidor.listen()
        print(f"El servidor esta escuchando en el {HOST}:{PORT}")
    except Exception as e:
        print(f"Error al iniciar el servidor{e}")
        return
    while True:
        try:
            cliente_socket, direccion = socket_servidor.accept()
            print(f"Nueva conexion establecida desde{direccion}")

            #Guardamos al cliente en la lista
            clientes.append(cliente_socket)

            # Usamos thread (hilo para atender a clientes en paralelo)
            hilo = threading.Thread(target=manipular_cliente, args=(cliente_socket))
            
            #EL hilo desaparece si el programa principal se cierra
            hilo.daemon = True          
            hilo.start()

        except KeyboardInterrupt:
            print("Apagando el servidor")
            break
        except:
            print("Ocurrio un error al aceptar la conexion")


