def main():
    time = input("What is the time? ")
    newtime = convert(time)


    if 7 <= newtime <= 8:
        print("Breakfast Time")
    elif 12 <= newtime <= 13:
        print("Lunch Time")
    elif 18 <= newtime <= 19:
        print("Dinner Time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
