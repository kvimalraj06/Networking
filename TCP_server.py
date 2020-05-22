import socket
import threading

bind_ip = "" # your IP
bind_port = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # to use ipv4 and tcp

server.bind((bind_ip, bind_port))

server.listen(5)
print("listening on %s:%d" % (bind_ip,bind_port) )

def handle_client(client_socket):

    request = client_socket.recv(4000)
    print("received %s" % (request))

    client_socket.send("ACK!".encode(encoding='utf-8'))

    client_socket.close()

while True:

    client,addr = server.accept()

    print("client is: ",client)
    print("accepting connection from %s:%d" % (addr[0],addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client,))

    client_handler.start()