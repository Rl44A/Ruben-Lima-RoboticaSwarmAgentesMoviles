import socket
import time
#IP = "192.168.5.221"
IP = "192.168.50.167"

PORT = 6800
ADDR = (IP, PORT)

""" TCP Socket """
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
    
import MovimientoconEncoders
from MovimientoconEncoders import Moverse
def soktLxZw(strings):
    """ Send data """
    #data = "2.2222,3.3333"
    print("Mandando a C",strings)
    client.send(strings.encode("utf-8"))
    """ Recv data """
    Mess = client.recv(1024).decode("utf-8")
    print(f"[SERVER] {Mess}")
    Actual=strings[0:6]
    Actual2=strings[7:13]
    Sig=Mess[0:6]
    Sig2=Mess[11:17]
    Moverse(Actual,Actual2,Sig,Sig2)
