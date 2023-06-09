from functools import reduce

#li = [1,87,56,745,32]
#max = reduce(lambda x,y: x if x>y else y,li)
#print(max)

# count number of even numbers in a list

#li = [1,2,3,4,6,8]
#count = reduce((lambda num,x: num+1 if x%2==0 else num),li,0)   # 0 is the initial value of num
#print(count)

#fibonacci series using reduce 
#li = [0,1,2,3,4]
#series = list(reduce((lambda x,y:x+y)li,0,1))
#print(series)

#string concatenation

li = ["a","b","c","d"]
nl = reduce(lambda x,y: x+y,li)
print(nl)