"""
Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv, below:

Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95

See regular.csv for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:

+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
--------------------------------------------------------------------------------------------------------------------------------------------------------------
In a file called pizza.py, implement a program that expects exactly one command-line argument.
                                                                                import sys

                                                                                def main()
                                                                                filepath = sys.argv[1]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

                                        if len(sys.argv) != 2:
                                sys.exit("Error: Too few arguments | Usage: python lines.csv <filename>")

                            if not filepath.endswith(".csv):
                                sys.exit("Python file not specfied.")

                            if not os.path.exists(filepath):
                                raise FileNotFound("Error: File does not exist.")

----------------------------------------------------------------------------------------------------------------------------------------------------------------
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format.

Example of using Tabulate from geeksforgeeks:
                                                                from tabulate import tabulate

                                                                # Data for the table
                                                                data = [
                                                                    {"Item":"Pizza", "Price": "850"},
                                                                    {"Item":"Burger","Price":  "500"},
                                                                    {"Item":"Salad", "Price": "475"},
                                                                    {"Item":"Pasta", "Price": "725"}
                                                                ]

                                                                print(tabulate(data, headers="keys"))


STEP 1 Convert the CSV to a list of dictonaries
STEP 2 Tabulate the List of Dictonaries

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Hints

    Recall that the csv module comes with quite a few methods, per docs.python.org/3/library/csv.html, among which are reader, per docs.python.org/3/library/csv.html#csv.reader, and DictReader, per docs.python.org/3/library/csv.html#csv.DictReader.
    Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
    Note that the tabulate package comes with just one function, per pypi.org/project/tabulate. You can install the package with:

    pip install tabulate



"""

import sys
import csv
import os
from tabulate import tabulate


def main():

    # Get the file path from command line argument | If the user does not specify exactly one command-line argument = system exit
    if len(sys.argv) != 2:
        sys.exit("Error: Too few arguments | Usage: python lines.csv <filename>")

    filepath = sys.argv[1]

    # or if the specified file’s name does not end in .csv
    if not filepath.endswith(".csv"):
        sys.exit("csv file not specfied.")

    # or if the specified file does not exist. Raise FileNotFound
    if not os.path.exists(filepath):
        raise FileNotFound("Error: File does not exist.")

    # and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format.
    converted = csv_convert(filepath)
    print(tabulate(converted, headers="keys", tablefmt="grid"))


def csv_convert(filepath):
    # The name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate
    pizza = []
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            pizza.append(row)
    return pizza


if __name__ == "__main__":
    main()
