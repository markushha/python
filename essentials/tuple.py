# tuple is a collection which is ucnhagneable
# they're similar to lists but only differs from them
# in the fact that they're immutable
# they're used to protect data (e.g: data from server)

tpl = ("Tea", "Coffee", 20, 21)

# print(tpl.count("Tea"), tpl.index(20))

# for x in tpl:
#     print(x)

def isInTuple(arg):
  if arg in tpl:
      return True
  else:
      return False

print(isInTuple(203))