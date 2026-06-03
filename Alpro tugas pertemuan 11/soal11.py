, bulan):
    if bulan < 1 or bulan > 12:
        return None
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bulan == 2 and tahun_kabisat(tahun):
        return 29
    return hari_per_bulan[bulan - 1]

def hari_pada_tahun(tahun, bulan, hari):
    if bulan < 1 or bulan > 12:
        return None
    
    maksimal_hari = hari_didalam_bulan(tahun, bulan)
    if hari < 1 or hari > maksimal_hari:
        return None
    
    total_hari = 0
    for b in range(1, bulan):
        total_hari += hari_didalam_bulan(tahun, b)
        
    total_hari += hari
    return total_hari
print(hari_pada_tahun(2000, 12, 31)) 