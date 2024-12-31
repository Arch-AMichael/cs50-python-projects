def main():
    time = input("What is the time? ")
    newtime = convert(time)


    if newtime <= 7 or newtime <= 8:
        print("Breakfast Time")
    elif newtime <= 12 or newtime <= 13:
        print("Lunch Time")
    elif newtime <= 18 or newtime <= 19:
        print("Dinner Time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
