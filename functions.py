# 1


def avg (num1, num2, num3):
   ''' takes 3 numbers as parameters and gives out their average'''
   return (num1 + num2 + num3) / 3.0

n1 =37
n2 = 108
n3 = 67
n4 =12
n5 = 10
print(avg(n1, n2, avg(n3, n4, n5)))


# 2

def types(num):
   '''takes a number as param and prints it as float and integer'''
   print(int(num))
   print(float(num))

types(5)

# 3

def squared(numtobesquared):
   print(numtobesquared **2)
squared(2)


# 4

def int_to_string(intval):
   strval =str(intval)
   print(strval)
   print(type(strval))
int_to_string(7)


# 5

def hello_world(name):
   print(f"Hello world, my name is {name}")

hello_world("asim")


# 6

from statistics import mean, median, mode
def improved_average(n1,n2,n3,n4,n5):
   Mean = mean([n1,n2,n3,n4,n5])
   print(Mean)

   Median = median([n1,n2,n3,n4,n5])
   print(Median)

   Mode = mode([n1,n2,n3,n4,n5])
   print(Mode)

improved_average(5,7,8,5,13)


# 7

def divide():
   num1 = int(input("Enter first number"))
   num2 = int(input("Enter second number"))

   result = num1/num2

   print(f"{result:.2f}")
divide()
    

# 8

def addition(num1,num2):
   '''This function adds the two numbers'''
   print(num1+num2)

def subtraction(num1,num2):
    '''This function subtracts the two numbers'''
    print(num1-num2)
   

def multiplication(num1,num2):
    '''This function multiplies the two numbers'''
    print(num1*num2)

def division(num1,num2):
   '''This function divides number 1 with number 2'''
   print(num1/num2)

def modulus(num1,num2):
   '''This function gives modulus of the given two numbers'''
   print(num1%num2)

def exponentiation(num1,num2):
   ''' this function gives exponentiation of num1 to num2'''
   print(num1**num2)


addition(4,3)
exponentiation(4,2)

help(addition)

# 9

def grade_calculation():
    sub1 = int(input("Enter your grade in sub1"))
    sub2 = int(input("Enter your grade in sub2"))
    sub3 = int(input("Enter your grade in sub3"))
    sub4 = int(input("Enter your grade in sub4"))
    sub5 = int(input("Enter your grade in sub5"))

    total_marks_obtained = sub1 + sub2 + sub3 + sub4 + sub5
    total_marks_possible = 100 * 5
    percentage = (total_marks_obtained / total_marks_possible)*100

    print(f"{percentage:.2f}%")

grade_calculation()




