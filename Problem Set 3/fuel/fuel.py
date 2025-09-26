'''In a file called fuel.py, implement a program that
# 1. prompts the user for a fraction,
#   formatted as X/Y, wherein each of X and Y is an integer,
#   and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.


2.  If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
    And if 99% or more remains, output F instead to indicate that the tank is essentially full.

3. If, though, X or Y is not an integer,
    X is greater than Y, or Y is 0, instead prompt the user again.
   (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''
def main():

    answer = get_number()



    if answer >= 99: # if 99% or more remains, output F instead to indicate that the tank is essentially full
        print('F')
    elif answer <= 1: # 1% or less remains, output E instead to indicate that the tank is essentially empty
        print('E')
    else:
        print(f'{answer}%') # outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank



def get_number():
    while True:
        try:
            x, y = input('Fraction: ').split('/') # prompts the user for a fraction | Uses the split Function to create a list
            x = int(x)
            y = int(y)

            if x <= y and y != 0: # X is greater than Y, or Y is 0, instead prompt the user again
                calculate = round((x * 100) / y)
                return calculate
            else:
                continue


        except (ValueError,ZeroDivisionError): # Be sure to catch any exceptions like ValueError or ZeroDivisionError.
            pass




main()










'''
Lesson from this code:
    If you desire one particular input or value
    Instead of writing statment to check for each unwanted outcome
    Use the != on the specfic value or input you want
    Anything else that is not that, re-prompt

'''














