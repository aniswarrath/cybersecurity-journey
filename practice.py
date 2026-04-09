pin = 1234
attempts = 0
while attempts < 3 :
    guess = int(input("Enter the pin number"))
    attempts += 1

    if pin == guess :
        print ("Access granted!")
        break
    elif attempts < 3:
        print (f"Wrong pin, {3-attempts} attempts remaining.")
    else :
        print("Card blocked")