#prime numbers from 1 to 10000
p = 1
while p <=10000:
     counter = 0
     i = 1
     while i <=p:
         if p % i == 0:
            counter+=1
         i+=1
     if i%2 == 0:
        print(p,end=" ")
     p+=1    










