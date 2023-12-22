L = []
n = int(input('n='))
SND = 0
TBC = 0
save = 0
dem = 0
for i in range(1, n + 1):
    L.append(int(input()))
for j in L:
    if j > 0:
        SND += 1
    if j % 2 == 0:
        save += j
        dem += 1
try:
    TBC = save / dem
except:
    TBC = 0

print(f'SND={SND}')
print(f'TBC={TBC}')
        

