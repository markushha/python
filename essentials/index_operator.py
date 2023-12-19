# index operator [] gives access to a sequence's element (str, list, tuple)

name = "mark Inger"

if (name[0].islower()):
    name = name.capitalize()

print(name[0:4])
print(name[5:].capitalize())

last_char = name[-1]

print(last_char)