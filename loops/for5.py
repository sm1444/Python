base  = int(input("Enter base: "))
power = int(input("Enter power: "))
pow=1
for i in range(1,power+1):
    pow = pow * base
print("Answer is: ",pow)