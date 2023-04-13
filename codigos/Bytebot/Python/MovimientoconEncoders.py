# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:48:08 2022

@author: lima1
"""

#Controlador utilizando los encoders 
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
import numpy as np
import random
import RPi.GPIO as GPIO
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

#Variables del controlador
Input=0.0
SampleTime = 0.0
SetPoint=0.0
dInput=0.0
lastInput=0.0
kp=0.0
ki=0.0
kd=0.0
outmin=0.0
outmax=0.0
error=0.0
Iterm=0.0
lasttime=0.0
Contador=0
ant=0
cmd=0
pwm=0


 
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

A_pin = 12
B_pin = 16


  

GPIO.setmode(GPIO.BCM)
GPIO.setup(A_pin, GPIO.IN)
GPIO.setup(B_pin, GPIO.IN)

outcome = [0,-1,0,1,0,1,0,1,1,0,0,1,0,1,1,0]
last_AB = 0b00
   
#Comienza parte de recepción y ejecución
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
	driveLeft.value =0.1
	driveRight.value = 0.1


 
def reverseDrive():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value =0.1
	driveRight.value = 0.1
	
 
def SpinLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.5
	driveRight.value = 0.5
	
 
def SpinRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.5
	driveRight.value = 0.5
	

 
def forwardTurnLeft():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.2
	driveRight.value = 0.8
	sleep(1)
	allStop()    
 
def forwardTurnRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.8
	driveRight.value = 0.2
	sleep(1)
	allStop()
 
def reverseTurnLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.2
	driveRight.value = 0.8
	sleep(1)
	allStop()
 
def reverseTurnRight():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.8
	driveRight.value = 0.2
	sleep(1)
	allStop()    
#Comienza parte de recepción y ejecución
def Encendido():
    SampleTime = 50
    kp=1.0
    ki=0.05;
    kd=23.0
    SetPoint = Contador
#Recepción con un socket de python y C, variable de prueba por el momento 
STANBY.value = True
def Dr(Direccion):
    last_AB = 0b00
    counter=0
    if Direccion == 1:
        while counter < 70:
            print("Adelante 40")
            forwardDrive()
            A = GPIO.input(A_pin)
            B = GPIO.input(B_pin)
            current_AB = (A << 1) | B
            position = (last_AB << 2) | current_AB
            counter += outcome[position]
            last_AB = current_AB
            
    allStop()
    if Direccion == 2:
        while counter < 70:
            print("Atras 40")
            reverseDrive()
            A = GPIO.input(A_pin)
            B = GPIO.input(B_pin)
            current_AB = (A << 1) | B
            position = (last_AB << 2) | current_AB
            counter += outcome[position]
            last_AB = current_AB
            
    allStop()
    if Direccion == 3:
        while counter < 17:
            print("Derecha 20")
            SpinRight()
            A = GPIO.input(A_pin)
            B = GPIO.input(B_pin)
            current_AB = (A << 1) | B
            position = (last_AB << 2) | current_AB
            counter += outcome[position]
            last_AB = current_AB
            
    allStop()
    if Direccion == 4:
        while counter < 16:
            print("Izquierda 20")
            SpinLeft()
            A = GPIO.input(A_pin)
            B = GPIO.input(B_pin)
            current_AB = (A << 1) | B
            position = (last_AB << 2) | current_AB
            counter += outcome[position]
            last_AB = current_AB
            #print (counter)
    allStop()
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
        print("Movimiento hacia arriba eje X",RecepSumatoria[0])
        Dr(1)
        sleep(2)
    elif RecepSumatoria[0]<0:
        print("Movimiento hacia abajo eje X",RecepSumatoria[0])
        Dr(2)
        sleep(2)
    else:
        print("Movimiento 0 en eje X")      
   #-----------------------------------------------------------EjeY
    print("Giro a la derecha");
    Dr(4)
    sleep(3)
    if RecepSumatoria[1]<0:
        print("Movimiento hacia izquierda",RecepSumatoria[1])
        Dr(2)
        sleep(2)
    elif RecepSumatoria[1]>0:
        print("Movimiento hacia derecha",RecepSumatoria[1])
        Dr(1)
        sleep(2)
    else:
        print("Movimiento 0 en eje Y")
    
    print("Movimiento Terminado")
    Dr(3)
    sleep(3)
    #Cambio de posiciones nuevas 
    #termina la función y regresa algo que le diga al algoritmo que tiene que volver a pedir la informacion y realizarse otra vez
    

