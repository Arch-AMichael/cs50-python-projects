import random
import sys


def main():
    while True:
        try:
            query = int(input("Level: "))
            if (
                query > 1
            ):  # If the user does not input a positive integer, the program should prompt again.
                number = random.randint(
                    1, query
                )  # Randomly generates an integer between 1 and query,
                guess(number)
                break
        except ValueError:  # Catches string input, and reprompts
            pass


def guess(number):
    while True:
        try:
            user_guess = int(input("Guess: "))  # Prompts the user to guess that integer
            if (
                user_guess < 1
            ):  # If the guess is not a positive integer, the program should prompt the user again.
                continue  # Restart Loop
            if user_guess > number:
                print("Too large!")  # Prints result and still continues in the loop
            elif user_guess < number:
                print("Too small!")  # Prints result and still continues in the loop
            else:
                sys.exit("Just right!")  # Exits system and prints 'Just right!'
        except ValueError:  # Catches string input, and reprompts
            pass


main()

"""
Notes:
1. Ques: why does the program skip the if statements after the continue?
        When you use continue inside a loop, it immediately skips the rest of the code in the current iteration
        and goes back to the beginning of the loop for the next iteration.
        This is why the if statements after continue are being skipped

2. Alternative:
        def guess(number):
            while True:
                try:
                    user_guess = int(input("Guess: "))
                    if user_guess < 1:
                        print("Please enter a positive integer.")
                    elif user_guess > number:
                        print("Too large!")
                    elif user_guess < number:
                        print("Too small!")
                    else:
                        return "Just right!"
                except ValueError:
                    print("Invalid input. Please enter a number.")
Why This Fix Works?
    No need for continue: The loop will restart anyway after completing all conditions.
    Prevents unnecessary skips: Each condition is checked only if needed, ensuring smooth logic.

3. Two ways of checking conditionals in a while Loop:
        The main function simply checks for the desired condition,
        everything other than that is ignored

        The guess function first checks if there is an input other,
        than the desired condition, if there is it specfically tells the program,
        to continue in the loop. The real condition will be under.
"""
