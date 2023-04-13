
import time 
import zmq 

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
while True: 

	Trama = socket.recv()
	print("valores recibidos %s" % Trama )
	
	socket.send(b"1")
