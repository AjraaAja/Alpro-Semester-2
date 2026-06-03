pendapatan =float(input("Masukkan pendapatan Anda: "))
pajak = 0

if pendapatan <= 60_000_000:
    print(pendapatan,"tarif pajak 5%")
    tpajak = 0.05
elif pendapatan > 60_000_000:
    print(pendapatan,"tarif pajak 15%")
    tpajak = 0.15
elif pendapatan > 250_000_000:
    print(pendapatan,"tarif pajak 25%")
    tpajak = 0.25
elif pendapatan > 500_000_000:
    print(pendapatan,"tarif pajak 30%")
    tpajak = 0.30
else:
    print("Pendapatan tidak valid")
pajak = pendapatan * tpajak

print("Pajak yang harus dibayar adalah:",pajak,"rupiah")
