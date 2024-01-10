def XuLyCode(danhSach,n):
    i = 0
    j = 0  
    for _ in range(n):
        if i < len(danhSach) :
            print(danhSach[i],end=' ')
            i += 1
        elif len(danhSach) <= i < n:
            print(danhSach[j],end=' ')
            j += 1
            i += 1
        else:
            break
        
danhSach = input().split()
print(danhSach)
print(len(danhSach))
if not danhSach:
    print("Danh sach rong")
else:
    try:
        n = int(input())
        while n < 0:
            print('Vui long nhap lai')
            n = int(input())
    except ValueError:
        print('Vui long nhap 1 so nguyen')
    else:
        XuLyCode(danhSach,n)
