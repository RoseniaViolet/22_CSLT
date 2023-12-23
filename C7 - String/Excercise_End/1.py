A = str(input())
In_hoa = 0
In_thuong = 0
chu_so = 0
khac = 0

for i in A:
    if i.isalpha():
        if i == i.lower():
            In_thuong += 1
        else:
            In_hoa += 1
    elif i.isnumeric():
        chu_so += 1
    else:
        khac += 1
        
print('In hoa:',In_hoa)
print('In thuong:',In_thuong)
print('Chu so:',chu_so)
print('Khac:',khac)