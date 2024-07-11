lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
prize = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

zero = 0
cnt = 0


for i in lottos:
    if i in win_nums:
        cnt += 1
    elif i == 0:
        zero += 1

print([prize[zero+cnt], prize[cnt]])