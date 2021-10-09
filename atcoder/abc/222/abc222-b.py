np = list((map(int, input().split(' '))))
a = list(map(int, input().split(' ')))

cnt = 0
for aa in a:
    if aa < np[1]:
        cnt += 1

print(cnt)