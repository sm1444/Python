#li = ["dev","aa","shalvi","bb","aaryan"]
#fl=list(filter(lambda x:(len(x)>=3 and x[0]=='a'),li))
#print(fl)

#store leap year in a new list

#li = [2004,2005,2008,2020,2024]
#fl=list(filter(lambda x:((x%4==0 and x%100!=0) or (x%400==0)),li))
#print(fl)

#name contains specific character
li = ["dev","aa","shalvi","bb","aaryan"]
char = 'a'
fl = list(filter(lambda x:(char in x),li))
print(fl)

#contains space in a new list
li2 = ["shalvi m","aaryan","dev m"]
char2=" "
lf2=list(filter(lambda x:(char2 in x),li2))
print(lf2)