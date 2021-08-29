n = int(input())

i = 1
while True:
    if 2**i > n:
        break
    else:
        i += 1

print(i-1)