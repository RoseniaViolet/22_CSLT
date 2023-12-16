# names = [1, 2, 3, 4, 5, 6]
# names.append(6)
# print(names)
# names.insert(0,7)
# print(names)
# names.insert(-1,8)
# print(names)
# names.insert(100,5)
# print(names)

# names = ['An', 'Nam', 'Binh', 'Ngoc']
# x=names.copy()
# print(x)
# print(x.count('Nam'))

names = ['An', 'Nam', 'Binh', 'Ngoc']
names.remove('An')
del(names[0])
x=names.pop(-2)
print(x)
print(names)

