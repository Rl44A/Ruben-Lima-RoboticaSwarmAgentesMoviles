import zmq
import time
from Sokt import socket
socket.connect("tcp://192.168.50.165:5555")
def Sokt(A):
    #print("Enviando X,Y,Z",A)
    print("Mandando",A)
    socket.send_string(A)
        
    message = socket.recv()
    print("recibido %b",message)
    
        
    return 0    