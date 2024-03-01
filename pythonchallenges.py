# difficulty-1

# String reverse

def string_reverse(string :str):
    return string[::-1]



# palindrome number

def palindrome_check(string:str):
    if string[::-1] == string:
        return True
    else:
        return False


# Count Vowels
# Write a function that counts the number of vowels in a given string.
def count_vowels(string:str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


# Check Even or Odd
# Write a function to determine if a given number is even or odd.
def odd_even(num: int):
    return num % 2 == 0



#Fibonacci Sequence
# Write a function to generate the Fibonacci sequence up to a certain number of terms.
def fibonacci_series():
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 10:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence
    



# Check Prime
# Write a function to check if a given number is prime.
import math

def is_prime(n: int):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        sqrt_n = int(math.sqrt(n))
        for i in range(5, sqrt_n + 1):
            if n % i == 0:
                return False
        return True


    


#Count Words in a Sentence
#Write a function to count the number of words in a given sentence.
def count_words(sentence: str):
    return len(sentence.split())


# Reverse Array

a = [1,2,3,4,5]
print(a[::-1])


# if __name__ == '__main__':
    # print(stringReverse("12435"))
    # print(palindrome_check("1221"))
    # print(odd_even())
   
    # print(fibonacci_series())
    # print(is_prime(99))
    # print(count_words("   the    fun game   "))



