#In a file called interpreter.py,
# implement a program that prompts the user for an arithmetic expression
# and then calculates
# and outputs the result as a floating-point value formatted to one decimal place.
#
# Assume that the user’s input will be formatted as x y z,
# with one space between x and y and one space between y and z, wherein:
# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1,
# your program should output 2.0. Assume that, if y is /, then z will not be 0.


#Main code accepts user input and prints result
def main():
    expression = (input("Expression: "))
    x, y, z = expression.split(" ")
    calculate = calculation(float(x), y ,float(z))
    decimal = round(float(calculate), 1)
    print(decimal)


def calculation(x,y,z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    else:
        return x / z



main()

# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.


# round(float) good function
