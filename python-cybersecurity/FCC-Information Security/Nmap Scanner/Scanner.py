import nmap

scanner = nmap.PortScanner()

print("Welcome to Nmap Automation Script")
print("<------------------------------->")

ip_addr = input("Enter the IP address of the target: ")
print("The IP address you entered is: " + ip_addr)

type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
    1)SYN ACK Scan
    2)UDP Scan
    3)Comprehensive Scan\n""")
print("You have selected option: " + resp)

if resp == '1':
    print("Nmap Version: " + scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: " + scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: " + str(scanner[ip_addr]['tcp'].keys()))
elif resp == '2':
    print("Nmap Version: " + scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: " + scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: " + str(scanner[ip_addr]['udp'].keys()))
elif resp == '3':
    print("Nmap Version: " + scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: " + scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: " + str(scanner[ip_addr]['tcp'].keys()))
elif resp >= '4':
    print("Wrong Choice")