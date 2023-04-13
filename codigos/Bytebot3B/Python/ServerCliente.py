import time 
import zmq
import Client
from Client import soktLx

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
Num=0;
while True: 

	Trama = socket.recv()
	print("iteracion",Num)
	Num=Num+1;
	print("valores recibidos y a enviar al cliente %s" % Trama )
	time.sleep(1);
	soktLx(Trama);
	time.sleep(1);
	#print("Nuevas coordenadas Robot",Client.Mess)
	socket.send_string("Movimiento Listo, siguiente iteracion")
