#for i in range(3):
#    for j in range(3-i,0,-1):
#        print(" ",end = "")
#    for k in range(i+1):
#        print("* ",end =" ")
#    print("\n")
#
#for i in range(1,4):
#    for j in range(4-i,1,-1):
#        print(" ",end="")
#    for k in range(i):
#        print(" *",end=" ")
#    print("\n")

#inverted pyramid
#for i in range(3):
#    for j in range(1,i+1):
#        print(" ",end = "")
#    for k in range(3-i,0,-1):
#        print(" * ",end=" ")
#    print("\n")

#Solid square pattern
#for i in range(4):
#    for j in range(4):
#        print(" * ",end="")
#    print("\n")

#Hollow square pattern
row = int(input("Enter number of rows: "))

print("Hollow sqaure pattern is: ")
for i in range(1,row+1):
    for j in range(1,row+1):
        if i==1 or i==row or j==1 or j==row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()