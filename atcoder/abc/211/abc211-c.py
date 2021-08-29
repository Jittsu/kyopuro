s = input()
chokudai = ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']
end_flag = True
for n in chokudai:
    if not n in s:
        end_flag = False
        break

ans = 0
if end_flag:
    s = s[s.find('c'):s.rfind('i')]
    c_snum = s.find('c')
    h_snum = s.find('h', c_snum)
    if h_snum == -1:
        end_flag = False
    o_snum = s.find('o', h_snum)
    if o_snum == -1:
        end_flag = False
    k_snum = s.find('o', o_snum)
    if k_snum == -1:
        end_flag = False
    u_snum = s.find('o', k_snum)
    if u_snum == -1:
        end_flag = False
    d_snum = s.find('o', u_snum)
    if d_snum == -1:
        end_flag = False
    a_snum = s.find('o', d_snum)
    if a_snum == -1:
        end_flag = False
    i_snum = s.find('o', a_snum)
    if i_snum == -1:
        end_flag = False
    
    if end_flag:
        i_enum = s.rfind('i', i_snum)
        if i_enum == -1:
            end_flag = False
        a_enum = s.rfind('a', a_snum, i_enum)
        if a_enum == -1:
            end_flag = False
        d_enum = s.rfind('d', d_snum, a_enum)
        if d_enum == -1:
            end_flag = False
        u_enum = s.rfind('u', u_snum, d_enum)
        if u_enum == -1:
            end_flag = False
        k_enum = s.rfind('k', k_snum, u_enum)
        if k_enum == -1:
            end_flag = False
        o_enum = s.rfind('o', o_snum, k_enum)
        if o_enum == -1:
            end_flag = False
        h_enum = s.rfind('h', h_snum, o_enum)
        if h_enum == -1:
            end_flag = False
        c_enum = s.rfind('c', c_snum, h_enum)
        if c_enum == -1:
            end_flag = False

        if end_flag:
            c_cnt = s[c_snum:c_enum].count('c')
            h_cnt = s[c_enum:h_enum].count('h')
            o_cnt = s[h_enum:o_enum].count('o')
            k_cnt = s[o_enum:k_enum].count('o')
            u_cnt = s[k_enum:u_enum].count('o')
            d_cnt = s[u_enum:d_enum].count('o')
            a_cnt = s[d_enum:a_enum].count('o')
            i_cnt = s[a_enum:i_enum].count('o')
            ans += (c_cnt * h_cnt * o_cnt * k_cnt * u_cnt * d_cnt * a_cnt * i_cnt)
            print(ans)

        else:
            print(0)

    else:
        print(0)

else:
    print(0)