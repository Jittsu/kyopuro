# -*- coding: utf-8 -*-

def main():
    ipt = input().split(' ')
    if ipt[0] == ipt[1]:
        ans = int(ipt[0])
        print(ans)
    else:
        ans = list(set(['0', '1', '2']) - set(ipt))
        ans = int(ans[0])
        print(ans)

if __name__ == '__main__':
    main()