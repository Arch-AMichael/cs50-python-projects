#Task: In a file called einstein.py,
# implement a program in Python that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer.
# Assume that the user will input an integer.


    #Get user input
Mass = int(input("m: "))
    #Convert Mass to Energy

Energy = (Mass) * 90000000000000000
    #Print Mass using J
print(f"E: {Energy}")


#You can add int either on when recieveing the input or when doing the caculation
#Input: int(input("m: ")))
#Caculation: int(Mass) * 90000000000000000
