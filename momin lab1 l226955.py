

"""
#1 Write a program that asks the user for their name and age, then prints a greeting message

name = input("Enter your Full name : ")
age = input("Enter your Age : ")

print("Your cool Name : "+name+" and your Age : "+age+ " WOW! your are getting old" )



#2 Create a program that takes user input and determines its data type, handling
#conversions to int or float when possible.

userinput=input("Enter a Number : ")

if userinput.isdigit():
    print("It is an integer.")
elif float(userinput):
    print("It is a float.")
else:
    print("It is a string.")
    

#3 Initialize a list with specific elements, modify it by adding and removing items, and print
#each element in uppercase.

items = ["lmao", "lol", "xd"]
items.append("haseingey log") 
items.append("momin") 
items.remove("lol")  

for item in items:
    print(item.upper())
    
#Unpack the first two elements of a given tuple into separate variables and print them
tuple = ("momin", 20.1, 30.2345, 40.32)
m1, m2, *remaining = tuple
print("First: ", m1)
print("Second: ", m2)


#Create a program to store five student names and their grades in a dictionary and then
#print the dictionary.
students={}
for i in range(5):
    name1=input("Enter the student name : ")
    grade=input("enter the "+name1+" Grade : ")
    students[name1]=grade

print("Student Grades:", students)


#Take two lists of integers from the user, convert them to sets, and display their union,
#intersection, and difference.

list1 = []
list2 = []

n1 = int(input("Enter the number of elements for the first list: "))
for i in range(n1):
    list1.append(int(input(f"Enter number {i+1} for first list: ")))

n2 = int(input("Enter the number of elements for the second list: "))
for i in range(n2):
    list2.append(int(input(f"Enter number {i+1} for second list: ")))

set1 = set(list1)
set2 = set(list2)

print(f"Union: {list(set1.union(set2))}")
print(f"Intersection: {list(set1.intersection(set2))}")
print(f"Difference (list1 - list2): {list(set1.difference(set2))}")
print(f"Difference (list2 - list1): {list(set2.difference(set1))}")


#Ask the user to enter an integer and determine if it is positive, negative, or zero, and
#whether it is even or odd.

num = int(input("Enter an integer: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


#Print numbers from 1 to 50, replacing multiples of three with "Fizz", multiples of five with
#"Buzz", and multiples of both with "FizzBuzz".

for i in range(1,51):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)



#Define a function to calculate the factorial of a non-negative integer using a loop.

def fac(f1):
    if f1 < 0:
        return "neg number = Error"
    
    fact = 1
    for i in range(1, f1 + 1):
        fact *= i
    
    return fact

num = int(input("Enter a non-negative integer: "))
print(f"The factorial of {num} is {fac(num)}")




# Create a function to check if a number is prime and use it to verify a user-entered number.

def checkprime(n):
    if n <= 1:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: "))
if checkprime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    


#Write a function that takes a list of integers and returns a new list with the squares of
#each number using list comprehension.

def square(no):
    sq = []
    for num in no:
        sq.append(num * num) 
    return sq

input = [1, 2, 3, 4, 5]
squared = square(input)
print(squared)



#Merge two dictionaries into one, with the second dictionary's values overwriting the first's
#in case of duplicate keys.

def merge(d1, d2):
    d1.update(d2)  
    return d1

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "d": 5}

dict = merge(d1, d2)
print(f"merged dictionary : {dict}")




#Write a function that removes duplicates from a list of integers while preserving the
#original order.

def removedup(no):
    s = set()  
    r = []  
    
    for num in no:
        if num not in s:
            r.append(num)
            s.add(num)
    
    return r

input2 = [1, 2, 3, 6, 8, 9, 10, 1, 45, 23, 3, 2, 4, 1, 5]
output2 = removedup(input2)
print(output2)



#Create a function to check whether a given string is a palindrome, ignoring case and spaces.

s = input("Enter a string to check if it's a palindrome: ")
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#Write a function that generates the first n numbers in the Fibonacci sequence based on 
#user input.


def fib(n):
    if n <= 0:
        return [] 
    elif n == 1:
        return [0]  
    
    seq = [0, 1]  
    
    for i in range(2, n):  
        next = seq[i - 1] + seq[i - 2] 
        seq.append(next) 
    return seq

n = int(input("Enter number to generate fibo of that num: "))
fibonacci_numbers = fib(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_numbers}")



#Develop a program that takes a series of numbers from the user, validates the input, and calculates the average.

def avg(nums):
    return sum(nums) / len(nums)

def valid(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

n = valid("Enter the number of elements for the list: ")
lst = []

for i in range(n):
    el = valid(f"Enter element {i + 1}: ")
    lst.append(el)

print(f"The average is: {avg(lst)}")



# Generate and print a multiplication table from 1 to 10 using nested loops.
for i in range(1, 11): #rows
    for j in range(1, 11): #cols
        print(i * j, end="      ")
    print()  
    


#Implement a simple registration and login system using a dictionary to store user
#credentials.

def register(users_db):
    print("Register a new user:")
    username = input("Enter username: ")
    if username in users_db:
        print("Username already exists. Please choose another one.")
        return
    password = input("Enter password: ")
    users_db[username] = password
    print("Registration successful!")

def login(users_db):
    print("Login:")
    username = input("Enter username: ")
    if username not in users_db:
        print("Username not found. Please register first.")
        return
    password = input("Enter password: ")
    if users_db[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password. Try again.")

def main():
    users_db = {}
    
    while True:
        print("\nWelcome to the system!")
        choice = input("Do you want to \n(1) Register \n(2) Login \n(3) Exit: ")

        if choice == '1':
            register(users_db)
        elif choice == '2':
            login(users_db)
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice")


main()


"""

#Take a list of words from the user and count the frequency of each word using a dictionary.

words = input("Enter a list of words separated by spaces: ").split()
word_count = {} 

for word in words:
    if word in word_count:
        word_count[word] += 1 
    else:
        word_count[word] = 1  

print("\nWord frequencies:")
print(word_count)




