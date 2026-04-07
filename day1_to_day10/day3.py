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

try:
    number = int(input("Type a number: "))

except ValueError:
    print("That's not a number. Try again!")
    exit()
    
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    