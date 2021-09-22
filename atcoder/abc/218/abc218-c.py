import numpy as np

n = int(input())

s_zahyo = []
for i in range(n):
    s = list(input())
    s = list(np.where(np.array(s) == '#')[0])
    if not len(s) == 0:
        for num in s:
            s_zahyo.append((num, -1*i))

t_zahyo = []
for i in range(n):
    t = list(input())
    t = list(np.where(np.array(t) == '#')[0])
    if not len(t) == 0:
        for num in t:
            t_zahyo.append((num, -1*i))

def rot90(zahyo):
    x = zahyo[0]
    y = zahyo[1]
    deg90 = np.deg2rad(90)
    cos = np.cos(deg90)
    sin = np.sin(deg90)
    xx = round((x * cos) - (y * sin))
    yy = round((x * sin) + (y * cos))

    return xx, yy

s_zahyo_koushin = []
for i, zahyo in enumerate(s_zahyo):
    if i == 0:
        x_kijun = zahyo[0]
        y_kijun = zahyo[1]
    zahyo = (zahyo[0] - x_kijun, zahyo[1] - y_kijun)
    s_zahyo_koushin.append(zahyo)

"""
t_zahyo_koushin = []
for i, zahyo in enumerate(t_zahyo):
    if i == 0:
        x_kijun = zahyo[0]
        y_kijun = zahyo[1]
    zahyo = (zahyo[0] - x_kijun, zahyo[1] - y_kijun)
    t_zahyo_koushin.append(zahyo)
"""

if len(s_zahyo) == len(t_zahyo):
    for i in range(len(t_zahyo)):
        flag = True
        t_zahyo_koushin = []
        x_kijun = t_zahyo[i][0]
        y_kijun = t_zahyo[i][1]
        for zahyo in t_zahyo:
            zahyo = (zahyo[0] - x_kijun, zahyo[1] - y_kijun)
            t_zahyo_koushin.append(zahyo)

        for rot in range(4):
            flag = True
            if not rot == 0:
                new = []
                for n, zahyo in enumerate(s_zahyo_koushin):
                    new_zahyo = rot90(zahyo)
                    new.append(new_zahyo)

                s_zahyo_koushin = new

            for zahyo in s_zahyo_koushin:
                if not zahyo in t_zahyo_koushin:
                    flag = False
                    break

            if flag:
                break

        if flag:
            break

else:
    flag = False

if flag:
    print('Yes')

else:
    print('No')

