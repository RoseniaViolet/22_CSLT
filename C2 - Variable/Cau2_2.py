GiaNiemYet=int(input('Nhap Gia niem yet: '))
ChietKhau=int(input('Nhap Chiet khau: '))
VAT=float((GiaNiemYet - ChietKhau)*0.01)
print('Gia ban: ' + str(float(GiaNiemYet - ChietKhau + VAT)))