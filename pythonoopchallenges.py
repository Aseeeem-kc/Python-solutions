# 1. Point Class
# Define a class Point with __init__ method setting coordinates (x, y). Create an instance, print its coordinates.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(3, 4)
print(point1.x, point1.y)  # Output: 3 4


# 2. Person Class
# Create a class to represent a person with attributes for name and age. Instantiate the class with the name 'John' and age '30', then print the details

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John", 30)
print(person1.name, person1.age)  # Output: John 30


#  3 . Set Student Name
# Create a class named Student with a method set_name to set the student's name

class Student:
    def set_name(self, name):
        self.name = name

# Example Usage:
student1 = Student()
student1.set_name("Alice")
print(student1.name)  # Output: Alice



# 4. . Set Rectangle Height and Width
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


# 5. Add Numbers in Calculator Class
# Create a class named Calculator with a method add to add two numbers.

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

calculator1 = Calculator()
result = calculator1.add(3, 5)
print(result)  # Output: 8




# 6. BanK Account Class
# Define a class called BankAccount with methods set_balance and deposit to manage a bank account's balance.

class BankAccount:
    def set_balance(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

# Example Usage:
account1 = BankAccount()
account1.set_balance(1000)
account1.deposit(500)
print(account1.balance)  # Output: 1500



# 7. Student Class with Method
# Create a Student class with __init__ method initializing name and age. Implement a method display_info() to print student details. Create an instance, call the method.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Alice", 20)
student1.display_info()  
# Output:
# Name: Alice
# Age: 20




# 8. BankAccount Class with Methods
# Define a BankAccount class with __init__ method setting account balance. Implement methods deposit() and withdraw() to modify balance. Create an instance, deposit some money, withdraw some money, and print the final balance.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

account1 = BankAccount(1000)
account1.deposit(500)
account1.withdraw(200)
print("Final Balance:", account1.balance)  # Output: Final Balance: 1300



# 9. Temperature Converter Class
# Create a TemperatureConverter class with __init__ method setting temperature in Celsius. Implement methods to_fahrenheit() and to_kelvin() to convert temperature. Create an instance, convert the temperature to Fahrenheit and Kelvin, and print the results.

class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15

temp = TemperatureConverter(25)
print("Temperature in Fahrenheit:", temp.to_fahrenheit())  # Output: Temperature in Fahrenheit: 77.0
print("Temperature in Kelvin:", temp.to_kelvin())          # Output: Temperature in Kelvin: 298.15


# 10. Employee Class with Salary Calculation Method
# Define an Employee class with __init__ method setting employee's name and hourly rate. Implement a method calculate_salary(hours) to calculate the employee's salary based on hours worked. Create an instance, calculate the salary for 40 hours worked, and print the result.

class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate
    
    def calculate_salary(self, hours):
        return self.hourly_rate * hours

employee1 = Employee("John", 20)
salary = employee1.calculate_salary(40)
print("Salary for 40 hours worked:", salary)  # Output: Salary for 40 hours worked: 800


# completed creating bundle