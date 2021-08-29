N, K = map(int, input().split())
"""
ans = 0
for n in range(N):
    n = str(n + 1)
    a = 1
    flag = True
    for i in range(len(n)):
        a = a * int(n[i])
        if a > K:
            flag = False
            break
        else:
            pass

    if flag:
        ans += 1

print(ans)
"""

import collections

ans = 0
num_str = [str(i) for i in range(10)]
for n in range(N):
    n = str(n+1)
    count = collections.Counter(n)
    if '0' in count:
        ans += 1
    else:
        s = 1
        flag = True
        for num in list(count.keys()):
            num_int = int(num)
            num_ue = int(count[num])
            s = s * (num_int ** num_ue)
            if s > K:
                flag = False
                break
            else:
                pass

        if flag:
            ans += 1
    
print(ans)