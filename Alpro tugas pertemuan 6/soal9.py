kata = input("Masukkan sebuah kata: ").upper()
for huruf in kata:
    if huruf in "AEIOU":
        continue
    else:
        print(huruf)