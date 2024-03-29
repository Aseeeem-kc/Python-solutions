class Employee:

    raise_amount = 1.04

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

emp1 = Employee('ashim', 'kc', 69000)
emp1.fullname = 'aseeeeem kc'
print(emp1.pay)
print(emp1.email)
print(emp1.fullname)


del emp1.fullname
print(emp1.email)