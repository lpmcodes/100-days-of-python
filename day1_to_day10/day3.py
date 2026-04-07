# ----------------- // -----------------
# conditional statements
# logical operators
# code blocks
# scope
# ----------------- // -----------------

'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can buy a ticket!")
else:
    print("You can't buy a ticket!")
'''
# shows the rest of a division
'''
print(10 % 3)
'''

# check if a number is even or odd
'''
try:
    number = int(input("Type a number: "))

except ValueError:
    print("That's not a number. Try again!")
    exit()
    
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
'''
# ----------------- // -----------------
# if inside of another if
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can buy a ticket!")
    age = int(input("What is your age? "))
    if age >= 18:
        print("You have to pay 10 $.")
    elif age > 12 and age < 18:
        print("You have to pay 7 $.")
    else:
        print("You have to pay 5 $.")
else:
    print("You can't buy a ticket!")
'''
weight = 85
height = 1.85

bmi = weight / (height ** 2)

print(f"bmi = {bmi}.\n")

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
elif bmi >= 25:
    print("overweight")
