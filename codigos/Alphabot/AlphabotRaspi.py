import socket


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
IP = '192.168.50.130'
#IP = '192.168.5.221'
PORT = 8500

server_address = (IP, PORT)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
global b , anteriorX,anteriorY,linea

def zero2(message):
    
    #ValoresAexcel(message)    
    sock.send(message.encode("utf-8"))
    print("datos mandados a Alphabot")
    
    data = sock.recv(1024).decode("utf-8")
    print("Comunicacion terminada",data)
    
