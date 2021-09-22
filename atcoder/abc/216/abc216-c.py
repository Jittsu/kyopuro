n = int(input())
i = n
ans = ''
while True:
    if n == 1:
        ans += 'A'
        break
    else:
        if int(n % 2) == 1:
            n -= 1
            n //= 2
            i -= 1
            i /= 2
            if n != i:
                print(n, int(i))
                print(type(n), type(i))
                break
            ans += 'AB'
        else:
            n //= 2
            i /= 2
            if n != i:
                print(n, int(i))
                print(type(n), type(i))
                break
            ans += 'B'
ans = ans[::-1]
print(ans)
print(len(ans))

"""
ans = ''
if n < 120:
    for _ in range(n):
        ans += 'A'
    print(ans)

else:
    cnt = 2
    while True:
        sho = n // cnt
        amari = n % cnt
        if sho + amari + cnt <= 120:
            break
        else:
            cnt += 1
    ans += 'A' * cnt
    ans += 'B' * sho
    ans += 'A' * amari
    print(ans)
    print(len(ans))

else:
    fuyasu = 1
    ans += 'A'
    while True:
        fuyasu = fuyasu * 2
        if fuyasu > n:
            fuyasu = fuyasu / 2
            break
        else:
            ans += 'B'

    while True:
        if fuyasu == n:
            break
        else:
            fuyasu += 1
            ans += 'A'

    print(ans)
"""