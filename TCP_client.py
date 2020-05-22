import socket

target_ip = "" # your ip
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_ip, target_port))

client.send("hi".encode(encoding='utf-8'))

response = client.recv(4000)

print(response)
