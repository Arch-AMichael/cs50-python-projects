'''
In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).

Then output the user’s grocery list in all uppercase,
sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.

No need to pluralize the items. Treat the user’s input case-insensitively

'''
'''
1. Creating an empty dictonary
2. Immediately use an if statements
3. Add user inputs into dictonary with value of 1 if the user does not exist.
4. If the user does exist, then update the value by 1

Lesson: Key can be anything and be the same thing. Key is different from index. Use the key to keep count of how many values,
'''

def main():
   dict = {}
   while True:
        try:
            item = input('').upper()
            if item not in dict:
                dict[item] = 1
            else:
                dict[item] = dict[item] + 1
        except EOFError:
            for i in sorted(dict):
                print(dict[i], i)
            break




main()
