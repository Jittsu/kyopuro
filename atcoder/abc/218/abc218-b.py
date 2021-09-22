s = 'abcdefghijklmnopqrstuvwxyz'
p = []

p = list(map(int, input().split(' ')))

ans = ''
for i in p:
    num = i - 1
    ans = ans + s[num]

print(ans)