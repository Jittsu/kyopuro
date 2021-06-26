# -*- coding: utf-8 -*-

def main():
    num_tree = int(input())
    num_mi = input().split(' ')
    num_mi = list(map(lambda x: int(x), num_mi))
    sum_mi = 0

    for mi in num_mi:
        if mi > 10:
            sum_mi += mi - 10
        else:
            pass

    print(sum_mi)

if __name__ == '__main__':
    main()