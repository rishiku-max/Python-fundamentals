import re
str = "Hello World"
x = re.findall("t", str)
print(x)

x = re.search("o", str)
y = x.start()
z = x.span()
m = x.string
print(x)
print(y)
print(z)
print(m)

str1 = "sunny sunny bunny"
x1 = re.split("un", str1)
print(x1)

x2 = re.split("s", str1)
print(x2)

x3 = re.split(" ", str1)
print(x3)

re.sub("sunny", "honey", str1)
print(str1)


