
# This  is regular way , not efficient as  newColor will replace previous newColor
colorList = ["Red", "pink", "White", "Brown", "Blue", "Yellow"]
newColor = ""
for c in colorList:
    newColor += c + ","
print(newColor)

# This is very efficient way
print("," .join(colorList))

