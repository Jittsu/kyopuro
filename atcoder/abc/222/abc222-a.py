n = input()

if len(n) == 1:
    ans = '000' + n
elif len(n) == 2:
    ans = '00' + n
elif len(n) == 3:
    ans = '0' + n
else:
    ans = n

print(ans)