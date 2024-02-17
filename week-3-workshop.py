# Part-2

#1 Develop a program that asks the user for a number
#  and then displays whether the number is positive or negative.
'''
num = int(input('enter any num'))

if (num >0):
    print('The number is positive')
else:
    print('The number is negative')
'''

#2 Write a Python program that reads in two numbers
# and prints out whether their sum is even or odd.

'''
a = int(input('enther the first number: '))
b = int(input('enter the second number: '))
sum = a + b
if (sum % 2 == 0):
    print('The sum of the numbers is even')
else:
    print('The sum of the numbers is odd')
'''

#3) Write a program to find the lowest number out
# of two numbers expected from the user.

'''
num1 = int(input('enter the first number'))
num2 = int(input('enter the second number'))
if (num1 > num2):
    print('The second number is lowest among the two numbers')
else:
    print('The first number is lowest among the two numbers')
'''


#4)Write a program to check whether a character is a vowel
#  or consonant. [Expected from user’s input].
    
'''
character = input('enter a character: ')
vowels = ['a','e','i','o','u','A','E','I','O','U']
if (character in vowels):
    print('the character is vowel')
else:
    print('the character is consonant')
'''

#5) Accept the age of 4 people and display the oldest one.
'''
person1 = int(input('enter the age of the first person'))
person2 = int(input('enter the age of the second person'))
person3 = int(input('enter the age of the third person'))
person4= int(input('enter the age of the fourth person'))

if (person1 > person2 and person1 > person3 and person1 > person4):
    print('First person is the oldest one')
elif (person2 > person1 and person2 > person3 and person2 > person4):
    print('second person is the oldest one')
elif (person3 > person1 and person3 > person2 and person3 > person4):
    print('second person is the oldest one')
else:
    print('Fourth person is the oldest one')
'''

#6) Write a program that takes three numbers as input and outputs the
# largest of the three numbers using if-else statements. For example, if
# the inputs are 4, 7, and 2, the program should output 7.
'''
num1 = int(input('enter the first number: '))
num2 = int(input('enter the second number: '))
num3 = int(input('enter the third number: '))

def lowerChecking(num1,num2,num3):
    if (num1 > num2 and num1 >num3):
        print(num1)
    elif (num2 > num1 and num2 > num3):
        print(num2)
    else:
        print(num3)

lowerChecking(num1,num2,num3)
'''

#7) Write a Python program to calculate the difference between
# a given number and 17. If the number is greater than 17,
# return twice the absolute difference.

'''
num = int(input('enter the number'))
if (num <= 17):
    diff = 17 - num
    print(diff)
elif(num > 17):
    diff = num -17
    print(diff*2)
'''

#8) Give an appropriate if statement for each of the following
#  (the value of num is not important):
#  (a) Displays 'within range' if num is between 0 and 100, inclusive.
#  (b) Displays 'within range' if num is between 0 and 100, inclusive, and displays 'out of range' otherwise.

'''
num = int(input('enter the number'))
if (num in range(1,100)):
    print('within range')
else:
    print('out of range')
'''

#9 9)	Rewrite the following if-else statements using a single if
# statement and elif:
 #if temperature >= 85 and humidity > 60:
# print ('muggy day today')
# else:
# if temperature >= 85:
# print ('warm, but not muggy today')
# else:
# if temperature >= 65:
# print ('pleasant today')
# else:
# if temperature <= 45:
# print ('cold today')
# else:
# print ('cool today')

'''
temperature = 98
humidity = 66

if (temperature >= 85 and humidity > 60):
    print('muggy day today')
elif (temperature >=85 ):
    print('warm, but not muggy today')
elif (temperature <= 45):
    print('cold today')
elif (temperature <85):
    print('cool today')
'''


# PART-3

#1. Write a program that takes the name and age of the user
#as input and displays a message whether the user is eligible
#to apply for a driving license or not.  (The eligible age is 18 years).
'''
#asking user for input (name and age)
name = input("enter your name")
age = int(input("enter your age"))
# checking the eligibility using if else
if (age >= 18):
    print(f'You are eligible for a driving licence, {name}')
else:
    print(f'Your are not eligible for a driving licence, {name}')
'''

#2.	Write a Python program that prompts the user to enter
# their weight in kilograms and their height in centimeters.
# The program should then calculate the user's BMI (Body Mass Index)
#using the formula: BMI = weight / height^2.
# The resulting BMI value should be printed to the
#console along with a message indicating whether the
#user is underweight (BMI < 18.5), normal weight (18.5 <= BMI < 25),
#overweight (25 <= BMI < 30), or obese (BMI >= 30).

'''
weight = float(input('enter your weight in kilogram'))
height_cm = float(input('enter your height in centimeters'))

height = height_cm / 100

BMI = weight / (height**2)
print(round(BMI,2))

if (BMI < 18.5):
    print('You are underweight')
elif (BMI < 25):
    print('Normal weight')
elif (BMI < 30):
    print('overweight')
elif (BMI >= 30):
    print('obese')
'''

#3.Write a Python program to sum two given integers.
# However, if the sum is between 15 and 20 it will return 20.

'''
num1 = int(input('enter first integer'))
num2 = int(input('enter second integer'))

sum = num1 + num2

if (sum <20 and sum>15):
    print(20)
else:
    print(sum)
'''

#4. Accept the marked price from the user and calculate the
# Net amount as (Marked Price - Discount) to pay according to
# the following criteria.
'''
marked_price = int(input('enter the marked price'))

if (marked_price > 10000):
    discount = (20/100)* marked_price
    print(marked_price - discount)
elif marked_price > 7000 and marked_price <= 10000:
    discount = (15/100)* marked_price
    print(marked_price - discount)
else:
    discount = (10/100)*marked_price
    print(marked_price - discount)
'''

# 5.Accept the age and gender, number of days
# and displays the wages accordingly:
'''
age = int(input('Enter the age: '))
gender = input('Enter your gender(M for male, F for female): ')
no_of_days = int(input('Enter the number of days: '))

if (age >= 18 and age <30):
    if (gender == 'M'):
        wage = 700 * no_of_days
        print(wage)
    elif (gender == 'F'):
        wage = 750 * no_of_days
        print(wage)

elif (age >=30 and age <= 40):
    if (gender == 'M'):
        wage = 800 * no_of_days
        print(wage)
    elif (gender == 'F'):
        wage = 850 * no_of_days
        print(wage)
'''

# 6-a

'''
string = input('Enter A,B or C: ')

if (string == 'A' or string == 'B' or string == 'C'):
    if (string =='A'):
        print('Apple')
    elif (string =='B'):
        print('Banana')
    elif (string == 'C'):
        print('Coconut')
else:
    print('Invalid input')
'''

# 6-b

'''
credit = int(input('enter your credit: '))

if (credit >= 90):
    print('Senior status')
elif (credit >= 60):
    print('Junior status')
elif (credit >=30):
    print('Sophomore status')
else:
    print('Freshman status')
    
'''

# 6-c

'''
num = int(input('Enter any num'))

if (num % 3 == 0 and num % 5 == 0):
    print('FizzBuzz')
elif (num % 3 == 0):
    print('Fizz')
elif (num % 5 == 0):
    print('Buzz')
'''


# PART-4

#1
'''

units = int(input('Enter the electric units: '))


if (units < 100):
     print(f'The electric bill is rs. 0 ')
else:
    if (units>100 and units <= 300):
        fee = (units-100)*2
        print(f'The electric bill is rs.{fee} ')
    elif (units > 300):
        fee = (200*2)+(units - 300)*5
        print(f'The electric bill is rs.{fee} ')

'''

#2.  Write a program that takes n number as user input,
 #   which determines the size of the grid to be output.

'''
num = int(input('Enter the size of the grid'))
for i in range(1,num+1,1):
     for j in range (1,num+1,1):
          print(i*j,end = " ")
     print (" ")
'''
