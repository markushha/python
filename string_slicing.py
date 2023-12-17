# we can slice strs in python using indexing[] and slice()

some_str = "Quicker than duck, luckier than sock"

first_word = some_str[0:8]
# [start:stop:step]
# empty space makes it to the end of the string
str_with_steps = some_str[0:]

reversed_str = some_str[::-1]

# slice

slice_web = slice(8, -4)

print("https://markinger.com"[slice_web])
