def func1(a):
    print(a)

func1(10)

func2 = lambda a:print(a)
func2(11)

def sum(a,b):
    return a+b

print(sum(10,12))

sum_1 = lambda a,b:a+b
print(sum_1(10,11))

def max(a,b):
    if(a>b):
        return a
    else:
        return b
    
print(max(5,4))

max_2 = lambda a,b: a if a>b else b
print(max(4,5))