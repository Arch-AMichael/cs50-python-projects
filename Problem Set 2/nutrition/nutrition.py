def main():
    item = dictonary(input("Item: ").strip().lower())
    if item:
        print(item)
    else:
         print("")



def dictonary(s):
    nutrition = {"apple":130, "avocado":50, "banana":110, "cantaloupe":50, "grapefruit":50, "grapes":90, "honeydew melon":50, "kiwifruit":90, "lemon":15, "Lime": 20, "nectarine":60, "orange":80, "peach":60, "pear":100, "pineapple":50, "plums":70,
             "strawberries":50, "sweet cherries":100, "tangerine":50, "watermelon":80}
    if s in nutrition.keys():
        return(f"Calories: {nutrition[s]}")
    else:
        return None

main()
