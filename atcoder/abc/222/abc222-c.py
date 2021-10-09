n, m = map(int, input().split(' '))
shoki_num = [n*2 - i for i in range(n*2)]
shoki_p = [0 for _ in range(n*2)]
shoki = dict(zip(shoki_num, shoki_p))

gcp = []
for _ in range(n*2):
    kojin = input()
    gcp.append(kojin)

for rounds in range(m):
    juni = list(shoki.keys())
    for battle in range(n):
        if rounds == 0:
            zensha = gcp[battle*2][rounds]
            kosha = gcp[battle*2+1][rounds]
            if zensha == 'G':
                if kosha == 'C':
                    shoki[n*2-(battle*2)] += 1
                elif kosha == 'P':
                    shoki[n*2-(battle*2+1)] += 1
                else:
                    pass
            elif zensha == 'C':
                if kosha == 'P':
                    shoki[n*2-(battle*2)] += 1
                elif kosha == 'G':
                    shoki[n*2-(battle*2+1)] += 1
                else:
                    pass
            else:
                if kosha == 'G':
                    shoki[n*2-(battle*2)] += 1
                elif kosha == 'C':
                    shoki[n*2-(battle*2+1)] += 1
                else:
                    pass

        else:
            zensha = gcp[n*2-juni[n*2-(battle*2)-1]][rounds]
            kosha = gcp[n*2-juni[n*2-(battle*2+1)-1]][rounds]
            if zensha == 'G':
                if kosha == 'C':
                    shoki[juni[n*2-(battle*2)-1]] += 1
                elif kosha == 'P':
                    shoki[juni[n*2-(battle*2+1)-1]] += 1
                else:
                    pass
            elif zensha == 'C':
                if kosha == 'P':
                    shoki[juni[n*2-(battle*2)-1]] += 1
                elif kosha == 'G':
                    shoki[juni[n*2-(battle*2+1)-1]] += 1
                else:
                    pass
            else:
                if kosha == 'G':
                    shoki[juni[n*2-(battle*2)-1]] += 1
                elif kosha == 'C':
                    shoki[juni[n*2-(battle*2+1)-1]] += 1
                else:
                    pass
    shoki = dict(sorted(shoki.items(), key=lambda x: (x[1], x[0])))
ans = list(shoki.keys())
for ansnum in range(n*2):
    print(n*2+1-ans[n*2-1-ansnum])