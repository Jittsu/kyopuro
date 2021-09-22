xy = input()
xy = xy.split('.')
x = xy[0]
y = int(xy[1])

if 0 <= y and y <= 2:
    print(x+'-')
elif 3 <= y and y <= 6:
    print(x)
else:
    print(x+'+')