#PART-2

# 1
'''
for i in range(1,11,1):
    print(i)
'''

# 2
'''
for i in range(3,15,2):
    print(i)
'''

# 3
'''
sum = 0
for i in range(1,11,1):
    sum = sum+i
print(sum)
'''

# 4
'''
num = int(input('Enter a positive integer: '))
for i in range(11):
    mul = num * i
    print(f'{num} X {i} = {mul}')
'''

# 5
'''
num = int(input("Enter any number: "))
for i in range(1,num):
    num = num * i
print(num)
'''

# 6
'''
num =input('Enter any number: ')
positive = 0
negative = 0
zeros = 0
while (num != ""):
    
    if (int(num)>0):
        positive = positive + 1
    elif (int(num)<0):
        negative = negative + 1
    elif (int(num) == 0):
        zeros = zeros + 1
    num = input('Enter a number again: ')
print (f"positive number = {positive}\nnegative number = {negative}\nzeros = {zeros}")
'''

# 7
'''
n = int(input("Enter the limit"))
a = 0
b = 1
t = 0
while (a <= n):
    print (a)
    t = a
    a = b
    b = b + t

print(f"fibonacci series upto {n} is over.")
    
'''

# 8
'''
user_input = input("Enter any string: ")
print(user_input[::-1])
'''

# 9
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end="")
    print()
'''

#PART-3

# 1
'''
add = 0
for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
        add = add + i
print(add)
'''

# 2

# string slicing using string notation
'''
user_input = input("Enter any number or string: ")
if (user_input == user_input[::-1]):
    
    print("It is palindrome")
else:
    print("It is not palindrome")
'''


# 3 - a
'''
addition = 0
for i in range(100,201):
    if (i % 2 == 0):
        addition += i
print(addition)
'''

# 3 - b
'''
user_input = input("Enter any number: ")
numsum = 0
while (user_input != ""):
    if (int(user_input) <= 100):
        numsum += int(user_input)
        user_input = input("Enter any number again: ")
    else:
        user_input = input("Enter any number again: ")
print (numsum)
'''

# 3 - c
'''
while (True):
    addition = 0
    for i in range(100,201):
        if (i % 2 == 0):
            addition += i
        elif(i % 2 == 1):
            continue
    print(addition)
    break
'''

# 4
'''
product = 1
num = int(input("enter first number: "))
while (num != 0):
    product = product * num
    num = int(input("enter another number: "))
print(f"the product is {product}")
'''

# 6
'''
largest_number = 0
user_input = int(input("Enter a number"))
while (user_input > 0): 
    digit = user_input % 10 
    if (digit > largest_number):
        largest_number = digit
    user_input = user_input // 10
print(largest_number)
'''

# 7
'''
user_input = input("Enter a string")
vowel_count = 0
 
for i in range(len(user_input)):
    if (user_input[i] in 'aeiouAEIOU'):
        vowel_count += 1
print(vowel_count)
'''

# 8
'''
import random as r
computer_num = r.randint(1,21)

player_attempt = 0
for i in range(1,6):
    player_guess = int(input("Guess the number: "))
    if (player_guess == computer_num):
        print('Congrats! you won the game')
        break;
    elif (player_guess<computer_num):
        print('Too low')
        player_attempt +=1
    elif (player_guess>computer_num):
        print('Too high')
        player_attempt +=1
'''

#PART-4

# 1
# PART-4

# 1
'''
num1 = input("enter first number: ")

while (num1 !="q"):
    num2 = input("enter second number: ")
    if (num2 !="q"):
        oper = input("enter the operator(addition,subtraction,multiplication or division): ")
        if (oper == "+"):
            print(f"{num1} + {num2} = {int(num1)+int(num2)}")
        elif (oper == "-"):
            print(f"{num1} - {num2} = {int(num1)-int(num2)}")
        elif (oper == "*"):
            print(f"{num1} * {num2} = {int(num1)*int(num2)}")
        elif (oper == "/"):
            print(f"{num1} / {num2} = {int(num1)/int(num2)}")
        num1 = input("enter first number: ")
    else:
        break;
print('The calculator program is over')
'''

# 2

'''
import random as r

roll = input("Enter 'roll' to roll the two dices.")
if (roll == "roll"):
    dice1 = r.randint(1,7);
    dice2 = r.randint(1,7);
    sumDice = dice1 + dice2
player_guess = input("Enter your guess: ")

while (int(player_guess) != sumDice):
    player_guess = input("Enter your guess again: ")
print("You guessed it correctly!")
'''

# 3
'''
user_quit = "";
guess = 1
guess_p = 0
while (user_quit!="q" ):
    import random as r

    roll = input("Enter 'roll' to roll the two dices.")
    if (roll == "roll"):
        dice1 = r.randint(1,6);
        dice2 = r.randint(1,6);
        sumDice = dice1 + dice2
    else:
        print('Invalid input')
    player_guess = input("Enter your guess: ")
    

    while (int(player_guess) != sumDice):
        guess += 1
        guess_p = round(((12-guess)/12)*100)
        player_guess = input("Enter your guess again: ")
    print("You guessed it correctly!")
    print(f"You took {guess} rounds to guess the sum of two dices.")
    print(f"Your guessing percentage is {guess_p}%")
    user_quit= input("Enter 'q' to exit the game.")
    
print('The game is over')
'''




