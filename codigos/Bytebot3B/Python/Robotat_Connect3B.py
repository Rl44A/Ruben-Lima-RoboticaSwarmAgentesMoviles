import threading
import socket
import json as json
import time 
#import SoktCPY
#from SoktCPY import Sokt
import math

HOST = "192.168.50.200"  # The server's hostname or IP address
PORT = 1883 # The port used by the server
global tcp_obj,Coo,As,Num,Msg,Coinicio
    
def Conexion_Robotat3B(agenteId):
       global Num;
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_obj:
            tcp_obj.connect((HOST, PORT))
            It=0;
            #print('Conectado')
            Num=0;
            while(It<8):
                while(1):
                    print("Continuar?")
                    X=int(input())
                    if X==1:
                        tcp_obj.sendall(json.dumps(agenteId).encode())
                        coordinates = tcp_obj.recv(1024).decode("utf-8")
                        
                        if(coordinates[1:19] =='onnected to the Ro'):
                            print('Primer mensaje, obviarlo')
                        else:
                            Coo = coordinates.split(sep=', ')
                            X=Coo[0]
                            XX=X[1:19]
                            Z=(Coo[2])
                            print("Coordenadas marker 7",XX +','+Z)
                            Msg=XX[0:6]+','+Z[0:6];
                            print("reduccion que se manda a bytebot",Msg)  
                            #Sokt(Msg)
                            It = It + 1
                            time.sleep(1)
                    else:
                        print("terminado")
                        
                
Conexion_Robotat3B(9)
