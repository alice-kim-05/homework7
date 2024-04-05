N, K, R = map(int, input().split())
P = K / 100 + 1
L = N
kol = 1
while L <= R:
    L *= P
    kol += 1
print(kol)
