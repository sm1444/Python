lang = ("C","C++","Python")
print(lang)

lang2=list(lang)

lang2.append("Java")

print(lang2)

lang=tuple(lang2)  #reinitialization of tuple not reassignment as tuple is immutable
print(lang)