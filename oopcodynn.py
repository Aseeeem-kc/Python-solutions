

# part-1 -  intro to classes, creating instance and methods
# part-2 -  inheritance
# part-3 -  encapsulation
# part-4 -  polymorphism
# part-5 -  abstract


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.__mileage = 0


    # def set_mileage(self, mileage):
    #     self.__mileage = mileage

    # def get_service(self):
    #     if self.__mileage < 15:
    #         print ("Time for service")
    #     else:
    #         print("Not necesary to service the vehicle")

    # def start(self):
    #     print("vehile started")

    # def stop(self):
    #     print("vehicle stopped")
    
    # def drive(self):
    #     print("vehicle is moving forward")


class car(Vehicle):
    def __init__(self, brand, model, year, color, doors):
        super().__init__(brand, model, year, color)
        self.doors = doors
    
    def start(self):
        print("car started")

    def brought_in(self):
        print("i bought this in 2021")

# class bike(Vehicle):
    
#     def wheelie(self):
#         print("the rider did the wheelie")



vehicle = Vehicle("toyota", 123, 2020, "white")
vehicle.start()


car = car("honda", 123, 2020, "white", 5)
car.start()

        
