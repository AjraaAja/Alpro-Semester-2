def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def hari_didalam_bulan(tahun, bulan):
    if bulan < 1 or bulan > 12:
        return None
    
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if bulan == 2 and tahun_kabisat(tahun):
        return 29
        
    return hari_per_bulan[bulan - 1]

data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    print(thn, bln, "->", end=" ")
    hasil = hari_didalam_bulan(thn, bln)
    if hasil == data_hasil[i]:
        print("Ok")
    else:
        print("Gagal")