n = int(input())
names = []
flag = True
for _ in range(n):
    name = input()
    if name in names:
        print('Yes')
        flag = False
        break
    names.append(name)
if flag:
    print('No')