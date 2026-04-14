
# just testing the pythons code that works similar to echo:
with open("output.txt", "w") as file :
     file.write("First line\n")
with open("output.txt", "a") as file :
     file.write("Second line\n")
