n = int(input())

t = list(map(int, input().split(' ')))
s = list(map(int, input().split(' ')))

s_min = s.index(min(s))
s_copy = s.copy()
s_copy.sort()
for i in range(n):
    if i == s_min:
        s_min_num = s_copy[1]
        s_min_sub = s.index(s_min_num)
    else:
        s_min_sub = s_min
    s_min_index = s_min_sub
    if i < s_min_index:
        watch = s[s_min_index:] + s[:i]
        watasu = t[s_min_index:] + t[:i]
    else:
        watch = s[s_min_index:i]
        watasu = t[s_min_index:i]
    watch_reverse = watch.copy()
    watch_reverse.reverse()
    watasu.reverse()
    times = []
    time_sum = 0
    c = 0
    for watch_num, watasu_num in zip(watch_reverse, watasu):
        if c == 0:
            times.append(time_sum+watch_num+watasu_num)
        else:
            times.append(time_sum+watch_num+watasu_num)
        time_sum += watasu_num
        c += 1

    times.append(s[i])
    print(min(times))