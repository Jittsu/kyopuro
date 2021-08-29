N, K = map(int, input().split())
a = list(map(int, input().split()))

if N == 1:
    print(K)
else:
    junban = [i for i in range(N)]
    zennin = K // N
    amari = K - zennin * N
    zennin_ames = [zennin for _ in range(N)]
    mynumber2amenum = dict(zip(a, zennin_ames))
    junban2mynumber = dict(zip(junban, a))
    sorted_a = sorted(a)
    if not amari == 0:
        for hito in sorted_a:
            mynumber2amenum[hito] += 1
            amari -= 1
            if amari == 0:
                break
            else:
                pass
    else:
        pass

    for j2m in junban:
        print(mynumber2amenum[junban2mynumber[j2m]])