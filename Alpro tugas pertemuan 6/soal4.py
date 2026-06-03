print( """       +=====================================================+" 
       |     selamat datang di game saya muggle!              |
       |     saya telah memilih sebuah angka rahasia          |
       |     antara 1 dan 100. coba tebak angka tersebut!     |
       +=====================================================+
       ======+""")
angka_rahasia = 13

angka_yang_ditebak = int(input("Masukkan tebakan Anda: "))
while angka_yang_ditebak != angka_rahasia:
    print("haha! kamu nyangkut deh di loop saya!")
    angka_yang_ditebak = int(input("Masukkan tebakan Anda: "))
print("Selamat! Anda menebak dengan benar!")