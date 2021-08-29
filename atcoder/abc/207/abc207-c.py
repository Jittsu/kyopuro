N = int(input())
tlr = []
for i in range(N):
    ipt = list(map(lambda x: int(x), input().split(' ')))
    tlr.append(ipt)

ans = 0
for i in range(N-1):
    for n in range(i+1, N):
        if (tlr[i][1] < tlr[n][1]) and (tlr[n][1] < tlr[i][2]):
            ans += 1
        elif (tlr[i][1] < tlr[n][2]) and (tlr[n][2] < tlr[i][2]):
            ans += 1
        elif (tlr[i][1] == tlr[n][1]):
            ans += 1
        elif (tlr[i][2] == tlr[n][2]):
            ans += 1
        elif (tlr[i][1] > tlr [n][1]) and (tlr[i][2] < tlr[n][2]):
            ans += 1
        else:
            if tlr[i][2] == tlr[n][1]:
                if (tlr[i][0] == 1) or (tlr[i][0] == 3):
                    if (tlr[n][0] == 1) or (tlr[n][0] == 2):
                        ans += 1
            elif tlr[i][1] == tlr[n][2]:
                if (tlr[i][0] == 1) or (tlr[i][0] == 2):
                    if (tlr[n][0] == 1) or (tlr[n][0] == 3):
                        ans += 1
            """
            if tlr[i][0] in [1, 3]:
                if tlr [n][0] in [1, 2]:
                    if tlr[i][2] == tlr[n][1]:
                        ans += 1
                    else:
                        pass
                else:
                    pass
            elif tlr[i][0] in [1, 2]:
                if tlr[n][0] in [1, 3]:
                    if tlr[i][1] == tlr[n][2]:
                        ans += 1
                    else:
                        pass
                else:
                    pass
            else:
                pass
            """

print(ans)