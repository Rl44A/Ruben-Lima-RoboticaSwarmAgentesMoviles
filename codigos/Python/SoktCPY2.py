import zmq
import time
from Sokt import socket
socket.connect("tcp://192.168.50.167:5555")
def Soktt(A):
    #print("Enviando X,Y,Z",A)
        
    socket.send_string(A)
        
    message = socket.recv()
        #print("received reply %s",message)
    
        
    return 0