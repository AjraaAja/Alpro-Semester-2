exo = []

exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

anggota = ["DO", "Bakhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]    
for member in anggota:
    exo.append(member)

del exo[6]
del exo[7]
del exo[7]

exo.insert(-3, "Xiumin")

print(exo)
print("Jumlah anggota exo:", len(exo))