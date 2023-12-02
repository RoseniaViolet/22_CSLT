# def Nhap():
#     return int(input('n='))
# def NhapVaDem(*DS_cac_so):
#     so_chan = 0
#     for i in DS_cac_so:
#         if i % 2 == 0:
#             so_chan += 1
#     return so_chan
# def InKQ(Kq):
#     print(f'So chu so chan la: {Kq}')
#     # main code
# n = Nhap()
# so_chan = NhapVaDem(*[int(input()) for _ in range(n)])
# InKQ(so_chan)           
def Nhap():
    return int(input('n='))
def NhapVaDem():
    Dem = 0
    print('Nhap 7 so nguyen:')
    for i in range(1,n+1):
        x = int(input())
        if x % 2 == 0:
            Dem = Dem + 1
    return Dem
def InKQ(kq):
    print('So chu so chan la:',kq)
n = Nhap()
kq = NhapVaDem(n)
InKQ(kq)
# InKQ(NhapVaDem(Nhap))
            
    