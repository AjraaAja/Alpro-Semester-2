print( """       +=====================================================+" 
       |     selamat datang di game saya muggle!              |
       |     saya telah memilih sebuah angka rahasia          |
       |     antara 1 dan 100. coba tebak angka tersebut!     |
       +=====================================================+""")
secret_number = 12

while True:
    guess = int(input("Masukkan tebakan Anda: "))
    if guess == secret_number:
        print("Selamat! Anda menebak dengan benar!")
        break
    else:
        print("haha! kamu nyangkut deh di loop saya!")