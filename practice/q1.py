#name = input("Enter your name: ")
#year = int(input("Enter year of study: "))
#enrollment = input("Enter your enrollment number: ")
#print("------------------")
#print(name)
#print(year)
#print(enrollment)
#print("------------------")

#divisible by 5 or not

#num = int(input("Enter a number: "))
#
#if(num%5==0):
#    print("divisible by 5")
#else:
#    print("not divisible by 5")

# to find the square root of a given number

#num = int(input("Enter a number: "))
#sqrt = num ** 0.5
#print("Square root of ",num," is ",sqrt)

#validity of a triangle
#a = int(input("Enter first side: "))
#b = int(input("Enter second side: "))
#c = int(input("Enter third side: "))
#
#if((a+b)>c and (b+c)>a and (c+a)>b):
#    print("Valid triangle")
#else: 
#    print("Invalid triangle")

#Print digits of a number in reverse order

#num = int(input("Enter a number: "))
#reverse = 0
#while(num>0):
#    temp = num % 10
#    reverse = (reverse*10)+temp
#    num = num // 10

#Fibonacci series

#n = int(input("Enter number upto which the series is to be printed: "))
#n1 = 0
#n2 = 1
#print(n1)
#print(n2)
#for i in range(n+1):
#    sum = n1+ n2
#    print(sum)
#    n1 = n2
#    n2 = sum

#number series

#num =0
#for i in range(100):
#    print(num+1)
#    num+=1
#print("------------")
#num = 101
#for i in range(100):
#    print(num-1)
#    num-=1
#
#print("---------")
#num = 0 
#for i in range(50):
#    print(num+1)
#    num+=2
#
#print("-----------")
#num = 1
#for i in range(50):
#    print(num+1)
#    num+=2

#Armstrong number#
#num = int(input("Enter a number: "))
#safe = num
#sum = 0
#while num>0:
#    temp = num%10
#    sum = sum + (temp*temp*temp)
#    num = num //10
#if(safe == sum):
#    print("Armstrong number")
#else:
#    print("Not an armstrong number")

#list1 = [13,23,35,4,5,6,7]
#list2 =[11,22,33,44,55,66,77]
#dict={}
#
#dict2 = list(zip(list1,list2))
#print(dict2)
#
#for i in range(0,len(list1)):
#    dict[list1[i]]=list2[i]
#   
#   
#print(dict)

#users = ["raj","ram","parth"]    
#users.extend(["viraj","vraj"])
#print(users)

#studnts = ["John", "Jennie", "Jim", "Jack", "Joe"]
#
#digits=[12,22,34,56,7,9]
#
#print(studnts)
#print(studnts[0:3])
#print(studnts[1:4])
#print(studnts[:3])
#print(studnts[2:])
#print(studnts[-1])
#print(studnts[0:-1])
##reverse the list using slicing
#print(studnts[::-1])
#print(studnts[::-3])
#print(studnts[-1::-1])
