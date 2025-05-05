'''
In a file called taqueria.py,

1.
implement a program that enables a user to place an order,
prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
2.
After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
Treat the user’s input case insensitively.
3.
Ignore any input that isn’t an item.
Assume that every item on the menu will be titlecased.


'''
def main():
    order = 0
    while True:
        try:
            item = menu(input('Item: ').lower().strip())
            order = calculate(order, item)
            print(f'Total order cost: ${order:.2f}')
        except EOFError:
            break
        except (KeyError, TypeError):
            pass






def calculate(num1, num2):
     return num1 + num2



def menu(order):
    menu = {
            "baja taco": 4.25,
            "burrito": 7.50,
            "bowl": 8.50,
            "nachos": 11.00,
            "quesadilla": 8.50,
            "super burrito": 8.50,
            "super quesadilla": 9.50,
            "taco": 3.00,
            "tortilla salad": 8.00
            }
    if order in menu:
        key = menu[order]
        return key
main()


'''
Lesson Notes:
1.
The :.2f is a format specification used in Python to control the appearance of floating-point numbers when they are converted to strings.
Specifically, :.2f ensures that the number is formatted with exactly two decimal places.

In the context of your code:
python = print(f'Total order cost: ${order_total:.2f}')

The :.2f means that order_total will be rounded to two decimal places
and displayed with two digits after the decimal point. For example:

    If order_total is 12.5, it will be displayed as 12.50.

    If order_total is 7.348, it will be rounded and displayed as 7.35.

This formatting makes the output cleaner and ensures consistency, especially when dealing with monetary values. 💰

2.
Have a variable where you store the number after the caculation
Make sure that it is out of the loop



'''
