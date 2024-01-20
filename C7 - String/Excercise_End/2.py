# gốc = str(input())
# khoảng_trắng = gốc.strip()
# # print(khoảng_trắng)
# In_hoa_chữ_đầu = khoảng_trắng.capitalize()
# # print(In_hoa_chữ_đầu)
# Tách_chuỗi = In_hoa_chữ_đầu.split()
# # print(Tách_chuỗi)
# gắn_chuỗi = ' '.join(Tách_chuỗi)
# # print(gắn_chuỗi)
# sạch = gắn_chuỗi.replace(' ,',',').replace(' ;',';').replace(' :',':').replace(' .','.')
# print(sạch)


# def xoa_khoang_trang_thua(s):
#     s=(' '.join(s.split()))
#     a=[' ,',' ;',' .']
#     for i in a:
#         if i in s:
#             s = s.replace(i,i[1])  
#     return s
# s = input()
# ket_qua = xoa_khoang_trang_thua(s)
# print(ket_qua)

# def xoa_khoang_trang_thua(s):
#     result = []
#     result = result.append(' '.join(s.split()))
#     a=[' ,',' ;',' .']
#     for i in a:
#         if i in result:
#             result = result.replace(i,i[1])  
#     return result
# s = input()
# ket_qua = xoa_khoang_trang_thua(s)
# print(*ket_qua)

def xoa_khoang_trang_thua(s):
    s = s.split('\n')
    for i in s:
        i = i.split('-')
        while '' in i:
            i.remove('')
        i = ' '.join(i)
        print(i)
        

s = input()
xoa_khoang_trang_thua(s)
