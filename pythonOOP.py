class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        print("Hello!" + self.name) 

    def __str__(self):
        return f"{self.name}({self.age})"
    
    

class Student(Person):
    def __init__(self, name,age, major):
        super().__init__(name, age)
        self.major = major

    def marks(self):
        print("The student got 30 out of 50!")

class Driver(Person):
    def __init__(self, name, age, vehicle):
        super().__init__(name, age)
        self.vehicle = vehicle

    def distance(self):
        print("The driver has drived over 100,000 miles")



s1 = Student("John",30, "Science")
d1 = Driver("rahul",43, "Truck")

s1.marks()
d1.distance()

