class Employee:

    num_of_emps: 0
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
        
    

    
emp_1 = Employee('Corey', 'kc', 50000)
emp_2 = Employee("Test", "user", 60000)


import datetime
my_date = datetime.date(2016, 7, 14)

print(Employee.is_workday(my_date))
