import random

number = random.randint(0,1000)
counter = 0

while number != 7:
    counter = counter + 1 # counter += 1
    number = random.randint(0,1000)
    
    if counter > 1100:
        break
    
print(counter, number)

for i in range(10):
    print(i*2)
    
letters = ['A', 'B', 'C', 'D']

for letter in letters:
    print(letter.lower())