import random

number = random.randint(0,10)

thresh = 5

if number > 8:
    print("Very Large Number")
elif number > thresh:
    print("Large Number")
elif number < thresh:
    print("Small Number")
else: # elif number == thresh
    print("Number is", thresh)
    
print(number)