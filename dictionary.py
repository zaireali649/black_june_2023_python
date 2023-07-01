var = {}

print(type(var))

var2 = {"juice": "cranberry", "fruit":"mango"}

print(var2)

print(var2["fruit"])

var2["food"] = "sandwich"

print(var2)

del var2["juice"]

print(var2)

var2["food"] = "pasta"

print(var2)

print(dir(var2))

print(list(var2.keys()))

print(list(var2.values()))

print(list(var2.items()))

for k, v in var2.items():
    print(k, v)
    
dict_of_lists = {"A": [0, 1, 2], "B": [2, 3, 4], "C": [4, 5, 6]}

for k, v in dict_of_lists.items():
    print(k, v)
