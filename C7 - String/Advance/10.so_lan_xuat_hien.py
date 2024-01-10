s = str(input())
def ky_tu_khong_trung_lap(s):
    chuoiketqua = ''
    for i in s:
        if i not in chuoiketqua:
            chuoiketqua += i
    return chuoiketqua
def dem_ky_tu(s):
    ChuoiKytu = ky_tu_khong_trung_lap(s)
    for x in ChuoiKytu:
        dem = s.count(x)
        print(f''''{x}':{dem}''',end=';')
dem_ky_tu(s)