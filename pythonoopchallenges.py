#  1. Set Student Name
# Create a class named Student with a method set_name to set the student's name

class Student:
    def set_name(self, name):
        self.name = name

# Example Usage:
student1 = Student()
student1.set_name("Alice")
print(student1.name)  # Output: Alice



# 2. Set Rectangle Height and Width
# Define a class called Rectangle with methods set_width and set_height to set the dimensions of the rectangle.

class Rectangle:
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

# Example Usage:
rectangle1 = Rectangle()
rectangle1.set_width(5)
rectangle1.set_height(10)
print(rectangle1.width, rectangle1.height)  # Output: 5 10


# 3. Add Numbers in Calculator Class
# Create a class named Calculator with a method add to add two numbers.

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

# Example Usage:
calculator1 = Calculator()
result = calculator1.add(3, 5)
print(result)  # Output: 8



