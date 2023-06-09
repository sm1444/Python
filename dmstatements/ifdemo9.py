print("Enter 1 for pizza.")
print("Enter 2 for burger.")
no = int(input("Enter a number: "))
pizza = 0
crust = 0
burger = 0

if no==1:
    print("You have selected pizza")
    print("Enter 1 for veg pizza")
    print("Enter 2 for non-veg pizza")
    pizza = int(input("Enter a number for pizza:"))
    if pizza ==1:
        print("You have selected veg pizza")
        print("Enter 1 for thin crust")
        print("Enter 2 for thick crust")
        print("Enter 3 for cheese burst")
        crust = int(input("Enter a number for crust: "))
        if crust == 1:
            print("You have selected thick crust")
        elif crust == 2:
            print("You have selected thin crust")
        elif crust==3:
            print("You have selected cheese burst.")
        else:
            print("Ypu have selected wrong option.")
    elif pizza == 2:
        print("You have selected non-veg pizza")
        print("Enter 1 for thin crust")
        print("Enter 2 for thick crust")
        print("Enter 3 for cheese burst")
        crust = int(input("Enter a number for crust: "))
        if crust == 1:
            print("You have selected thick crust")
        elif crust == 2:
            print("You have selected thin crust")
        elif crust==3:
            print("You have selected cheese burst.")
        else:
            print("Ypu have selected wrong option.")    
    else:
        print("You have selected wrong option")
elif no==2:
    print("You have selected burger")
    print("Enter 1 for veg burger")
    print("Enter 2 for non-veg burger")
    burger = int(input("Enter a number for burger:"))
    if burger ==1:
        print("You have selected veg burger")
    elif burger == 2:
        print("You have selected non-veg burger")
    else:
        print("You have selected wrong option")
else:
    print("You have selected wrong option.")        