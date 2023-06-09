no = int(input("Enter a number: "))
evensum=0
oddsum = 0
for i in range(1,no+1):
    if(i%2==0):
        print("Even number: ",i)
        evensum = evensum+i
    elif(i%2==1):
        print("Odd number: ",i)
        oddsum = oddsum +i

print("Even sum: ",evensum)
print("Odd sum: ",oddsum)