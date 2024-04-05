N = int(input())
ost = N / 2
for i in range(0, N):
    ost /= 2
    if (ost == 1.0) or (N / 2 == 1.0):
        print('Верно')
        break
    elif (int(ost) * 2) < (ost * 2):
        print('Неверно')
        break
