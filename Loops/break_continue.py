shoppingList = ["milk", "Egg", "Spam", "Bread", "rice"]

for item in shoppingList:
    if item=="Spam":
        continue
    print("Buy : "+ item)

print("=======================")
for item in shoppingList:
    if item == "Spam":
        break
    print("Buy : " + item)