'''
print("Hello World")
print("Hello" + " Angela")
print("Hello\nWorld!")
'''

# print('Hello ' + input('What is your name?\n') + '!')

# name = input('What is your name?\n')
# print(name)

'''
name = 'Lucas'
print(name)
lenght = len(name) # with 'len()' you can find out the lenght of your word
print (lenght)

print(len(input('What is your name?\n')))
'''

'''
# challenge
username = input('What is your name?\n')
lenght = len(username)
print('The lenght of username word is: ' + str(lenght)) # you can turn into a string using 'str()'
print('The lenght of username word is:', lenght) # or using ',' -> don't need space after the text
print(f'The lenght of username word is: {lenght}') # or using "f-string"
'''

# challenge 2 (Write 3 lines of code to switch the contents of the variables)
glass1 = 'milk'
glass2 = 'juice'

aux = glass1 # 'aux' is a temporary variable to help you
glass1 = glass2
glass2 = aux

print(glass1 + '\n' + glass2)
