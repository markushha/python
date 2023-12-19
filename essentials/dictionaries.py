# dictionary is like an objects in js. 
# A changeable, unordered collection of UNIQUE key:value pairs

capitals = {
    "USA": "Washington DC",
    "Russia": "Moscow"
}

# print(capitals.get("USA"))
# print(capitals.values())
# print(capitals.keys())
# print(capitals.items())

capitals.update({
    "Germany": "Berlin"
})

# capitals.pop("USA")

# capitals.clear()

for [key, value] in capitals.items():
    print(key + ': ' + value)