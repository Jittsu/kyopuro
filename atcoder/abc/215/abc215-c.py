import itertools
# import time
s, k = input().split(' ')
k =  int(k)

s_sorted = ''.join(sorted(s))

cnt = 0
continue_cnt = 0
s_num = []
#start = time.time()
for i in range(len(s_sorted)):
    if i == 0:
        s_num.append(str(0))
        continue_cnt += 1
    else:
        if s_sorted[i-1] != s_sorted[i]:
            cnt += continue_cnt
            s_num.append(str(cnt))
            continue_cnt = 1
        else:
            continue_cnt += 1
            s_num.append(str(cnt))

s_iter = itertools.permutations(s_num, len(s_num))
s_list = list(s_iter)
s_list_use = []
#start = time.time()
"""
for i in range(len(s_list)):
    if i == 0:
        s_list_use.append(s_list[i])
    else:
        if s_list[i] in s_list_use:
            pass
        else:
            s_list_use.append(s_list[i])
"""
#start = time.time()
s_tuple = set(s_list)
#print(time.time()-start)
s_list_use = sorted(s_tuple)
print(s_list_use)
#print(time.time()-start)
s_list_use = [''.join(i) for i in s_list_use]
s_list_use = sorted(s_list_use)

junban = s_list_use[k-1]

ans = ''
for n in junban:
    ans += s_sorted[int(n)]

print(ans)