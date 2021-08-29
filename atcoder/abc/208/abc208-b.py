p = int(input())

kouka = []
for i in range(10):
    yen = 1
    for j in range(i+1):
        yen = yen * (j+1)
    kouka.append(yen)
kouka = sorted(kouka, reverse=True)

count = 0
for k in kouka:
    flag = True
    while flag:
        if p >= k:
            p = p - k
            count += 1
        else:
            flag = False

print(count)