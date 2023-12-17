drinks = ["coffee", ["capuccino", "latte"], "food", ["pizza", "sushi"]]

menu = "Discover our menu! "

for i in drinks:
    if isinstance(i, list):
        for j in i:
            menu += j + ", "
        menu += ". "
    else:
        menu += i.capitalize() + ": "

print(menu)