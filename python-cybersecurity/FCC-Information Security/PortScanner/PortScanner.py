import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the IP address: ")
port = int(input("Enter the port: "))

def portScanner(host, port):
    if s.connect_ex((host, port)):
        print("Port %d is closed" % port)
    else:
        print("Port %d is open" % port)

portScanner(host, port)