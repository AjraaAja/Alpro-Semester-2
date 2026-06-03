Angka1 = int(input("Masukkan angka pertama: "))
Angka2 = int(input("Masukkan angka kedua: "))
Angka3 = int(input("Masukkan angka ketiga: "))

if Angka1 > Angka2 and Angka1 > Angka3:
    AngkaBesar = Angka1

elif Angka2 > Angka1 and Angka2 > Angka3:
    AngkaBesar = Angka2

elif Angka3 > Angka1 and Angka3 > Angka2:
    AngkaBesar = Angka3

print("Angka yang lebih besar adalah:", AngkaBesar)