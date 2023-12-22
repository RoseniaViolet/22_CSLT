# dùng để nối chuỗi theo phương pháp tham số
# %d : dữ liệu kiểu số nguyên
# %g : dữ liệu kiểu số thực
# %s : dữ liệu kiểu chuỗi (string)
n_decimal=3
n_float=2.5
st="Python"
print("Toi da hoc " + st + " lan thu " + str(n_decimal) + ", trong " + str(n_float) + " nam")
print("Toi da hoc %s lan thu %d, trong %g nam" % (st,n_decimal,n_float))