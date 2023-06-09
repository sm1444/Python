# reverse each element of a list using functions
list1 = [19,33,45,167]

def reverseelm(data):
    reversed_list = []
    for i in data:
        num = i
        reversed_num = 0
        while num>0:
            temp = num%10
            reversed_num = (reversed_num*10)+temp
            num//=10
        reversed_list.append(reversed_num)
    print(reversed_list)

reverseelm(list1)