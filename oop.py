class PortScanner:

    def __init__(self, target):
        self.target = target
        self.open_ports = []
        print(f"Scanner created for: {self.target}")

    def scan(self, port):
        print(f"Scanning {self.target} on port {port}")

    def show_results(self):
        print(f"Open ports: {self.open_ports}")


scanner = PortScanner("192.168.1.1")
scanner.scan(80)
scanner.scan(443)
scanner.show_results()

class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says : woof!")

dog1 = Dog("Bruno")
dog2 = Dog("Max")

dog1.bark()
dog2.bark()


class Dog:
    def __init__(self, name):
        print(f"A dog name {name} was created")
dog1 = Dog("Bruno")


class Student:
    def __init__(self, name, status):
        self.name = name 
        self.status = status
        print(f"{self.name} is {self.status} today")

    def attend(self):
        if self.status == "Present":
            print(f"{self.name} attended the class")
        else: 
            print(f"{self.name} missed the class")

student1 = Student("Anish", "Present")
student2 = Student("Abhi", "Present")
student3 = Student("Anshu", "Absent")
student4 = Student("Anisha", "Absent")

student1.attend()
student2.attend()
student3.attend()
student4.attend()