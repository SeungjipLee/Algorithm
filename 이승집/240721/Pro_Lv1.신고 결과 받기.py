id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

answer = []
now_report = {i: set() for i in id_list}
cnt_email = {i: 0 for i in id_list}

for i in report:
    a, b = i.split()
    now_report[b].add(a)

print(now_report)

for i in now_report:
    if len(now_report[i]) >= k:
        for j in now_report[i]:
            cnt_email[j] += 1

print(cnt_email)

for i in cnt_email:
    answer.append(cnt_email[i])

print(answer)