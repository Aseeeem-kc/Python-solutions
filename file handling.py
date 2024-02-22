# part-3 ques-1

# with open("datafile.txt", "r") as f:
#     for line in f:
#         words = line.split()
#         reduced_line = ' '.join(words)
#         print(reduced_line)


# ques-2

# def extract_temp():
#   with open("datafile.txt") as file:
#     for line in file:
#       words = line.split()
#       for i in words:
#         if (i.isdigit()):
#           print(i)

# extract_temp()


# ques-3

# def check_quotes():
#     quote1 = "'"
#     quote2 = '"'
#     single_quotes = 0
#     double_quotes = 0

#     with open("datafile.txt", "r") as f:
#         for i in f:
#             for j in i:
#                 if j == quote1:
#                     single_quotes += 1
#                 elif j == quote2:
#                     double_quotes += 1

#     return single_quotes % 2 == 0 and double_quotes % 2 == 0

# print(check_quotes())

# ques-5


# import random as r


# def interleave_chars():
#   with open("datafile.txt","r") as file:
#     for i in file:
#       splited = i.split()
#       joined =''.join(splited)
#       result = ""
#       for i in range(0,len(joined)):
        
#         ran_num = r.randint(0,len(joined)-1)
#         result += joined[ran_num]
#       print(result)


# interleave_chars()


# ques-6


# def counter():
#   line = "hello This is a string\n second line of the string!!"
#   splited_line = line.split()
#   string_count = 0
#   for i in splited_line:
#     string_count += len(i)
#   print(string_count)
    
# counter()


# ques-7

# def first_three():
#   month = "December"
#   print(month[:3])

# first_three()



# ques-8

# def check_r():
#   month ="Decemben"
#   return 'r' in month
# print(check_r())

# ques-9

# def count():
#   month="decemberrer"
#   print(month.count('r'))
# count()


# ques-10

# def name_lname():
#   first_name = "ashim"
#   last_name = "kc"
#   result = first_name + ", "+last_name
#   print(result)
# name_lname()


# ques-11


# def check_nondigit():
#   ss_num = '123231'
#   if (ss_num.isdigit()):
#     print("Only digit")
#   else:
#     print("Contains non-digit")
# check_nondigit()



# ques-12

# def check_location():
#   email_addr = "ashimkc7297@gmail.com"
#   print(email_addr.index('@'))
# check_location()


# ques-13

# def replace_slash():
#   date = "12/14/2012"
#   changed_date = date.split('/')
#   result = '-'.join(changed_date)
#   print(result)
# replace_slash()
    

# ques-14

# def remove_():
#   err_mesg = "** error message **"
#   result = err_mesg.strip('*, ')
#   print(result)
# remove_()


# ques-4

# def letter_counter():
#     with open('datafile.txt','r') as file:
#         words=file.read()
#         checked_words=[]
#         words_count=[]
#         for i in words:
#             word_count=0
#             if not i.lower() in checked_words and i!=' ':
#                 for j in words:
#                     if j.lower()==i.lower():
#                         word_count+=1
#                 words_count.append((i.lower(),word_count))
#                 checked_words.append(i.lower())
#             else:
#                 continue
#         print(words_count)

# letter_counter()

# part-4 question

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_val + shift) % 26 + ascii_val)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def process_file(file_name, operation):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            
        shift = int(input("Enter the shift value for encryption/decryption: "))
        
        if operation == 'e':
            result = encrypt(content, shift)
            output_file_name = f"encrypted_{file_name}"
            print(f"Encryption successful. Result written to {output_file_name}")
        elif operation == 'd':
            result = decrypt(content, shift)
            output_file_name = f"decrypted_{file_name}"
            print(f"Decryption successful. Result written to {output_file_name}")
        else:
            print("Invalid operation. Please enter 'e' for encryption or 'd' for decryption.")
            return

        with open(output_file_name, 'w') as output_file:
            output_file.write(result)

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

print("This program will encrypt and decrypt text files")

operation = input("Enter (e) to encrypt a password, and (d) to decrypt: ").lower()

if operation in ['e', 'd']:
    file_name = input("Enter the name of a text file to encrypt/decrypt: ")
    process_file(file_name, operation)
else:
    print("Invalid operation. Please enter 'e' for encryption or 'd' for decryption.")







