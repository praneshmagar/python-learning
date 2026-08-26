#while loop = used to repeat a block of code aslong as a condition remains 'True'
# we recheck the condition at the end of the loop



name = input("Enter your name: ")

while name == "":
    name = input("Enter your name: ")



age = input("enter your age: ")

while age == "" and age < 0:
    age = input("Please enter a valid age")

age = int(age)


print(f"Hello {name}")
print(f"You age are {age} years old!")
