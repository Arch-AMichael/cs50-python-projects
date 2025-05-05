#Task: . In a file called twttr.py,
# implement a program that prompts the user for a str of text
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

def main():
    string = shorten(input('Input: '))
    print (f'Output: {string}')




def shorten(string):
    result = ""
    for word in string:
        if isalpha(word) and word not in ['A','E','I','O','U','a','e','i','o','u']:
            result += word
    return result


main()


