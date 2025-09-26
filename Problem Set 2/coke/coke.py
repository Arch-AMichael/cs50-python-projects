#Task:In a file called coke.py,
# implement a program that prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due.
# Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed.
# Assume that the user will only input integers,
# and ignore any integer that isn’t an accepted denomination.

#Receive the input
def main():
    amount_due = 50
    final = caculate(amount_due)
    change_owed = abs(final)  #Abs function
    print(f"Change Owed: {change_owed}")

def caculate(amt):
    while amt > 0:
        print(f"Amount Due: {amt}")
        int_input = int(input("Insert Coin: "))
        if int_input in [25, 10, 5]: #You can create a list directly in your if statment
            amt -= int_input # Update amt with the inserted coin
    return -amt # Return the change owed, which is the negative of the remaining amount

main()






#The abs() function returns the absolute value of the specified number.
