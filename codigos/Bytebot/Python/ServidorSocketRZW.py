# Servidor
import socket
import sokkt
from sokkt import soktLxZw
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#IP = '192.168.5.221'
IP = '192.168.50.167'
PORT = 5800
s.bind( (IP, PORT))
s.listen(1)
Num=0
    
while True:
        print('waiting for a connection')
        conexion, address= s.accept()
        print("Connection from " + str(address[0]) + " has been established.")
        
        try:
            print('conectado a RaspizeroW', address)
            
            # Receive the data in small chunks and retransmit it
            while True:
                data = conexion.recv(1024).decode("utf-8")
                print("Iteracion",Num)
                Num=Num+1
                print('received {!r}'.format(data))
                soktLxZw(data)
                mensaje = "total"
                conexion.send(mensaje.encode("utf-8"))
                
                
        finally:
            # Clean up the connection
            conexion.close()        
