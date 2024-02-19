# 1

my_list = [1,5,4,6,0,5]
my_list.append(9)
print(my_list)

# 2

nested_list = [
    ["first list","second value"],
    ["second list","second value"
    ],]
print(nested_list[1][0])

# 3

my_tuple = ("hi",3,True,"John")
print(len(my_tuple))


# 4

my_integers = [1,5,3,7,8,3,2]
my_integers.insert(2,569)
print(my_integers)


# 5

student_names = {"ashim":18,"sagar":21,"nabin":21}
print(student_names["ashim"])


# 6

user_input = input('Enter the integer: ')
my_list = []
while (user_input != ""):
    if int(user_input)<=100:
        my_list.append(user_input)
    else:
        my_list.append('over')
    user_input = input('Enter the integer: ')
print(my_list)

# 7

dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50, 6:60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)


# extra

odd = {1:"one",3:"three",5:"five",7:"seven",9:"nine"}
print(odd.keys())
print(odd.values())
print(odd.items())
print(len(odd))
if 7 in odd:
    print('7 is in the dictionary')
print(odd[9])
del odd[9]
print(odd)


# 8

students=[
{"student_id": 1, "name": "Jean Castro", "class": "V"},
{'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
{'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
{'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
{'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]
print(students)
user_input_key = input('Enter the key you want to check: ')
user_input_name = input('Enter the name you want to check: ')

for student in students:
    the_keys = student.keys()
    the_names = student.values()
    if user_input_key in the_keys and user_input_name in the_names:
        print(f"key:{user_input_key} and value:{user_input_name} does exist")
        break
    else:
        print(f"key:{user_input_key} and value:{user_input_name} does not exist")
        break


# 9

a_string = input('Enter any string: ')
a_list = []
while (a_string!= ""):
    if 'a' in a_string:
        a_list.append(a_string)
    a_string = input('Enter another string: ')
print(a_list)

# 10

list1 = input("Enter first list: ")
list2 = input("Enter second list: ")
new_list = []
for i in list2:
    if i in list1:
        new_list.append(i)
print(new_list)  

# 11

people_detail = {"ashim":22,"ankit":18,"nabin":32,"chitiz":16}
people_over_18 = {x for x in people_detail if people_detail[x]>18}
print(people_over_18)

# 12

friends = {"nabin":9871673319,"sharukh khan":9871673318,"messi":9871673312,"ronaldo":9871673315,"ankit":9871673345}
print(friends)
friends["musk"]=9869122100
print(friends)
del friends["nabin"]
print(friends)
friends["ankit"]=1234567890
user_input=input("Searching for? : ")
if user_input in friends:
    print(f"{user_input}'s number available")
else:
    print(f"{user_input}'s number is not available!")
sorted_list = [sorted(friends.items())]

print(sorted_list)

# 13
# program used lamba function (a syntax to call anonymous function) used to sort items by value and correspinding key

shop_items = {'item3': 45.50, 'item2':35, 'item1': 41.30, 'item5':55, 'item4': 24}


sorted_items = sorted(shop_items.items(), key=lambda x: x[1])
print(sorted_items)
sorted_items_reversed=sorted_items[::-1]
top_three_items = sorted_items_reversed[:3]
for key, value in top_three_items:
    print(f"{key}:{value}")


# 14

students = [
    {"name": "Alice", "age": 17, "gender": "female", "grades": [90, 85, 95]},
    {"name": "Bob", "age": 16, "gender": "male", "grades": [80, 75, 70]},
    {"name": "Charlie", "age": 16, "gender": "male", "grades": [100, 90, 95]},
    {"name": "Diana", "age": 17, "gender": "female", "grades": [85, 80, 90]},
    {"name": "Emily", "age": 16, "gender": "female", "grades": [95, 90, 100]}
]
# using loop to iterate through list of students
for student in students:
    name = student["name"]
    grades = student["grades"]
    #using sum and len function for computation
    average_grade = sum(grades) / len(grades)
    #displaying the name:average grade
    print(f"{name}: {average_grade}")


# 15

books = [
    ("Book1", "nemahang rai"),
    ("Book2", "ashim kc"),
    ("Book3", "subash chandra nemang")
]
sorted_books = sorted(books, key = lambda x:x[1])
print(sorted_books)

# 16

color_list_1 = ["red", "orange", "green", "blue", "white"]
color_list_2 = ["black", "yellow", "green", "blue"]
color1_minus_color2 = [set(color_list_1) - set(color_list_2)]
print(color1_minus_color2)
color2_minus_color1 = [set(color_list_2) - set(color_list_1)]
print(color2_minus_color1)

# 17  matrix game

def print_matrix(main_matrix):
    for i in main_matrix:
            print(i)

            
main_matrix = [[1,1,1],[1,1,1],[1,1,1]]
user_input = input("Select a element in a 3 X 3 matrix using index (index index): ")
move_count = 0

while (user_input != ""):
    move_count += 1
    first_user_index = int(user_input[0])
    second_user_index = int(user_input[2])
    if (main_matrix[first_user_index][second_user_index]!='X'):
         main_matrix[first_user_index][second_user_index]='X'
         print_matrix(main_matrix)
         if (main_matrix == [['X','X','X'],['X','X','X'],['X','X','X']]):
             print(f"The game is over! The number of moves you made was {move_count}")
             break
         user_input = input("Select a element in a 3 X 3 matrix using index: ")
    else:
        print("The cell has already been selected: ")
        user_input = input("Select a element in a 3 X 3 matrix using index: ")

# 18  library system

book_list = [
{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
{"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
{"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
{"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]

def display_books():

# Function to print all the books one by one 
    i = 1
    for book in book_list:
        print(f"{i}) {book}")
        i+=1
display_books()

def add_book(user_newbook):
    #function to add a book into the book list 
    book_list.append(user_newbook)
    print(f"{user_newbook} added!")
def remove_book(user_removebook):
    # function to rmeove a book from the book list
    del book_list[int(user_removebook)-1]
    print("The book was removed!")

def search_bytitle(user_titlesearch):
    for book in book_list:
        if user_titlesearch in book["title"]:
            print(f"The book {user_titlesearch} is available")

def search_byauthor (user_authorsearch):
    for book in book_list:
        if user_authorsearch in book["author"]:
            print(f"The book by {book['author']} is available.")



# asking user for input the bery first time
user_input = input("Enter a number for any option:\n 1.Add a new book\n2.Remove a book\n3.Search for a book by title\n4.Search for a book by author (optional)\n5.List all the books\n6.Quit")

# using while loop to run the program everytime except when the input is 'q'
while user_input !="q":
    
    #checking the user_input using if and else if
    if user_input == '1':
        user_newbook = input("Enter any book you want to add (list): ")
        add_book(user_newbook)
    elif user_input == '2':
        user_removebook = input("Enter the number of the book in list, you want to remove: ")
        remove_book(user_removebook)
    elif user_input == '3':
        user_titlesearch = input("Type the title of the book you want to search: ")
        search_bytitle(user_titlesearch);

    elif user_input == '4':
        user_authorsearch = input("Name the author to search their book: ")
        search_byauthor(user_authorsearch)

    elif user_input == '5':
        display_books()

    user_input = input("Enter a number for any option: ")
print("The library program is over!")





my_dict = {'name':'ashim','class':12,'roll':7}

for key, value in my_dict.items():
    print(key,value)

my_dict2 = {'val1':1,'val2':25,'val3':3}

sum_ = 0
for value in my_dict2.values():
    sum_ = sum_ + value
print(sum_)



