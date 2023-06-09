#fibonacci series

num1 = 0
num2 = 1
sum = 0
print(num1)
print(num2)
for i in range(1,8):
    sum = num1 + num2
    print(sum)
    num1 = num2
    num2 = sum
    