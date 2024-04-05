t = float(input())
kol = 0
while t != 0:
    t_0 = t
    t = float(input())
    if t == 0:
        break
    if t < t_0:
        kol += 1
print(kol)
