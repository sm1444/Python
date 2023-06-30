tuple1 = ("shalvi","mahi","rahil","dhyey","daksh")

try:
    tuple1.insert("Anusha")

except AttributeError:
    print("Tuple is not mutable")
