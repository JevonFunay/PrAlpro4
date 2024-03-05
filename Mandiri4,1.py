def cek_angka(a,b,c):
    if (a != b != c != a) and (a + b == c or a + c == b or b + c == a):
        return True
    else:
        return False
a = int(input("Masukkan Nilai A = "))
b = int(input("Masukkan Nilai B = "))
c = int(input("Masukkan Nilai C = "))
print(cek_angka(a,b,c))