from math import ceil

fees = [180, 5000, 10, 600] # 기본 시간 | 기본 요금 | x분 당 | y원
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
answer = []
prefix_sum = dict()
Now = []
for i in records:
    time, number, state = i.split()
    if state == "IN":
        Now.append((number, time))
    else:
        mid = ("", "")
        for i in Now:
            if i[0] == number:
                mid = i
                break

        a = int(mid[1][:2])
        b = int(mid[1][3:5])
        c = int(time[:2])
        d = int(time[3:5])
        add_time = (int(time[:2]) * 60 + int(time[3:5])) - (int(mid[1][:2]) * 60 + int(mid[1][3:5]))

        if number in prefix_sum:
            prefix_sum[number] += add_time
        else:
            prefix_sum[number] = add_time
        Now.remove(mid)



for (i, j) in Now:
    add_time = 24*60 - 1 - (int(j[:2]) * 60 + int(j[3:5]))
    if i in prefix_sum:
        prefix_sum[i] += add_time
    else:
        prefix_sum[i] = add_time

print(prefix_sum)

A = list(prefix_sum.keys())
A.sort()

for i in A:
    mid = prefix_sum[i] - fees[0]
    if mid > 0:
        answer.append(ceil(mid/fees[2]) * fees[3] + fees[1])

    else:
        answer.append(fees[1])

print(answer)