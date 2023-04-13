import zmq
from konectzmq import socket
import Movimiento
from Movimiento import Mov

socket.connect("tcp://localhost:6666")
Mess=1
#stringss=str(123.5534)+','+str(250.3554)

def soktLx(Cadena):
        strings = str(Cadena, 'UTF-8')
        print("Connectando a C")
        print("Enviando valores a C",strings)
        socket.send_string(strings)
        
        message = socket.recv()
        Mess=str(message,'UTF-8')
        #print("Recibiendo de C",Mess)
        print("Nuevas coordenadas Robot",Mess)
        #Variables para mandar a Mov
        Actual=strings[0:6]
        Actual2=strings[7:13]
        Sig=Mess[0:6]
        Sig2=Mess[10:17]
        Mov(Actual,Actual2,Sig,Sig2)
