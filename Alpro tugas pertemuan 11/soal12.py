def cek_prima(bilangan):
    # Bilangan prima harus lebih besar dari 1
    if bilangan <= 1:
        return False
    
    # Mengecek apakah bilangan habis dibagi angka lain selain 1 dan dirinya sendiri
    for j in range(2, bilangan):
        if bilangan % j == 0:
            return False # Jika habis dibagi angka lain, maka bukan prima
            
    return True # Jika lolos dari semua pengecekan, maka prima

# Kerangka kode bawaan dari soal
for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()