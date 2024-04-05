N = int(input())
kol = 1
N_1 = 100000000
while N_1 > 1:
    N /= 2
    kol += 1
    N_1 = N
    N_1 /= 2
print(kol)


