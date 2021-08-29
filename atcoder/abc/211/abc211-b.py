d = {'H': 0, '2B': 0, '3B': 0, 'HR': 0}

for _ in range(4):
    ipt = input()
    d[ipt] += 1

if 0 in list(d.values()):
    print('No')
else:
    print('Yes')