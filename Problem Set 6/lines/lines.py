"""
First Path:
If the user does not specify exactly one command-line argument
or if the specified file’s name does not end in .py
or if the specified file does not exist, the program should instead exit via sys.exit. = Using the os method to check
                        import sys
                        import os
                        if not os.path.exists(sys.argv[1])


Second Path:
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines.




Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.):
                not line.lstrip().startswith("#") | Only selects lines with no comments


Assume that any line that only contains whitespace is blank:
                Explanation : In Python, non-empty strings are considered “True”, and empty strings are “False.”
                if line.strip means → “If this line isn’t empty (even after removing spaces or tabs), then do something.”


Hints

    Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including lstrip and startswith.
    Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
    You might find it helpful to test your program on, e.g., some of Week 6’s source code as well as on programs of your own.

"""

# First Path
""" Import the Packages and checks if the input matches what we want. (1) We want the user to input something in the command line. (2) We want that input to be a python file (3) We want the python file to actually exist inside the computer """


import sys
import os


def main():

    # Get the file path from command line argument | If the user does not specify exactly one command-line argument = system exit
    if len(sys.argv) != 2:
        sys.exit("Error: Too few arguments | Usage: python lines.py <filename>")

    filepath = sys.argv[1]

    # or if the specified file’s name does not end in .py
    if not filepath.endswith(".py"):
        sys.exit("Python file not specfied.")

    # or if the specified file does not exist. Raise ValueError
    if not os.path.exists(filepath):
        raise ValueError("Error: File does not exist.")

    print(lines_count(filepath))


def lines_count(filepath):
    line_count = 0
    with open(filepath) as temp:
        for line in temp:
            line = line.strip()
            # (1) Assume that any line that only contains whitespace is blank. (2) Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.)
            if line and not line.startswith(("#")):
                line_count += 1
    return line_count


if __name__ == "__main__":
    main()
