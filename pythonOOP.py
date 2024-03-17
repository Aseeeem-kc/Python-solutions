from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__lifeexp = 80


    def sayHi(self):
        print("Hello!" + self.name) 

    def __repr__(self):
        return f"from repr method: {self.name}({self.age})"

    # def __str__(self):
    #     return f"from str method: {self.name}({self.age})"

    def setLifeexp(self, exp):
       self.__lifeexp = exp

    def getLifeexp(self):
        print(self.__lifeexp)
    
    
    
    

class Student(Person):
    def __init__(self, name,age, major):
        super().__init__(name, age)
        self.major = major

    def setLifeexp(self, exp):
       self.__lifeexp = exp

    def getLifeexp(self):
        print(self.__lifeexp)

   

    def marks(self):
        print("The student got 30 out of 50!")

    def spendTime(self):
        print("A student spends most of his time studying")




class Driver(Person):
    def __init__(self, name, age, vehicle):
        super().__init__(name, age)
        self.vehicle = vehicle

    def distance(self):
        print("The driver has drived over 100,000 miles")

    def spendTime(self):
        print("A driver spends most of his time driving")
    
    def setLifeexp(self, exp):
       self.__lifeexp = exp

    def getLifeexp(self):
        print(self.__lifeexp)



# s1 = Student("John",30, "Science")
# d1 = Driver("rick",43, "Truck")

# s1.spendTime()
# d1.spendTime()
        
# person1 = Student("bob", 30, "Computer")
# person1.setLifeexp(60)
# person1.getLifeexp()
# print(person1) # str method (prints out repr method if no str is called)
# print([person1]) # repr method



  
# Create Abstract base class 
class Car(ABC): 
  def __init__(self, brand, model, year): 
    self.brand = brand 
    self.model = model 
    self.year = year 
      
  # Create abstract method       
  @abstractmethod
  def printDetails(self): 
    pass
    
  # Create concrete method 
  def accelerate(self): 
    print("speed up ...") 
    
  def break_applied(self): 
    print("Car stop") 
      
# Create a child class 
class Hatchback(Car): 
    
#   def printDetails(self): 
#     print("Brand:", self.brand); 
#     print("Model:", self.model); 
#     print("Year:", self.year); 
    
  def Sunroof(self): 
    print("Not having this feature") 
      
# Create a child class 
class Suv(Car): 
    
  def printDetails(self): 
    print("Brand:", self.brand); 
    print("Model:", self.model); 
    print("Year:", self.year); 
    
  def Sunroof(self): 
    print("Available") 
  
ogcar = Car("Maruti", "Alto", "2022")
car1 = Hatchback("Maruti", "Alto", "2022"); 
  
# car1.printDetails()
car1.printDetails()