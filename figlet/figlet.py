from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

check = ['-f', '--font']
try:
    if len(sys.argv) < 2:
        random.choice(figlet.getFonts())
        query = input('Input: ')
        print(figlet.renderText(query))


    elif len(sys.argv) < 4 and sys.argv[1] in check and sys.argv[2] in figlet.getFonts() : #This include (0)python (1)name_of_script (2)input(-f or --font) (3)input(font)
        figlet.setFont(font=sys.argv[2])
        query = input('Input: ')
        print(figlet.renderText(query))

    else:
         sys.exit("Invalid usage")

except IndexError:
        sys.exit("Invalid usage")





''' The len of sys.argv and the use in print is different, the print start from the name_of_script as 0
 But the len(sys.argv) takes in the python as start 0

Good Help : https://www.reddit.com/r/cs50/comments/xnvrol/libraries/

 '''




