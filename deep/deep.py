#Input
def main():
    Q_of_life = input("What is the great question of life ").strip().lower()
    Q_of_life = Q_of_life.replace("-","").replace(" ","")

    if Q_of_life == "42" or Q_of_life == "fortytwo":
        print("Yes")
    else:
        print ("No")

main()

# Smarter way to solve the problem is to replace all the expected inputs to one input you desire and using that.
# For example, instead of
#   if Q_of_life == "42" or Q_of_life == "fortytwo":
#        print("Yes")

#use
# Q_of_life = Q_of_life.replace("-","")

# that way any forty-two will become fortytwo. This is applicable to spaces as well
