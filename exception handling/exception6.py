s1 = input("Enter first string: ")
i = int(input("Enter a number: "))

try:
    final = s1+i
    print("Result is: ",final)

except TypeError:
    print("String and integer cannot be concatened, it can be done by casting int to string")