def nhap():
    L = input().split()
    L = list(map(int,L))
    return L

def count(L):
    if len(L) < 2:
        return False
    return True

def tang_dan(L):
    if ketqua == True:
        for j in range(len(L)+1):
            if j + 1 < len(L):
                if  L[j] > L[j+1]:
                    return "Khong"
            else:
                return "Co"
    else:
        return "Khong"
    
L = nhap()
ketqua = count(L)
print(tang_dan(L))