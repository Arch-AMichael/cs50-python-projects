import random
import sys


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x, y = generate_integer(level)
        actual_answer = x + y
        error = 0
        while True:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if error == 2:
                    print(f"Correct Answer Dumbass: {x} + {y} = {actual_answer}")
                    break
                if user_answer == actual_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    error += 1
                    continue

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            except EOFError:
                sys.exit()

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Please enter 1, 2, or 3: "))
            if level in range(1, 4):
                return level

        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError

    return x, y


if __name__ == "__main__":
    main()
