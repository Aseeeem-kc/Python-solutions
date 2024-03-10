from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = 0


    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

    def make_sound(self):
        pass
    



# class Car(Vehicle):
#     def make_sound(self):
#         print("ghuiii")

# class bike(Vehicle):
#     def make_sound(self):
#         print("vhroom")

# my_vehichle = Vehicle(1,2,3)
# my_vehichle.set_price("50 lakhs")
# print(my_vehichle.get_price())
    
my_vehicle = Vehicle("hi",1,2)
# my_car = Car(1,2,3)
# my_bike = bike(1,2,3)
my_vehicle.make_sound()
# my_bike.make_sound()





# class Car(Vehicle):
#     def make_sound(self):
#         print("ghuiii")

# class bike(Vehicle):
#     def make_sound(self):
#         print("vhroom")

# my_vehichle = Vehicle(1,2,3)
# my_vehichle.set_price("50 lakhs")
# print(my_vehichle.get_price())
    
my_vehicle = Vehicle("hi",1,2)
# my_car = Car(1,2,3)
# my_bike = bike(1,2,3)
my_vehicle.make_sound()
# my_bike.make_sound()



