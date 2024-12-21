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
