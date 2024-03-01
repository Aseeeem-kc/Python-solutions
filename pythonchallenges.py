# difficulty-1

# String reverse

def string_reverse(string :str):
    return string[::-1]
# done



# palindrome number

def palindrome_check(string:str):
    if string[::-1] == string:
        return True
    else:
        return False
# done


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
# done


#Fibonacci Sequence
# Write a function to generate the Fibonacci sequence up to a certain number of terms.
def fibonacci_series():
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 10:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence
    # done




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
# done


    


#Count Words in a Sentence
#Write a function to count the number of words in a given sentence.
def count_words(sentence: str):
    return len(sentence.split())
# done







# Reverse Array
def reverse_array(my_list):
    result = (my_list[::-1])
    return result
# done

#find_maximum

def find_maximum(my_list):
    return max(my_list)


# find minimum
def find_minimum(my_list):
    return min(my_list)



# find Amstrong number:

def is_armstrong(number):
    num = number
    num_digits = 0
    while num > 0:
        num_digits += 1
        num //= 10
    
    armstrong_sum = 0
    num = number
    while num > 0:
        digit = num % 10
        armstrong_sum += digit ** num_digits
        num //= 10
    
    return armstrong_sum == number



# Remove duplicates

def remove_duplicates(my_list):
    return list(set(my_list))


# check anagram

def check_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2


# count characters

def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count



# check perfect number
def is_perfect_number(number):
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number



# array sum

def array_sum(my_list):
    return sum(my_list)



# find average

def find_average(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)
    


#  factorial finder

def factorial_finder(number):
    if number < 0:
        return None
    if number == 0:
        return 1  
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result



# Fibonacci Sequence up to a number
def fibo_upto_a_number(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

    

if __name__ == '__main__':
    # print(stringReverse("12435"))
    # print(palindrome_check("1221"))
    # print(odd_even())
   
    # print(fibonacci_series())
    # print(is_prime(99))
    # print(count_words("   the    fun game   "))
    print(reverse_array([1,1, -1, 0 , 4, -4]))
    # print(find_maximum([5,4,8,7]))
    # print(find_minimum([5,4,8,7]))
    # print(is_armstrong(143))
    # print(remove_duplicates([1,1,2,5,6,4,6,7,5]))
    # print(check_anagram("john", "sia"))
    # print(count_characters("lionel messi"))
    # print (is_perfect_number(6))
    # print (array_sum([1,2,3,4]))
    # print (find_average([1,6,78,3,2]))
    # print(factorial_finder(5))
    # print(fibo_upto_a_number(10))
    



