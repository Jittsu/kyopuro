import math
n, m = map(int, input().split(' '))

a = list(map(lambda x: int(x), input().split(' ')))

ans = []
for p in range(m):
    b = True
    for q in range(n):
        r = math.gcd(a[q], p+1)
        if r != 1:
            b = False
    if b:
        ans.append(p+1)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])