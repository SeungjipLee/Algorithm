s = input()
one_cnt = s.count('1') // 2
zero_cnt = s.count('0') // 2
s_length = one_cnt + zero_cnt
new_s = ''
for ch in s:
    if len(new_s) == s_length:
        break

    if ch == '1':
        if one_cnt <= 0:
            new_s += '1'
        else:
            one_cnt -= 1
    else:
        if zero_cnt > 0:
            new_s += '0'
            zero_cnt -= 1

print(new_s)