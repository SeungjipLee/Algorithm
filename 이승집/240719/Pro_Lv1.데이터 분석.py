# 코드 / 날짜 / 최대 수량 / 현재 수량
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
answer = []

standard = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

for i in data:
    st = standard[ext]
    if i[st] < val_ext:
        answer.append(i)

answer = sorted(answer, key=lambda x: x[standard[sort_by]])

print(answer)