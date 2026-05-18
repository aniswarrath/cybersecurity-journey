try:
    filename = input("Enter filename - ")
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error- file not found")
finally:
    print("operation completed")