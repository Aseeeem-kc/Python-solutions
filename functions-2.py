# tutorial ques-1
'''
def check_divisibility(num):
    if num % 7 == 0:
        return "The number is divisble by 7"

print(check_divisibility(21))
'''

# ques-2
'''
def calculate_si(principle, time, rate):
    si =  (principle * time * rate) / 100
    return si
print(calculate_si(3000, rate=10, time=2)
'''

# ques-3
'''
def arith_operation(num1,num2,operation):
    if operation == "+":
        print("The output is ", num1 +  num2)
    elif operation == "-" :
        print("The output is ", num1 - num2)
    elif operation == "/":
        print("The output is ", num1 / num2)
    elif operation == "*":
        print("The output is ", num1 * num2)

def find_factorial(num):
    factorial = 1
    for i in range(1,num + 1):
        factorial = factorial * i
    print("The factorial is: ",factorial)

def find_mmm(operation, input_list):
    if operation == 'mean':
        total = sum(input_list)
        nums = len(input_list)
        mean = total/nums
        print("mean = ",mean)
    elif operation == 'median':
        input_list.sort()
        nums = len(input_list)

        if nums/2 == 0:
            first_mid = input.list[num//2]
            second_mid = input.list[num//2 + 1]
            median = (first_mid + second_mid)/2
            print("median = ", median)
        else:
            mid_num = input.list[num//2]
            print("median = ",mid_num)

find_mmm('mean', [1,2,3,4,5,6,7,8])

arith_operation(10,1,'+')

find_factorial(10);
'''



# home task question:
'''
def loginProgram():
    uid = input("Enter your username: ")
    pwd = input("Enter your password: ")
    login_track = 0

    while (login_track !=3):
        login_track += 1
        if (uid == 'ADMIN' and pwd == 'St0rE@1'):
            print("Login successful!")
            break;
            
        else:
            print("Try again!")
            uid = input("Enter your username: ")
            pwd = input("Enter your password: ")
            if login_track == 3:
                print("Too many unsuccessful attempts")
                break;
loginProgram()
'''

# for you exercise-1
'''
def swap_program(num1,num2):
    if num1 < num2:
        num1= num2
        return num1
    else:
        return num1,num2
print(swap_program(7,4))

    '''

# exercise- 2
'''
def mrms_name(name,gender):
    if (gender == 'm'):
        return "Mr."+ name
    else:
        return "Ms." + name

print(mrms_name('sita','f'))
'''

# for you addiotional exercise
import math

def calculate_square_area(side):
    return side ** 2

def calculate_square_perimeter(side):
    return 4 * side

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

def calculate_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius

print(calculate_cylinder_surface_area(5,90))
    
    
