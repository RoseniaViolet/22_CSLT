def Nhap():
    n = int(input('n='))
    return n
def NhapVaDem(*DS_cac_so):
    so_chan = 0
    for i in DS_cac_so:
        if i % 2 == 0:
            so_chan += 1
    return so_chan
def InKQ(Kq):
    print(f'So chu so chan la: {Kq}')
    # main code
n = Nhap()
so_chan = NhapVaDem(*[int(input()) for _ in range(n)])
InKQ(so_chan)           