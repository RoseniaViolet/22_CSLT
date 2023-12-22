str = str(input())
ch = (input())
dem = 0
for i in str:
    if ch == i:
        dem += 1
print(f'Number of character {ch} is: {dem}')