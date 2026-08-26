#logical operators = evaluate multiple conditions (or, and, not)
# or = atleast one condition must be true
# and = both conditions must be true
# not = inverts the condition (not false, not true)


#temp = 35             OR GO DOWN
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
#    print("The outdoor event is canceled")
#else:
#    print("The outdoor event is still scheduled")



#temp = 20              AND  GO DOWN
#is_sunny = True

#if temp >= 28 and is_sunny:
#    print("It is hot outside 🤪")
#    print("It is sunny ☀️")
#elif temp <= 0 and is_sunny:
#    print("It is cold outside 🥶")
#    print("It is sunny ☀️")
#elif 28 > temp > 0 and is_sunny:
#    print("It is warm outside 😀")
#    print("It is sunny ☀️")

temp = -8             
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside 🤪")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is cold outside 🥶")
    print("It is sunny ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside 😀")
    print("It is sunny ☀️")
if temp >= 28 and not is_sunny:
    print("It is hot outside 🤪")
    print("It is Cloudy ⛅")
elif temp <= 0 and not is_sunny:
    print("It is cold outside 🥶")
    print("It is Cloudy ⛅")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside 😀")
    print("It is Cloudy ⛅")    