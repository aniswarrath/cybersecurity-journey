
'''# just testing the pythons code that works similar to echo:
with open("output.txt", "w") as file :
     file.write("First line\n")
with open("output.txt", "a") as file :
     file.write("Second line\n")'''

# Exercise 1 - Write to file 
with open("log.txt", "w") as f:
    f.write("Aniswar Rath\n")
    f.write("May 14, 2026\n")

#Exercise 2 - read from the File
with open("log.txt","r") as f:
    content = f.read()
    print(content)

#Exercise 3 - Append mode:
with open("log.txt", "a") as f:
     f.write("Day 65 of 400\n")
with open("log.txt", "r") as f:
     content = f.read()
     print(content)

#Exercise 4 - r+
with open("log.txt", "r+") as f :
     content = f.read()
     f.write("\nNew line")
     f.seek(0)
     updated = f.read()
     print(updated)

#Exercise - Missed - finallly keyword in the errorhandeling
try : 
     with open("log.txt","r") as f:
          content = f.read()
          print(content)
except FileNotFoundError:
     print("Error - file not found")
except FileExistsError:
     print("Error- file does not exist.")
finally:
     print("File operation complete - always runs")

sock = socket.socket()
try:
    result = sock.connect_ex((ip, port))
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()  # socket ALWAYS closes — no matter what happened