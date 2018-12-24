
# assuming the file is not present in the directory

try:
    f = open("TestScript.csv", "r")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)