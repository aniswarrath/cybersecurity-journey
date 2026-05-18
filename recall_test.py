ports = [80, 443, 22,21, 3036, 8080,9999, 135, 25, 53]
services = {80: "HTTP" , 443 : "HTTPS" , 22: 'SSH', 21: "FTP", 53: "DNS"}

for port in ports :
    service = services.get(port, "Data not available")
    print(f"Port {port} - {service}")