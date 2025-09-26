#Task:In a file called camel.py,
# implement a program that prompts the user for the name of a variable in camel case
# and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

name = input('CamelCase: ')

for letter in name: #Take one letter from the input or and run the below statment on it
    if letter.isupper(): #If this one letter is upper i want you to do this ↓
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")

print()
