def Liter100km_ke_mpg(liter):
    mil_dalam_meter = 1609.344
    galon_dalam_liter = 3.785411784
    
    mil = 100000 / mil_dalam_meter
    galon = liter / galon_dalam_liter
    
    return mil / galon

def mpg_ke_Liter100km(mil):
    mil_dalam_meter = 1609.344
    galon_dalam_liter = 3.785411784
    
    liter = galon_dalam_liter * 100000
    km100 = mil * mil_dalam_meter
    
    return liter / km100

print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))