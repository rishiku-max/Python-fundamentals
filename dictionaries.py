# Dictionaries in Python
# key-value pair
# key are work as set(they can't get duplicated)
# value are work like lists(they can be duplicated as many times)

# data = {0:34, 1:35, 2:67, 3:8}
# print(data)
# print(data[2])


# data = {'rishi':34, 'gagan':35, 'daksh':67, 'kartavya':8}
# print(data)
# print(data['kartavya'])
# print(data.get('rishi')) # same working
# print(data.get(1))     # it gives none
# print(data.get('daksh', 'not found'))     # it gives none
# print(data.get('arshit', 'not found'))

# making dictionaries by different way:

# keys = {'rishi', 'dhruv', 'daksh', 'gagan'}
# values = [2,4,5,5]
# dict1 = dict(zip(keys, values))
# print(dict1)

# Dictionary: key value pair

record = {}
record = {"name":"grish", "age":22, "batch":"c1", "ID": 3051}
print(record)
print(record["name"])
print(record["batch"])
print(len(record))
print(record.keys())
print(record.values())
print(record.items())
#print(record("age", 0 ))
record.update({"age":36})
record.pop("batch")
record.popitem()
record.setdefault("name", "grish")
#record.clear
new_dict = record.copy()
print(new_dict)

square = {i: i**2 for i in range(5)}
print(square)

