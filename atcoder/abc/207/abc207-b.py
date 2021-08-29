ipt = list(map(lambda x: int(x), input().split(' ')))

a = ipt[0]
b = ipt[1]
c = ipt[2]
d = ipt[3]
blue = 0
if b >= (c*d):
    print(-1)
else:
    k = (c * d) - b
    i = a // k
    n = a % k
    if n == 0:
        pass
    else:
        i += 1
    print(i)