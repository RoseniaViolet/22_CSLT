a='0huy11huybui12'
for i in range(len(a)):
    if a[i].isalpha():
        a = a.replace(a[i],' ')
a = a.split()
print(len(a))
