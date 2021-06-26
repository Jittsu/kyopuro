# -*- coding: utf-8 -*-

def main():
    ipt = input().split(' ')
    N, M = tuple(map(lambda x: int(x), ipt))
    route_dict = {}
    if M != 0:
        for _ in range(M):
            ipt = input().split(' ')
            a, b = tuple(map(lambda x: int(x), ipt))
            if not a in route_dict:
                route_dict[a] = [b]
            else:
                route_dict[a].append(b)

        pointer = 0
        route_num = 0
        for i in range(N):
            available = [i+1]
            pointer = 0
            flag=True
            while flag:
                if not available[pointer] in route_dict:
                    flag = False
                else:
                    for n in route_dict[available[pointer]]:
                        if not n in available:
                            available.append(n)
                        else:
                            pass
                    if (pointer+1) == len(available):
                        flag = False
                    else:
                        pointer += 1
            route_num += len(available)

        print(route_num)

    else:
        print(N)

if __name__ == '__main__':
    main()