# Network scanner - project 1

targets = {
    "192.168.1.1" : {"hostname": "router", "ports" : []},
    "192.168.1.2": {"hostname": "server", "ports": []},
    "192.168.1.3": {"hostname": "workstation", "ports": []}
}

common_ports = [21, 22, 80, 443, 3306, 8080]

def scan_ports(ip, ports):
    open_ports = []
    for port in ports :
        if port in [22, 80, 443]:
            open_ports. append(port)
    return open_ports

def display_results(targets):
    print("\n === SCAN RESULTS === ")
    for ip , details in targets.items():
        print(f"\nIP : {ip}")
        print(f"Hostname : {details['hostname']}")
        if details['ports']:
            print(f"Open Ports : {details['ports']}")
        else:
            print("No open ports found")

for ip in targets :
    open_ports = scan_ports (ip, common_ports)
    targets[ip]["ports"] = open_ports
display_results(targets)