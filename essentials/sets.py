# set is set. hashsets :))))

some_set = {"Mark", "John", "Mark", "Kate", "Ido"}
other_set = {"Green", "White", "Blue"}

some_set.add("Jacob")

# merge two sets
some_set.update(other_set) # mutates some_set
some_set.union(other_set) # doesn't mutate some_set

# for x in some_set:
#     print(x)

# differences in 2 sets

print(some_set.difference(other_set)) # what some_set has that other_set doesn't
print(some_set.intersection(other_set)) # what 2 sets have in common

# if "Mark" in some_set:
#     print(True)