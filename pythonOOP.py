class Myfirstclass:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.addres = address


    def working(self):
        print('Im working')
    
    def eating(self):
        print('Im eating')


class Inheritedclass(Myfirstclass):
    def __init__(self, name, age, address, cilas):
        Myfirstclass.__init__(self, name, age, address)
        self.cilas = cilas

p1 = Inheritedclass('ashim', 18, 'pepsicola', 'secondsem')
print(p1.name)
print(p1.cilas)
p1.working()

