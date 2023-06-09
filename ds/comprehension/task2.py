#dictionary comprehension

dict1 = {1:"one",2:"two",3:"three",4:"four",5:"five"}
dict2 = {i: j for i,j in dict1.items() if len(j)>3}
#for i , j in dict1.items():
#    if len(j)>3:
#        dict2[i] = j
print(dict2)

##################################################
list = [1,2,3,4,5,6,7,8,9,10]
dict = {i:i*i for i in list}
#for i in list:
#    dict[i] = i*i
print(dict)