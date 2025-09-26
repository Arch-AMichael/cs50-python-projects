#Task: In a file called indoor.py,
# implement a program in Python that prompts the user for input
# and then outputs that same input in lowercase.
# Punctuation and whitespace should be outputted unchanged.
# You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

Name = (input("Hi and welcome to Mcdonald, what would you like to get today? ")).lower().strip()

print(f"Sure, 1 {Name} coming up")

