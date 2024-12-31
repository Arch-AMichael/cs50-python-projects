def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    #First convert the $ to " " using replace() method and store it in a variable called  number
    number = d.replace("$", " ")
    #Convert the input string to float and store it in a variable called float_number
    float_number = float(number)
    #(Optional)Round the digit to it's nearest integer ex. 25.6274 => 25.6 or 25.63. Store you round number in a variable x
    x = round(float_number, 1)
    #return float number, rounded and without dollar sign to main fucntion
    return x


def percent_to_float(p):
    # TODO
    #First convert the % to " " using replace() method and store it in a variable called  number
    number = p.replace("%", " ")
    #Convert the input string to float and store it in a variable called float_number
    float_number = float(number)
    #Divide digit by 100 to get the percentage
    y = float(float_number / 100)
    #Return percentage
    return y

main()





def main():
    time = input("What is the time?")
    hours, minutes = time.split(":")
    newtime = convert(hours), (float(minutes))


def convert(hours, minutes):
    caculation = minutes / 60

   if hour == "7" or  hour == "8":
        return ("Breakfast Time")
    elif hour == "12" or  hour == "13":
        return ("Lunch Time")
    elif hour == "18" or  hour == "19":
        return ("Dinner Time")
    else:
        return (" ")
)



if __name__ == "__main__":
    main()
