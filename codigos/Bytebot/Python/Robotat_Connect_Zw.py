import threading
import socket
import json as json
import time 
import math
import SocketClienteZw
from SocketClienteZw import zero

HOST = "192.168.50.200"  # The server's hostname or IP address
PORT = 1883 # The port used by the server
global tcp_obj,Coo,As,Num,Msg,Coinicio,rep
#DatosRobot = pd.DataFrame(columns=['ActualX', 'ActualY', 'SiguienteX','SiguienteY'],index=range(4))
    

                    
def Conexion_RobotatZW(agenteId):
       global b,anteriorX,anteriorY, Num,rep,Ex,Ey;
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_obj:
            tcp_obj.connect((HOST, PORT))
            Num=0;
            rep=0;
            anteriorX=0;
            anteriorY=0
            while(rep<15):
                tcp_obj.sendall(json.dumps(agenteId).encode())
                coordinates = tcp_obj.recv(1024).decode("utf-8")
                    
                if(coordinates[1:19] =='onnected to the Ro'):
                    print('Primer mensaje, obviarlo')
                    time.sleep(15)
                else:
                    Coo = coordinates.split(sep=', ')
                    X=Coo[0]
                    XX=X[1:19]
                    Z=(Coo[2])
                    Ex=XX[0:6]
                    Ey=Z[0:6]
                    #Msg=XX[0:6]+','+Z[0:6];
                    Msg=Ex+','+Ey;
                    print(Msg) 
                    zero(Msg)
                    rep = rep + 1
                    print(rep)
                    

                
Conexion_RobotatZW(5)   
