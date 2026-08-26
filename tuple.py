#List [] = mutable, most flexible
#Tuple () = immutable, faster
#Set {} = mutable (add/remove), unordered
#         NO duplicates, best ofr membership testing

fruits = ("apple", "bannana", "orange", "coconut")


for fruit in fruits:
    print(fruit, end=" ")