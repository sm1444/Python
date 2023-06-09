# prime number
#24= 1, 2 , 3 ,4,5,8,2,24

num=int(input("Enter number:"))
count = 0
i = 1
while i<=num:
    if num % i ==0:
        print(i,end=" ")
        count+=1
    i+=1
print()
print(count)    
if count ==2:
    print("prime",num)

# prime numbers between 1 to 10000    