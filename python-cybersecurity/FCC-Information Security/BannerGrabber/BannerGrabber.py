import socket
def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print("The banner is: " +str(s.recv(1024)).split("b"))
def main():
    ip = input("Enter the IP address: ")
    port = str(input("Enter the port: "))
    banner(ip, port)

main()
