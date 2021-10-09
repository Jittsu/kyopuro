n = int(input())
a_s = list(map(int, input().split(' ')))
b_s = list(map(int, input().split(' ')))

cnt = 1
for i, (a, b) in enumerate(zip(a_s, b_s)):
    if i == 0:
        c = b - a + 1
        cnt = cnt * c
        pred_b = b
    else:
        c = b - a + 1
        iran = (pred_b - a) * (pred_b - a + 1) // 2
        c -= iran
        cnt = cnt * c
        pred_b = b

print(cnt%998244353)