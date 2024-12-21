#Input
Q_of_life1 = input("What is the greaat question of life ").lower()
Q_of_life = Q_of_life1.replace(" f", "f")

if Q_of_life == "42":
    print("Yes")
elif Q_of_life == "forty-two":
    print("Yes")
elif Q_of_life == "forty two":
    print("Yes")
else:
    print ("No")
