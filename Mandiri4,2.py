a = int(input("Masukkan Nilai A = "))
b = int(input("Masukkan Nilai B = "))
c = int(input("Masukkan Nilai C = "))
    
def cek_digit_belakang(a,b,c):
    if (a%10 == b%10 == c%10 == a%10) or (a%10 == b%10 or a%10 == c%10 or c%10 == b%10):
        return True
    else:
        return False
print(cek_digit_belakang(a,b,c))
    

