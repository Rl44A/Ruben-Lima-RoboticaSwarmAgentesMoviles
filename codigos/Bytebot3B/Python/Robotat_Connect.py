
import socket
import numpy as nu
import json as json
import time 
import math
import SoktCPY
from SoktCPY import Sokt

HOST = "192.168.50.201"  # The server's hostname or IP address
PORT = 1883 # The port used by the server
global tcp_obj,Coo,As
def Transformacion(x,y,z,w):
        t0 = 2.0 * (w * x + y * z)
        t1 = 1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = 2.0 * (w * y - z * x)
        t2 = 1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = 2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
        #print("RollX",nu.rad2deg(roll_x))
        print("PitchY",nu.rad2deg(pitch_y))
        #print("YawZ",nu.rad2deg(yaw_z))
     
        return roll_x, pitch_y, yaw_z # in radians
    
def Conexion_Robotat(agenteId):
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_obj:
           tcp_obj.connect((HOST, PORT))
           #print('Conectado')
           inicio=time.time()
           for i in range(100):
               tcp_obj.sendall(json.dumps(agenteId).encode())
               coordinates = tcp_obj.recv(1024).decode("utf-8")
               
               if(coordinates[1:19] =='onnected to the Ro'):
                   print('Primer mensaje, obviarlo')
               else:
                   #print(coordinates)
                   Coo = coordinates.split(sep=', ')
                   X=Coo[0]
                   XX=X[1:19]
                   XXX=float(XX)
                   #print("Cordenada X", XXX)
                   Y=(Coo[1])
                   #print("Cordenada Y", Y)
                   Z=(Coo[2])
                   #print("Cordenada Z", Z)
                   
                   Q1=Coo[3]
                   QQ1=float(Q1)
                   #print("Cordenada Q1", QQ1)
                   Q2=Coo[4]
                   QQ2=float(Q2)
                  # print("Cordenada Q2", Q2)
                   Q3=Coo[5]
                   QQ3=float(Q3)
                  # print("Cordenada Q3", Q3)
                   Q4=Coo[6]
                   QQ4=Q4[0:18]
                   QQQ4=float(QQ4)
                   #print("Cordenada Q4", QQQ4)
                   #Transformacion(QQ1,QQ2,QQ3,QQQ4)
                   #print(XX,',',Z)
                   Num=0;
                   Msg=str(Num)+','+XX[0:6]+','+Y[0:6]+','+Z[0:6];
                   Sokt(Msg)
                   Num+1;
                   #time.sleep(2);
           print('termino')
           final=time.time()
           print('tiempo',inicio-final)
    #timeout_count=0;
    #timeout = 10000;
    #bytes_recvd=0
    #MSGLEN=100
    
    # while(bytes_recvd < MSGLEN) and (timeout_count < timeout):
    #         timeout_count=timeout_count+1;
    # if(timeout_count== timeout):
    #     print("No se recive mas data del server")
        
    # else:
    #     mocap_data = json.JSONDecoder(chr(tcp_obj.recv(1024)))
    #     mocap_data = nu.reshape(mocap_data,[7,len(agenteId)])
        #if(rotrep == 'eulzyx'):
         #   mocap_data[:,4:nu.end-1]=nu.rad2deg(euler_from_quaternion(mocap_data))
          #  mocap_data[:,nu.end]=[];
        #else:
         #   print('error, invalid ID(s)')
            

Conexion_Robotat(9)
        
    