#if statements = execute some code only if  acondition is True
#they allow for basic decisimion making (if, elif, else)

age = int(input("Enter your age: "))
has_ticket = True
price = 10.00


if age >= 65:
    print("wsg big dawg")
    print(f"The ticket pice for a senior is ${price*0.75}")
elif age >= 18:
     print("You are of age")
     print(f"The ticket pice for an adult is $ {price}")     
else:
     print("You are young")
     print(f"The ticket pice for a kid is ${price*0.5}")


if has_ticket:
     print("You can enter, you have a ticket")
else:
     print("You dont have a ticket!")     