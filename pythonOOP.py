class Employee:

    raise_amount = 1.04

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    

    def __add__(self, other):
        return self.pay + other.pay
        

class Developer(Employee):
    raise_amount = 1.10

    def __init__ (self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang
    

class Manager(Employee):
     
    def __init__ (self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)   

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


    
dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'Employee', 60000)
dev_3 = Developer('kc', 'ashim', 69000, 'bhailang')

print(dev_1 + dev_2)
# print(help(Developer))

# mgr_1 = Manager("sue", "smith", 90000, [dev_1,dev_2])

# print(mgr_1.email)
# mgr_1.add_emp(dev_3)
# # mgr_1.remove_emp(dev_2)

# mgr_1.print_emps()

# # print(dev_1.lang)
# # dev_1.apply_raise()
# # print(dev_1.pay)


# print(issubclass(Manager, Developer))

# print(dev_1)

print(repr(dev_1))
print(str(dev_1))