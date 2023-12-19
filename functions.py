# functions is functions

import math

def nroot(x, n):
    return math.pow(x, 1/n)

# print(nroot(256, 4))

# keyword arguments

def greetUser(first_name, last_name):
    return f'Welcome, {first_name} {last_name}!'

# print(greetUser(last_name="Inger", first_name="Mark"))

# *args (are accepted as a tuple data type)

def summarize(*args):
    sum = 0

    for i in args:
        if not isinstance(i, int):
            if isinstance(i, str) and i.isdigit():
                sum += int(i)
            
            continue

        sum += i

    return sum

# print(summarize("123", 2, 3, 4, 5, "656", 7, 8, "Aa"))

# **kwargs - same as *, but are accepted as a dictionary

def useless(**dict):
    for _, val in dict.items():
        print(val)

    return f"{dict['num1']}, {dict['num2']}"

# print(useless(num1=123, num2=234))

# just normal arrays ... 

def mean(list):
    sum = 0

    for i in list:
        sum += i

    return sum / len(list)

print(mean([2, 3, 4, 5, 6, 6]))