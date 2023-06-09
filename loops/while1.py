no = 153
safe = no
sum = 0
temp = 0
while(no>0):
    temp = no%10
    sum = sum + (temp*temp*temp)
    no = no//10

if (safe==sum):
    print("Armstrong number")
else:
    print("Not Armstrong number")
