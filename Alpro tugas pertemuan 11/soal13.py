def cek_prima(bilangan):
    if bilangan <= 1:
        return False
     
    for j in range(2, bilangan):
        if bilangan % j == 0:
            return False
            
    return True 
for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()