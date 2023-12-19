# python has next logical operators - or / and / not

age = int(input("Your age zaebal: "))

if age >= 18 and age <= 60:
    print("Nice work mate")

# we also can write this as

if 18 <= age <= 60:
    print("Good Good " * 2)

# not is equal to ! before boolean in js

if not(60 <= age <= 18):
    print('GOOD')
