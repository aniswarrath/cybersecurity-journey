user = {
    "name" : "Anish",
    "age" : 26,
    "role" : "admin",
    "active" : True
}
print(user)
print(user["name"])
print(user["role"])
print(user["age"])

#adding, updating and deleting
user = {
    "name" : "Anish",
    "age" : 26,
    "role" : "admin"
}
user["email"] = "anish@gmail.com"
print(user)

user ["role"] = "superadmin"
print(user)

del user ["age"]
print(user)

# dictionary methods
user = {
    "name" : "Ansih",
    "age": 26,
    "role": "admin"
}
print(user.keys())
print(user.values())
print(user.items())

# looping through a dictionary:
user = {
    "name": "Anish",
    "age" : 26 ,
    "role": "admin"
    }
for key, value in user.items():
    print(f"{key}: {value}")

# how this is used in security 
scan_results = {
    "target": "192.168.1.1",
    "open_ports": [22, 80, 443],
    "os": "Linux",
    "vulnerable": True
}
for key, value in scan_results.items():
    print(f"{key}: {value}")

# nested dictionaries
users = {
    "anish": {
        "role": "admin",
        "active": True
    },
    "raj" : {
        "role": "viewer",
        "active": False
    }
}
print(users["anish"])
print(users["anish"]["role"])
print(users["raj"]["active"])

''' Create a dictionary called network_devices with 3 devices. Each device should have:

ip address
type (router, switch, firewall)
status (online/offline) '''

network_devices = {
    "device1" : {
        "ip" : "100.101.1.2",
        "type" : "router",
        "status" : "online"
    },
    "device2" : {
        "ip" : "100.101.1.3",
        "type" : "switch",
        "status" : "offline"
    },
    "device3" : {
        "ip" : "100.101.1.3",
        "type" : "firewall",
        "status" : "online"
    }
}
for device, details in network_devices.items():
    print(f"\nDevice:{device}")
    for key, value in details.items():
        print(f" {key} : {value}")
