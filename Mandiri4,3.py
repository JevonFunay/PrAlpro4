print("Pilih 1 untuk Fahrenheit, Pilih 2 untuk Reamur")
opsi = int(input("Pilihan anda = "))
if opsi == 1:
    c = int(input("Masukkan Celcius = "))
    fahrenheit = lambda c : (9/5)*c+32
    print(fahrenheit(c))
elif opsi == 2:
    c = int(input("Masukkan Celcius = "))
    reamur = lambda c : 0.8*c
    print(reamur(c))

     