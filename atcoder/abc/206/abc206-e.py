ipt_lr = list(map(lambda x: int(x), input().split(' ')))

find_l = [i for i in range(ipt_lr[0], ipt_lr[1]+1)]
ans_sub = 0
for i in range(find_l):
    x = i
    if not x == 1:
        if (x != 2) and (x % 2 == 0):
            ans_sub += ipt_lr[1] // 2 - x // 2