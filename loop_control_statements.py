# break - man i mean it's obvious
# continue - skips iteration
# pass - does nothing

while True:
    name = input("Enter your name: ")
    if name.strip() != "":
        break

for i in range(10 + 1):
    if i % 2 != 0:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass
    else:
        print(i*i)