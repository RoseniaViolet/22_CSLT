gốc = str(input())
khoảng_trắng = gốc.strip()
# print(khoảng_trắng)
In_hoa_chữ_đầu = khoảng_trắng.capitalize()
# print(In_hoa_chữ_đầu)
Tách_chuỗi = In_hoa_chữ_đầu.split()
# print(Tách_chuỗi)
gắn_chuỗi = ' '.join(Tách_chuỗi)
# print(gắn_chuỗi)
sạch = gắn_chuỗi.replace(' ,',',').replace(' ;',';').replace(' :',':').replace(' .','.')
print(sạch)
