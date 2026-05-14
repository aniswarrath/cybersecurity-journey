'''i = 1
while i < 6 :
    print(i)
    i+=1

# 2
attempts = 0
while True :
    password = input("Enter password: ")
    attempts += 1
    if password == "secure123":
        print(f"Access granted in {attempts} attempt(s)")
        break
    print("Wrong password, try again.")

#3
attempts = 0
max_attenmpts = 3
while True :
    password = input("Enter password : ")
    attempts += 1
    if password == "secure123":
        print(f"Access granted in {attempts} attempts.")
        break
    if attempts >= max_attenmpts :
        print("Account blocked! Too many wrong attempts.")
        break
    print("Wrong. Try again")

#4 
numbers = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(numbers) :
    m = numbers[i]
    i += 1
    if i % 2 == 0:
        print(The number)

password = input("Password: ").strip()
if len(password) <= 3 :
    print("Too short")
if len(password) >= 20 :
    print("Too long")

name = "Aniswar Rath"
print(name.startswith("Mr "))

ips = ["100.120.1.1" , "100.120.1.2" , "100.120.1.3", "100.120.1.4" , "101.120.1.5" ]
for ip in ips :
    if ip.startswith("100"):
        print (f"This {ip} is in our netowrk.")
name = "Aniswar Rath"
print(name[::-1])



ports = ["220" , "221" , "222" , "223" , "224" , "225"]
for port in ports :
    if int(port) % 2 == 0 :
        print(f"The port {port} is even.")
    else :
        print(f"The port {port} is odd.") 

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for num in numbers :
    if num % 3 == 0 and num % 5 == 0 :
        print (f"The number {num} is divisible both by 3 and 5.")
    else :
        print (f"The number {num} is not divisible both by 3 and 5.") 


username = input("Enter the username :").lower().strip()
password = input("Enter the password :").strip()
if username != "anish" or password != "secure123":
    print ("Wrong credentials entered. Try again. ")
elif username == "anish" and password != "secure123":
    print ("Wrong password entered. Try again. ")
elif username == "anish" and password == "secure123":
    print ("Access granted. ")'''

hacker = {
    "name": "Anish",
    "age": 26,
    "role":"pentester"
}
print(hacker["name"])
print(hacker["role"])

hacker["city"]= "BHubaneswar"
print(hacker)

hacker["city"]= "Bhubaneswar"
hacker["age"] = 27
del hacker["role"]
print(hacker)

for key, value in hacker.items():
    print(f"{key}:{value}")
    print(hacker.keys())
    print(hacker.values())

for key in hacker.keys():
    print(key)
for value in hacker.values():
    print(value)



target = {
    "ip": "192.168.1.1",
    "open_ports" : [80, 443, 22],
    "os" : "Linux",
    "vulnerable": True
}

for key,value in target.items():
    print(f"{key}:{value}")

import datetime
target["last_seen"]= str(datetime.datetime.now())
for key,value in target.items():
    print(f"{key}:{value}")

scan_results = {
    "192.168.1.1" : ["80","443","22"],
    "192.168.1.2" :["21","3306"],
    "192.168.1.3" : []
}
for ip, ports in scan_results.items():
    print(f"\nIP: {ip}")
    for port in ports:
        print(f" Port: {port}")