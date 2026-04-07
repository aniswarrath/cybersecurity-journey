username = input("Username: ").lower()
password = input("Password: ")

if username == "anish" and password == "secure123": 
    print ("Access granted. Welcome Anish.")
elif username == "anish" and password != "secure123":
    print("Wrong password. Access denied.")
else : print("Unknown user. Access denied.")

#while loop with break
attempts = 0
while True :
    password = input("Enter password: ")
    attempts += 1
    if password == "secure123" :
        print(f"Access granted after {attempts} attempt(s)")
        break
    if attempts >= 3 :
        print("Account locked. Too many attempts. ")
        break
    print("Wrong password. Try again. ")

    # practice 
    ports = [21, 22, 80, 443, 0, 8080, 65536]

    for port in ports :
        if port <= 0 or port > 65536 :
            continue 
        print(f"scanning port {port}")
        