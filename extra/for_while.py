x = "Hello Ashok "
print(x*3)

x = 90
print(x**3)   # 90 * 90 * 90

# while Loop

# _ = 1   # Intialization   -> start Point
# while _ <= 100:   # Condition  -> End Point
#     print(_,end=' ')   # Statement
#     _ += 1   # Flow (Asignment O/p -> Priority Low)  # _ = _ + 1

# --------------------
# i = 99

# while i >= 1:
#     print(i,end=' ')
#     i-=2


# --------------------
i = 100

# while i >= 1:
#     if i % 5 == 0 or i % 7 == 0:   # 1 1  -> 1     # 1 0 -> 1
#         print(i,end=' ') # 100 98 95 91 90 85 84 80 77 75 70 65 63 60 56 55 50 49 45 42 40 35 30 28 25 21 20 15 14 10 7 5
#     i-=1

#------------------------
i = 100

while i >= 1:
    if  i % 5 == 0 or i % 7 == 0 and (i%3 == 0 and i% 2 == 0):    # Logical Operator
        print(i,end=' ') 
    i-=1  # 100 95 90 85 84 80 75 70 65 60 55 50 45 42 40 35 30 25 20 15 10 5


print()
x = 90
if x is not 90:   # Identity Operator -> is, is not
    print(True)
else:
    print(False)


# --------------------
print()


# k = 3

# while k <= 13:
    
#     k += 1
#     if k==6:
#         continue
#     print(k)


# k = 3

# while k <= 13:
    
#     k += 1
#     if k==6:
#         break
#     print(k)



l = 3 
while l<=7:  # l = 4
    j = 2   # j = 2
    while j <= 14:  #  j = 5
        print(j)   # 2 4 5
        if l== j:   # 4 == 5
            j+=1    # j = 5
            continue
        j+=2  # j = 7
    l+=1   # 4

# Prime, Palindrome,Armstrong, Perfect, Twin, SUm of Digits, reverse Number, TOtal Digits


# Prime Number

# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47 .......

# 24 = 1,2,3,4,6,8,12,24
# 23 = 1,23
# 41 = 1,41
# 56 = 1,2,4,7,8,14,28,56


p = 1   # start

while p <= 10000:   # End   # p = 29
    counter = 0   # Reset
    i = 1         # Reset
    while i<=p:  # i <= 29
        # print(i)
        if p % i == 0:   # 28 % 4 == 0
            # print(i,end=' ')
            counter += 1   # 3
        i+=1 

    if counter==2:   # 3 == 2
        print(p,end=' ')
    p+=1  # Flow


# 1 to 10000 -> Print Prime Numbers