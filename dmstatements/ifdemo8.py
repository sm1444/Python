age = int(input("Enter your age: "))

if age>=18:
    print("You are eligible to vote.")
    if age>21:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage but can vote.")
else:
    print("You are not eligible for voting.")
    if age>=14:
        print("You are eligible for school.") 
    else:
        print("You are not eligible for school,")           