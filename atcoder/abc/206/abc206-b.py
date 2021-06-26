goal = int(input())

flag = True
i = 1
while flag:
    chokin = (1/2) * i * (i+1)
    if chokin >= goal:
        flag = False
    else:
        i += 1
print(i)