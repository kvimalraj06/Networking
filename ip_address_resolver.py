import socket

target_name = input("enter the domain: ")
target_ip = socket.gethostbyname(target_name) # socket method to convert the domain name into ip
print("The ip address of the {} is {}".format(target_name, target_ip))