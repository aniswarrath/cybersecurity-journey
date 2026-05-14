try :
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100/ {number} = {result}")
except ValueError:
    print("Error - please enter a number not text")
except ZeroDivisionError :
    print("error - cannot divide by zero")