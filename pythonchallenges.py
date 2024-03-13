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
        if char != " ":  # Skip spaces
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

    

# if __name__ == '__main__':
    # print(stringReverse("12435"))
    # print(palindrome_check("1221"))
    # print(odd_even())
   
    # print(fibonacci_series())
    # print(is_prime(99))
    # print(count_words("   the    fun game   "))
    # print(reverse_array([1,1, -1, 0 , 4, -4]))
    # print (find_maximum([]))
    # print(find_minimum([5,4,8,7]))
    # print(is_armstrong(143))
    # print(remove_duplicates([]))
    # print(check_anagram("hello", "john"))
    # print(count_characters("lionel messi"))
    # print (is_perfect_number(0))
    # print (array_sum([]))
    # print (find_average([1,6,78,3,2]))
    # print(factorial_finder(-5))
    # print(fibo_upto_a_number(10))



# leetcode questions

# Two sum = Sum to Target
# "Given an array of integers called 'nums' and an integer 'target', find the index of two distinct numbers in the array that add up to the given target. Assume that there is exactly one solution for each input.
def sum_to_target(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
print(sum_to_target(nums, target))



# matrix transposition
def matrix_transposition(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


# List Sorting

def custom_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# Pascal's triangle

def generate_pascals_triangle(num_rows):
    triangle = [[1]]
    for i in range(1, num_rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

# Prime Factorization

def prime_factors(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return factors
    

# binary to decimal

def binary_to_decimal(binary_num):
    return int(binary_num, 2)

# decimal to binary

def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

# fibonacci with recursion

def fibonacci_recursive(limit):
    if limit == 0:
        return [0]
    elif limit == 1:
        return [0, 1]
    else:
        fib = fibonacci_recursive(limit - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

# Unique Paths in a grid
    
def unique_paths(m, n):
    dp = [[1] * n] * m
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

# Stack Sorting

def sort_stack(stack):
    temp_stack = []
    while stack:
        temp = stack.pop()
        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())
        temp_stack.append(temp)
    while temp_stack:
        stack.append(temp_stack.pop())
