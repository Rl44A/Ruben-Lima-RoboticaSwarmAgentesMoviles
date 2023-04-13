from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
import time
import socket
from time import sleep
import numpy as np
import random
import RPi.GPIO as GPIO
#///////////////// Define Motor Driver GPIO Pins /////////////////

print("--* Hilo de Ejecición - Servidor para Agentes TX*")
print("--* Tiempo de Inicio TX", time.strftime("%b %d %Y %H:%M:%S", time.gmtime(int(time.time()))))
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = ''
PORT = 7500
servidor.bind((IP, PORT))
print("--* Preparandose para recibir clientes")
servidor.listen(1)
conn, address = servidor.accept()
print("--* Conectado a: "+address[0] + ":" + str(address[1]))
Colores = ["R","G","B"]
k = 0
print("--* Comenzando a enviar tramas")

def Enviar(k):
    desicion = Colores[k]
    k = k + 1
    if k == 3:
        k = 0
    conn.send(desicion.encode())
    print("--* Comando Enviado")
    time.sleep(1)

def Moverse(ActualX,ActualZ,SiguienteX,SiguienteZ):
    ActualXX=float(ActualX)
    ActualZZ=float(ActualZ)
    SiguienteXX=float(SiguienteX)
    SiguienteZZ=float(SiguienteZ)
    #print("Ax",ActualXX,"Az",ActualZZ,"Sx",SiguienteXX,"Sz",SiguienteZZ)
    RecepSiguiente=np.array([SiguienteXX,SiguienteZZ]);#Recepcion de C
    RecepActual=np.array([ActualXX,ActualZZ]);   #Recepcion de C
    #print("Recep Actual",RecepActual)
    #print("Recep Siguiente",RecepSiguiente)
    RecepNegativo=np.array([-1.0,-1.0]);
    # Posicionamiento y ejecución 
    RecepResta=np.multiply(RecepNegativo,RecepActual);
    RecepSumatoria=np.add(RecepResta,RecepSiguiente);#Cuanto tiene que moverse y a donde 
    #----------------------------------------------------------EjeX
    if RecepSumatoria[0]>0:
        print("Mandando Green")
        k=1
    elif RecepSumatoria[0]<0:
        print("Mandando Blue")
        k=2
    else:
        print("Movimiento 0 en eje X")      
   #-----------------------------------------------------------EjeY
    Enviar(k)
    sleep(2)
    print("Giro a la derecha");
    k=0
    print("Mandando Rojo")
    Enviar(k)
    sleep(3)
    if RecepSumatoria[1]<0:
        print("Mandando Blue") 
        k=2
    elif RecepSumatoria[1]>0:
        print("Mandando Green")
        k=1
    else:
        print("Movimiento 0 en eje Y")
    
    print("Movimiento Terminado")
    Enviar(k)
    sleep(2)
    k=0
    print("Mandando Rojo")
    Enviar(k)
    sleep(3)
    #Cambio de posiciones nuevas 
    #termina la función y regresa algo que le diga al algoritmo que tiene que volver a pedir la informacion y realizarse otra vez
    



