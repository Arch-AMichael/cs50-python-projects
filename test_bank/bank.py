#In a file called bank.py,
# implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100.
# Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively

def main():
    print(value(input("Greeting:  ").strip().lower()))



def value(greeting):

    if "hello" in greeting:
        return(f"$0")

    elif greeting.startswith("h"):
        return(f"$20")

    else:
        return(f"$100")


if __name__ == "__main__":
    main()


# New method startswith()
# In Python, you can use the startswith() method to check if a string starts with a specific prefix.

#OR use Indexing
#elif "h" in greeting [0]
