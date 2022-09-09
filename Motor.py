from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
import numpy as np
import random 
#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_DRIVE_LEFT = 24		# ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 18	# IN1 - Forward Drive
REVERSE_LEFT_PIN = 23	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 7		# ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 8	# IN1 - Forward Drive
REVERSE_RIGHT_PIN = 25	# IN2 - Reverse Drive
STBY = 1
 
# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)
 
# Initialise objects for H-Bridge digital GPIO pins
STANBY = DigitalOutputDevice(STBY)
forwardLeft = DigitalOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = DigitalOutputDevice(REVERSE_LEFT_PIN)
forwardRight = DigitalOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = DigitalOutputDevice(REVERSE_RIGHT_PIN)

def allStop():
	forwardLeft.value = False
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = False
	driveLeft.value = 0
	driveRight.value = 0
 
def forwardDrive():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.3
	driveRight.value = 0.3
 
def reverseDrive():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.3
	driveRight.value = 0.3
 
def spinLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def SpinRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0
 
def forwardTurnLeft():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.2
	driveRight.value = 0.8
 
def forwardTurnRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.8
	driveRight.value = 0.2
 
def reverseTurnLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.2
	driveRight.value = 0.8
 
def reverseTurnRight():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.8
	driveRight.value = 0.2
    
#Comienza parte de recepción y ejecución

#Recepción con un socket de python y C, variable de prueba por el momento 

def Movimiento():

    A=random.uniform(-3.5, 3.5)
    print(A);
    C=random.uniform(-3.5, 3.5)
    print(C);
    RecepSiguiente=np.array([A,0.16,C]);#Recepcion de C
    RecepActual=np.array([0.9121,0,2.0691]);   #Recepcion de C
    RecepNegativo=np.array([-1.0,-1.0,-1.0]);
    # Posicionamiento y ejecución 
    RecepResta=np.multiply(RecepNegativo,RecepActual);
    RecepSumatoria=np.add(RecepResta,RecepSiguiente);#Cuanto tiene que moverse y a donde 
    #----------------------------------------------------------EjeX
    if RecepSumatoria[0]>0:
        print("Movimiento hacia arriba eje X",RecepSumatoria[0])
        forwardDrive() 
    elif RecepSumatoria[0]<0:
        print("Movimiento hacia abajo eje X",RecepSumatoria[0])
        reverseDrive()
    else:
        print("Movimiento 0 en eje X")
        
    #-----------------------------------------------------------EjeY
    print("Giro a la derecha");
    forwardTurnRight()
    if RecepSumatoria[2]<0:
        print("Movimiento hacia izquierda",RecepSumatoria[2])
        reverseDrive()
    elif RecepSumatoria[2]>0:
        print("Movimiento hacia derecha",RecepSumatoria[2])
        forwardDrive()
    else:
        print("Movimiento 0 en eje Y")
    print("Giro a la izquierda")
    forwardTurnLeft()
    #Cambio de posiciones nuevas 
    #termina la función y regresa algo que le diga al algoritmo que tiene que volver a pedir la informacion y realizarse otra vez
    

     

 
# numero = int(input("Seleccione una opcion: "))
# STANBY.value = True 
# while True:
#         if numero == 1:
#                 forwardDrive()
#         if numero == 2:
#                 reverseDrive()
#         if numero == 3:
#                 allStop()
#         if numero == 4:
#                 forwardTurnLeft()
#         if numero == 5:
#                 forwardTurnRight()
#         if numero == 6:
#                 numero == 0
#         else:
#                 print("Numero 1 = avanza")
#                 print("Numero 2 = retrocede")
#                 print("Numero 3 = Stop")
#                 print("Numero 4 = ForwardTurnLeft")
#                 print("Numero 5 = ForwardTurnRight")
#                 numero = int(input("Seleccione una opcion: "))

    




