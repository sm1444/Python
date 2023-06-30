user="Anand"
index = int(input("Enter index that is to be accessed: "))
try:
    x = user[index]
    print(x)

except IndexError:
    print("Index out of range")