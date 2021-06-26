N = int(input())
A = list(map(lambda x: int(x), input().split(' ')))

ans = 0

cnts = {}
used = {}
for i in A:
    if not i in cnts:
        cnts[i] = 0
        cnts[i] += 1
        used[i] = 0
    else:
        cnts[i] += 1
for i, num in enumerate(A):
    find = len(A) - i - 1
    sub_ans = find - (cnts[num] - used[num] - 1)
    used[num] += 1
    ans += sub_ans
    
print(ans)