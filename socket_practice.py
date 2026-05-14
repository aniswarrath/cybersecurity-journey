import socket

def check_port(ip, port):
    try :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        result = sock.connect_ex((ip,port))
        sock.close()
        if result == 0:
            return True
        return False
    except Exception as e:
        return False

print(f"port 80 (HTTP): {check_port('8..8.8.8', 53)}")
print(f"Port 443 (HTTPS): {check_port('8.8.8.8', 9999)}")

import socket
print(f"Google DNS port 53: {check_port('8.8.8.8', 53)}")