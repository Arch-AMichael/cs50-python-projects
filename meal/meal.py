def main():
    time = input("What is the time?")
    time_parts = time.split(":")
    result = convert(time_parts[0])
    print (f"{result}")


def convert(hour):
    if hour = "7" or "8":
        return ("Breakfast Time")
    if hour = "12" or "13":
        return ("Lunch Time")
    if hour = "7" or "19":
        return ("Breakfast Time")



if __name__ == "__main__":
    main()
