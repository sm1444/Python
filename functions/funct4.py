#return student name who is having highest marks
def students(st):
    max = 0
    name=" "
    for i ,j in st.items():
        if j>max:
            j = max
            name = i
        return name


st={'shalvi':98,'aaryan':94,'dev':95}
x  = students(st)
print(x)