import random

x = random.randint(1, 6) # in range of 1 to 6
y = random.random() # from 0 to 1

list = ["some", "random", "list!"]
z = random.choice(list)

random.shuffle(list) # shuffles list items

print(list, x, y, z)
