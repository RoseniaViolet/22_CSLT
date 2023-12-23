str = str(input('str='))
ch = (input('ch='))
dem = 0
for i in str:
    if ch.lower() == i.lower():
        dem += 1
print(f'Number of character {ch} is: {dem}')