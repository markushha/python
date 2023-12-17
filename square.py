# 2 nested loops should format a rectangle

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol to use: ")

for i in range (0, rows):
    str = ""
    for j in range(0, columns):
        str += symbol
    print(str)

# or 

# for i in range (0, rows):
#     for j in range(0, columns):
#         print(symbol, end = "")
#     print() # broke the line