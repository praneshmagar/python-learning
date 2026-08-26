#List [] = mutable, most flexible
#Tuple () = immutable, faster
#Set {} = mutable (add/remove), unordered
#         NO duplicates, best ofr membership testing

fruits = ["apple", "bannana", "orange", "coconut"]

#fruits[3] = "Pineapple"   #replaces fruits at index 3 for pineapple

#fruits.append("mange") #adds mange to the end of list

#fruits.remove("apple") #removes apple from list

fruits.pop(1) #pops/removes whatever index 1 is from list

for fruit in fruits:
    print(fruit, end=" ")