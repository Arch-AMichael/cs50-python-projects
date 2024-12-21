def main():
    greeting = input("Greeting ").strip().lower()

    if "hello" in greeting:
        print(f"$0")

    elif greeting.startwith("h"):
        print(f"$20")

    else:
        print(f"$100")



main()
