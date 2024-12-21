#Input
def main():
    Q_of_life = input("What is the great question of life ").strip().lower()
    Q_of_life = Q_of_life.replace("-","").replace(" ","")

    if Q_of_life == "42" or Q_of_life == "forty two":
        print("Yes")
    else:
        print ("No")

main()
