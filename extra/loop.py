
# y= int(input("Enter a number:"))
# i=1
# while i<=10:
#     x= y*i
    
#     print(f"{y} x {i} = {x}")
#     i+=1

# l = 3
# j = 2
# while l<=7: # true l =3
#     while j<=14: # j = 14
#         print(j) # 
#         if l==j:  # 3 ==6
#             j+=1
#             continue
#         j+=2
#     l+=1     

# prime numbers from 1 to 50

p = 1
while p<=50:
    counter = 0
    i = 1
    while i<=p:
        if p%i==0:
            counter+=1
        i+=1
    if counter == 2:
         print(p)
    p+=1                         

    
