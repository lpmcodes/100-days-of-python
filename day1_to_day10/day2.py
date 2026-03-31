# Use 'type' to find out what data type you are using
'''
print(type('123'))
print(type(123))
print(type(123.5))
print(type(True))
'''
# challenge (make this line of code run without errors)
'''
print('Number of letters in your name:', len(input('Enter yout name: ')))
'''
# math operations
'''
print(5 / 3)
print(5 // 3) # you can get an integer result by using '//'

print(5 ** 2) # by using '**', you can raise a number to a power
'''

# priority order
# PEMDAS - PARANTHESES, EXPONENTS, MULTIPLICATION/DIVISION, ADDITION/SUBTRACTION
# ()
# **
# * OR (/ -> //)
# + OR -
'''
print((int(3 * (3 + 3) / 3 - 3)))
'''
bmi = 84 / (1.65 ** 2)
print(bmi)

print(int(bmi))

print(round(bmi)) # 'round' -> round to the nearest whole number

gli = 30.29
print(round(gli))

mto = 35.8912839
print(round(mto, 2)) # will retain the value to two decimal places