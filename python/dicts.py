device = {
    "ip" : "192.188.1.1" , 
    "port" : 22 ,
    "protocol" : "TCP",
    "status" : 200 ,
}

for key , value in device.items():
    print(f"{key}:{value}")

network_scan = {
    "192.168.1.1" : {"port": 80, "status": "open"},
    "192.168.1.2" : {"port": 22, "status": "open"},
    "192.168.1.3" : {"port": 3306, "status": "closed"}
}
for ip, value in network_scan.items():
    print(f"\n- {ip} -")
    for ports , statuses in value.items():
        print(f"{value['port']} , {value['status']}")  
          

network = {
        "192.168.1.1" : {
             80: "HTTP",
             443: "HTTPS",
             53: "DNS"
        },
        "192.168.1.19" : {
             22: "SSH",
             8080: "HTTP-ALT"
        },
        "192.168.1.30" : {
             21: "FTP",
             3306: "MysQL"
        }
    }

for ip , ports in network.items():
    print(f"\n{ip}")
    for port , service_name in ports.items():
        print(f"{port} - {service_name}")