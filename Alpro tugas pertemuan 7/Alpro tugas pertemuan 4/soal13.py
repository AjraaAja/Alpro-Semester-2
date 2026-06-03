Jam = int(input("Waktu mulai (jam)"))
Menit = int (input("Waktu mulai (menit)"))
Durasi = int(input("Durasi (menit)"))
print ("Waktu selesai adalah", (Jam + (Menit + Durasi) // 60) % 24, "jam", (Menit + Durasi) % 60, "menit")