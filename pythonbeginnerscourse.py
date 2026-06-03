#Full Python Course for Beginners
print("4")

course = "Python \nProgramming"
print(course)

first = "Mosh"
last = "Hamedani"
full = f"{len(first)} {2+2}"
print(full)

course = "  python programming"
print(course.upper())
print(course)
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("p","j"))
print("pro" in course)

#Numbers
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3) #use double slash to get integer
print(10%3)
print(10**3)

#Inputs
x = input("x:")
print(type(x))
y = int(x)+1
y = x + 1
print(f"x:{x},y:{y}")

print(bool("False"))

#Comparison Operators
"bag" > "apple"
"bag" == 'BAG'
ord("b")
ord("B")

#Conditional Statements
temp = 35
if temp > 30:
    print("it's warm")
    print("Drink water")
elif temp > 20:
    print ("It's nice")
else:
    print ("It's cold")
print("done")

#Ternary operator
age = 22
message = 'Eligible' if age >= 18 else "Not Eligible"
print (message)

#Logical Operators
high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print("eligible")
else:
    print("Not Eligible")

age = 22
if 18 <= age < 65:
    print("Eligible")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else: 
    print("c")
#Letter c will be printed

#Loops
for number in range(1,10,2):
    print("Attempt", number, (number)*".")

successful = True
for number in range(3):
    print("attempt")
    if successful:
        print ("Successful")
        break
else:
    print("Failed Attempts")

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

print(type(5))
print(type(range(5)))

for x in "Python":
    print(x)

number = 100
while number > 0:
    print(number)
    number //=2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

count = 0
for number in range(1,10):
    if number % 2 == 0:
        print(number)
        count += 1 
print(f"We have {count} even numbers")

def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("Welcome aboard")

greet("Mosh", "Ham")
greet("John", "Smith")

round(1.9)

def get_greeting(name):
    return f"Hi {name}"
message = get_greeting("Mosh")

def increment(number, by):
    return number + by

print (increment(2))

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

multiply(2,3,4,5)