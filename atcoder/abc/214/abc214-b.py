s, t = map(int, input().split(' '))

cnt = 0

for i in range(s+1):
    for ii in range(s+1):
        for iii in range(s+1):
            if (i + ii + iii <= s) and (i * ii * iii) <= t:
                cnt += 1
            else:
                break

print(cnt)