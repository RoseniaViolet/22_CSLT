def in_list(danhSach):
    for i in range(len(danhSach)):
        print(f'{i} {danhSach[i]}')

danhSach = input().split()

# in_list(danhSach)

# def kiem_tra_ds_giam(danhSachSo):
#    #Cach 1
#    # for soThuTu in range(len(danhSachSo) - 1):
#    #     #So sanh 2 phan tu lien ke nhau
#    #     if danhSachSo[soThuTu] < danhSachSo[soThuTu + 1]:
#    #         return False
#    # return True

#    #Cach 2
#    ketQua = all(danhSachSo[soThuTu] >= danhSachSo[soThuTu+1] for soThuTu in range(len(danhSachSo)-1))
#    return ketQua
  

# #Nhap danh sach tu ban phim
# danhSach = input().split()
# #Kiem tra xem danh sach co rong hay khong
# if len(danhSach) == 0:
#    print("Danh sach rong")
# else:
#    #Khoi lenh co the phat sinh loi
#    try:
#        #Ep kieu du lieu sang so thuc
#        danhSachSo = list(map(float, danhSach))
#        #Goi thuc thi ham va truyen tham so cho ham
#        ketQua = kiem_tra_ds_giam(danhSachSo)
#        print(ketQua)
#    #Khoi lenh duoc thuc thi khi loi xay ra
#    except:
#        print("Vui long nhap cac phan tu la so thuc!")
