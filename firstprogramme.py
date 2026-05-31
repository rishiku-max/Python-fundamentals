text = 'Irishi'
text[1]
print(text[1])
print(text[-1])

nums = [10, 20, 30, 40, 50]
mix = ['rishi', 67, 6.7, ]
print(mix)
 
mix1 = [nums, mix]
print(mix1)
print(mix1[1])
print(mix1[0][1])
mix2 = nums + mix
print(mix2)
# unpacking ............
num = (2, 'rishi', 4.5)
ab, bc, cd = num
print(ab)
print(bc)
print(cd)

# making tuple from immutable to mutable
tubB = (12, 34, 'rishi', [2,3,4,5,6])
tubB[3][4] = 98
print(tubB)

# a variable inbult
34 in tubB # it will give True as answer

# set and operations
set2 = set(2,3,4,5,5,6,6,7,7)
set3 = set(1,3,4,5,6,7,7,7,7,6,5,5,4,4,4,4,34,34,34,54,54,56,65,67,7)
print(set2 - set3)
print(set2 | set3)
print(set2 & set3)
print(set2 ^ set3)
