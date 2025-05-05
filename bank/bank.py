#In a file called bank.py,
# implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100.
# Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively

def main():
    greeting = input("Greeting:  ").strip().lower()

    if "hello" in greeting:
        print(f"$0")

    elif greeting.startswith("h"):
        print(f"$20")

    else:
        print(f"$100")



main()


# New method startswith()
# In Python, you can use the startswith() method to check if a string starts with a specific prefix.

#OR use Indexing
#elif "h" in greeting [0]
