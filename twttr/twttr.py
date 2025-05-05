#Task: . In a file called twttr.py,
# implement a program that prompts the user for a str of text
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.
import string

def main():
    string = shorten(input('Input: '))
    print (f'Output: {string}')




def shorten(sentance):
    result = ""
    for word in sentance:
        if isalpha(word) and word not in string.punctuation and word not in ['A','E','I','O','U','a','e','i','o','u']:
            result += word
    return result


main()


