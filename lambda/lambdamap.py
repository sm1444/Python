#map function is used to get a manipualted list
#li = [1,2,3,4,5]
#nl = list(map(lambda x:x**2,li))
#print(nl)

####################

#li = ["ram","shyam","parth"]
#nl = list(map(lambda x:x.upper(),li))
#print(nl)

#####################

#li = [1,2,3,4]
#nl = list(map(lambda x: x**2 if x%2==0 else x**3,li))
#print(nl)

#####################

li=["shalvi m","aaryan","ram p"]
char=" "
nl = list(map(lambda x:x.title() if char in x else x.upper(),li))
print(nl)