A = str(input())
chu_cai = 0
chu_so = 0
for i in A:
    if i.isalpha():
        chu_cai += 1
    elif i.isnumeric():
        chu_so += 1
print('Chu cai:',chu_cai)
print('Chu so:',chu_so)