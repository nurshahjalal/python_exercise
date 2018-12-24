
menu = []
tea_menu = []
egg_menu = []
menu.append(["potato", "Egg", "Onion", "Coffee"])
menu.append(["Bread", "Butter", "Jelly", "Coffee"])
menu.append(["Bread", "Hot Dog", "Tea", "Pepper"])
menu.append(["potato", "Egg", "Bread", "Tea"])
menu.append(["Egg", "Honey", "Onion", "Egg", "Toast"])
menu.append(["potato", "Chicken", "Egg", "lentil"])
menu.append(["potato", "Egg", "Fish", "Coffee"])

for item in menu:
    if "Coffee" not in item:
        # Creating tea menu lists
        tea_menu += item
print("Tea Menu {} : ".format(tea_menu))
if ("Egg" and "Bread") in tea_menu:
    print("this is I want in my Breakfast")
