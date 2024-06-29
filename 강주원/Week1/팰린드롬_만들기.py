name = input()
my_dict = {chr(i):0 for i in range(65, 91)}
for spell in name:
    my_dict[spell] += 1

cnt_odd = 0
res = ''
for key, value in reversed(list(my_dict.items())):
    cnt = value // 2
    if value % 2 == 1:
        cnt_odd += 1
        if cnt_odd >= 2:
            res = "I'm Sorry Hansoo"
            break
        middle_index = len(res) // 2
        res = res[:middle_index] + key + res[middle_index:]

    res = cnt * key + res + cnt * key

print(res)