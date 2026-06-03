a = (1 > 0)
b = (1 < 0)

x = (a and b) or (a and not b)
print(x)

y = (not a or b) and (a or b)
print(y)