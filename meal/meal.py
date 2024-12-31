def main():
    time = input("What is the time? ")
    hours, minutes = time.split(":")
    newtime = convert(hours), (float(minutes))
    checkhour = newtime[0]

    if checkhour == "7" or  hour == "8":
        return ("Breakfast Time")
    elif checkhour == "12" or  hour == "13":
        return ("Lunch Time")
    elif checkhour == "18" or  hour == "19":
        return ("Dinner Time")
    else:
        return (" ")



def convert(hour, minute):
    caculation = hour + minute / 60
        return (caculation)


if __name__ == "__main__":
    main()
