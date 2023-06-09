# tuple does not support comprehension as it is not mutable

#word = "india"
#dict1 = {}
##for i in word:
##    dict1[i]=i+i+i
##print(dict1)
#
#dict1 = {i:i+i+i for i in word}
#print(dict1)

######################################################

#dict3 = {i:i**3 for i in range(11) if i%2==0}
#print(dict3)

######################################################

#str = "hello this is india"
#dict = {i:i for i in str}
#print(dict)

######################################################

x = set(["naman","parth","kay","madam","malayalam","amit"])

set1 = {i for i in x if i == i[::-1]}
print(set)