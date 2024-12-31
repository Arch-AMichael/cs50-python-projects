def main():
    time = input("What is the time? ")
    hours, minutes = time.split(":")
    newtime = convert(hours, (float(minutes)))
    checkhour = newtime[0]

    if checkhour == "7" or  checkhour == "8":
        print ("Breakfast Time")
    elif checkhour == "12" or checkhour == "13":
        print ("Lunch Time")
    elif checkhour == "18" or checkhour == "19":
        print ("Dinner Time")
    else:
        return (" ")



def convert(hour, minute):
    caculation = hour + str(minute / 60)
    return (caculation)


if __name__ == "__main__":
    main()
