
## Get the input
def main():
    time = input("What is the time? ")
# Turn to a list
    hours, minutes = time.split(":")
#Put the list into convert function
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


# Takes the list
def convert(hour, minute):
# Turn into 7.5 format
    caculation = hour + str(minute / 60)
    return (caculation)


if __name__ == "__main__":
    main()
