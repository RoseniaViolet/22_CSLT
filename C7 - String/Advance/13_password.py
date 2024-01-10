p=str(input())
a = p.split()
dem  =0
for i in a:
    if  (i.isnumeric()) or (i.isalpha()):
        dem += 0
    else:
        dem += 1
print(dem)