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
