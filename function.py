def greet(name, age) :
    print(f"hello {name}, you are {age} years old.")

greet("Anish", 26)
greet("Raj", 22)

def greet(name, age = 18) :
    print (f" Hello {name} , you are {age} years old.")

greet("anish", 26)
greet("Raj")

def create_user(username, role = "viewer", active = "true") :
    print ( f" User: {username} | Role: {role} | Active: {active}")

create_user ("Anish", "Admin", "True")
create_user ("Raj", "Admin")
create_user ("Kishore")