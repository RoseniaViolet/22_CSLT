def xoa_khoang_trang_thua(s):
    s = s.strip()
    return ' '.join(s.split())

def can_giua_cac_cau(s):
    dsCacCau = s.split('.')
    maxDoDaiCau = 0
    for cau in dsCacCau:
        cau = xoa_khoang_trang_thua(cau)
        if len(cau) > maxDoDaiCau:
            maxDoDaiCau = len(cau)
    for cau in dsCacCau:
        cau = xoa_khoang_trang_thua(cau)
        cau = cau.title()  # Gán lại giá trị của cau sau khi sử dụng title()
        print(cau.center(maxDoDaiCau))

s = input()
can_giua_cac_cau(s)
