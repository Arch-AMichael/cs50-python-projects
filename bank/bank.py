def main():
    greeting = input("Greeting ").strip().lower()

    if greeting == "hello":
        print(f"$0")

    elif "h" in greeting:
        print(f"$20")

    else:
        print(f"$100")



main()
