def main():
    time = input("What is the time?")
    hours, minutes = time.split(":")
    newtime = convert(float(hours), float(minutes))


def convert(hours, minutes):
    caculation = minutes / 60
    if hours = "7" or "8":
        return ("Breakfast Time")
    if hours = "12" or "13":
        return ("Lunch Time")
    if hours = "7" or "19":
        return ("Breakfast Time")



if __name__ == "__main__":
    main()
