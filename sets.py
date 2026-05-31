# sets = unordered, unique

#a = {}
#type(a)
# a = {10,}
# b = set()
a = {10, 20, 30, 40, 50}
# a.add(50)
# a.remove(20)
# a.remove(80) error
# a.pop()
# print(a)
myset = {"apple", "banana", "cherry"}
myset.add("orange")
print(myset)
myset.update(a)
print(myset)

myset.remove("apple")
myset.discard("orange")
myset.pop()
print(myset)
myset.clear()
myset.copy()
print(myset)
