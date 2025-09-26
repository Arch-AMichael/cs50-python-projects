import inflect
p = inflect.engine()


Names_List = []

while True:
    try:
        Name = input('Name: ')
        Names_List.append(Name)
    except EOFError:
        Names_String = p.join(Names_List)
        print(f"Adieu, adieu, to {Names_String}")
        break




