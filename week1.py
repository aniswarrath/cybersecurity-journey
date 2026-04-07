username = input("Username: ").lower()
password = input("Password: ")

if username == "anish" and password == "secure123": 
    print ("Access granted. Welcome Anish.")
elif username == "anish" and password != "secure123":
    print("Wrong password. Access denied.")
else : print("Unknown user. Access denied.")