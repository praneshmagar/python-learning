#List [] = mutable, most flexible
#Tuple () = immutable, faster
#Set {} = mutable (add/remove), unordered
#         NO duplicates, best ofr membership testing



#sets we can add and remove element but cant replace any elements because sets are unordered
#we can not access them by index like fruits[0] == "[pineapple]" nor pop
#we can not duplicate
#best for membership testing basically testing if there is a given value in our set
#we can accept user input and search for inside set

fruits = {"apple", "bannana", "orange", "coconut"}
fruits.add("beer")
fruits.remove("coconut")
#fruits.clear() #can clear

fruit = input("enter a fruit to search for: ")

if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")



#for fruit in fruits:
#    print(fruit, end=" ")