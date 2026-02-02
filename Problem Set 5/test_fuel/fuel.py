"""

In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input,
 wherein each of X and Y is a positive integer,
 and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
If Y is 0, then convert should raise a ZeroDivisionError.

gauge expects an int and returns a str that is:
        "E" if that int is less than or equal to 1,
        "F" if that int is greater than or equal to 99,
        and "Z%" otherwise, wherein Z is that same int.

"""


def main():

    print(gauge(convert(input("Help: "))))


def convert(fraction):
    try:
        x, y = fraction.split(
            "/"
        )  # prompts the user for a fraction | Uses the split Function to create a list
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("This is not in X/Y format with integers")

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError("X should be less than Y")
    return round((x * 100) / y)


def gauge(answer):
    if (
        answer >= 99
    ):  # if 99% or more remains, output F instead to indicate that the tank is essentially full
        return "F"
    elif (
        answer <= 1
    ):  # 1% or less remains, output E instead to indicate that the tank is essentially empty
        return "E"
    else:
        return f"{answer}%"  # outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank


if __name__ == "__main__":
    main()


"""
Lesson from this code:
    If you desire one particular input or value
    Instead of writing statment to check for each unwanted outcome
    Use the != on the specfic value or input you want
    Anything else that is not that, re-prompt

"""
