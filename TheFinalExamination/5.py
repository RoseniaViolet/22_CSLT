st1=input().lower()
st2=input().lower()
def ham(st1,st2):
    for x in st2:
        ket_qua=st1.find(x)
        if ket_qua < 0:      
            return False
    return True
print(ham(st1,st2))