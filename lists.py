''' ports = [22, 80, 443, 8080]
names = ["Anish", "Raj", "Priya"]
mixed = [1, "hello",True, 3.14] '''

ports = [22, 80, 443, 8080]
print(ports)
print(ports[0])
print(ports[-1])
print(len(ports))

ports = [22, 80, 443, 8080]

ports.append(3306)
print(ports)

ports.remove(80)
print(ports)

ports.sort()
print(ports)

print(ports.index(443))

blocked_ips = ["192.168.1.5", "10.0.0", "172.16.0.1"]
ip = input("Enter IP: ")

if ip in blocked_ips :
    print("Blocked - access denied")
else:
    print("allowed - access granted")
    

blocked_ips = ["192.168.1.5", "10.0.0.2", "172.16.0.1"]
blocked_ips.append("8.8.8.8")
blocked_ips.remove("10.0.0.2")
print(f"Blocked Ips : {blocked_ips}")
ip = input("Enter Ip to check: ")
if ip in blocked_ips:
    print("BLOCKED")
else:
    print("ALLOWED")


ports  = [21, 22, 80, 443, 8080, 8443]
print(ports[0:3])
print(ports[2:5])
print(ports[:3])
print(ports[3:])
print(ports[-2:])

numbers = [1,2,3,4,5]
squares = []
for n in numbers :
    squares.append(n*n)
print(squares)

numbers = [1,2,3,4,5]
squares = [n*n for n in numbers]
print(squares)

ports = [21,22,80,443,3306,8080,8443]
high_ports = [port for port in ports if port > 1000]
print(high_ports)

ports = [21,22,80,443,3306,8080,8443]
suspicious = [21, 3306, 8080]
flagged = [port for port in ports if port in suspicious]
print (f"suspicious ports found : {flagged} ")
